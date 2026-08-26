#!/usr/bin/env python3
"""
check_docs_vs_code.py — fail when the tutorial documents an option number the
program does not accept, or omits one it does.

Why this exists
---------------
The 2026-08-25 tutorial audit found that nine documented option numbers ran a
different analysis than the tutorial claimed (see ../capability_gap.md, G-1),
including a straight swap of [30] and [31]. The document had not degraded — it
had *drifted*: two renumberings landed in the code and nothing tied the prose
to them. Correcting today's numbers by hand fixes the symptom; this script
fixes the mechanism.

Run it in CI on every push. It needs no dependencies and no network.

    python3 check_docs_vs_code.py --settings vasprocar_dev/src/_settings.py \
                                  --docs README.md

Exit status: 0 = consistent, 1 = mismatches found, 2 = could not parse.

Limits, stated honestly
-----------------------
This checks the *option-number contract* only: which numbers exist, and
whether the doc's label for a number is about the same thing as the program's
own menu label. It cannot tell you whether the prose explaining an option is
correct, and it deliberately does not try.

Label comparison is coarse on purpose — two labels agree if they share any
distinctive content-word stem. That is enough to separate "the doc and the
menu describe the same feature" from "these are two different features", and
it avoids grading English. Tuning happens in GENERIC, not in a threshold.

A worked limitation, so nobody over-trusts this: against the pre-2026-08-25
README the [30]/[31] swap is caught at [31] but *not* at [30], because that
line's "2D Projection of Orbitals" and the menu's "projected-DOS" share the
stem "proj". One half of a swap is enough to fail the build and point a human
at the pair, which is the job — but this tool detects *disagreement*, it does
not certify agreement.
"""

import argparse
import re
import sys

# --------------------------------------------------------------------------
# side A: what the program accepts and prints
# --------------------------------------------------------------------------

def parse_settings(path):
    """Extract accepted option numbers and their menu text from _settings.py.

    Two sources, because the program has two:
      * the ``task_*`` allowlists handed to dynamic_input(), which define what
        the menu will actually accept;
      * the ``print("## [nn] description")`` lines, which are what the user
        reads on screen.
    """
    src = open(path, encoding='utf-8', errors='replace').read()

    accepted = set()
    for m in re.finditer(r'task_\w+\s*=\s*\[([^\]]*)\]', src):
        for tok in re.findall(r'-?\d+', m.group(1)):
            if not tok.startswith('-'):
                accepted.add(tok)
    # allowed_values=[...] inline lists count too (e.g. the DFT prompt)
    for m in re.finditer(r'allowed_values\s*=\s*\[([^\]]*)\]', src):
        for tok in re.findall(r'-?\d+', m.group(1)):
            if not tok.startswith('-'):
                accepted.add(tok)

    # Collect every printed line, in order, keeping its cleaned text. Menu
    # entries come in two shapes:
    #   "## [50] POSCAR: Conversion between Direct/Cartesian coord.  ##"
    #   "## Band Structure plot:                                     ##"
    #   "## [10] Default   --   [-10] Custom                         ##"
    # In the second shape the description sits on the *preceding* lines, so a
    # bare "Default -- Custom" entry has to look backwards to find its meaning.
    printed = []
    for line in src.split('\n'):
        s = line.strip()
        if not s.startswith('print'):
            continue
        m = re.search(r'print\s*\(\s*[fr]?["\'](.*)["\']\s*\)', s)
        if not m:
            continue
        text = re.sub(r'[#=]+', ' ', m.group(1))
        text = re.sub(r'\s{2,}', ' ', text).strip(' -|')
        printed.append(text)

    menu = {}
    for i, text in enumerate(printed):
        hit = re.search(r'\[(\d+)\]\s*(.*)', text)
        if not hit:
            continue
        num, desc = hit.group(1), hit.group(2).strip()
        if re.match(r'(?i)default\b', desc) or not desc:
            # walk back over separators to the nearest real description,
            # accumulating continuation lines (descriptions wrap over 2-3 lines)
            parts = []
            for j in range(i - 1, max(-1, i - 6), -1):
                prev = printed[j].strip()
                if not prev or re.fullmatch(r'[\s\-|]*', prev):
                    continue
                if re.search(r'\[-?\d+\]', prev):
                    break
                parts.insert(0, prev)
                if prev.endswith(':'):
                    break
            if parts:
                desc = ' '.join(parts).strip()
        if num not in menu and len(desc) > 3:
            menu[num] = desc

    dispatch = {}
    lines = src.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('#'):
            continue
        m = re.search(r'option\s*==\s*(\d+)', line)
        if not m:
            continue
        window = '\n'.join(lines[i:i + 6])
        f = re.search(r"execute_python_file\(filename\s*=\s*(.+?)\)", window)
        if f:
            dispatch.setdefault(m.group(1), f.group(1).strip())

    return accepted, menu, dispatch


# --------------------------------------------------------------------------
# side B: what the documentation claims
# --------------------------------------------------------------------------

def parse_docs(path):
    """Extract claimed option numbers + descriptions from the documentation.

    Recognises the three shapes documentation has used:
      * ``<summary>...Option [nn] description</summary>``   (legacy README)
      * a markdown heading ``## Option [nn] - description``  (legacy)
      * a markdown table row ``| `nn` | description | ...`` (current docs)

    The table form is how the rewritten reference is organised, so it is the
    one that matters going forward; the other two are kept so this check can
    also be pointed at older documents.
    """
    claimed = {}

    def add(num, desc, lineno):
        if num.startswith('-'):
            return
        desc = re.sub(r'<[^>]+>', '', desc)
        desc = re.sub(r'[*_`\[\]]', '', desc)
        desc = re.sub(r'\s{2,}', ' ', desc).strip(' -\u2014:|')
        if desc and num not in claimed:
            claimed[num] = (lineno, desc)

    # Menu transcripts inside <pre>/``` blocks use '##' as ASCII decoration
    # ("## [30] Default -- [-30] Custom ##"). Those are not markdown headings
    # and not tables, so code blocks are skipped entirely -- otherwise the
    # transcript of a menu gets mistaken for documentation of it.
    in_code = 0
    for n, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        low = line.lower()
        if '<pre' in low:
            in_code += low.count('<pre')
        if '</pre' in low:
            in_code = max(0, in_code - low.count('</pre'))
            continue
        if line.lstrip().startswith('```'):
            in_code = 0 if in_code else 1
            continue
        if in_code:
            continue

        # legacy: "Option [30] description"
        for m in re.finditer(r'Option \[(-?\d+)\][:\s]*(.*?)(?:</summary>|$)', line):
            add(m.group(1), m.group(2), n)

        # current: a heading naming an option group, e.g. "## `[1]` Energy - ..."
        h = re.match(r'\s*#{1,6}\s*`?\[(-?\d+)\]`?\s*(.*)', line)
        if h:
            add(h.group(1), h.group(2), n)

        # current: a table row whose first cell is just an option number
        if line.lstrip().startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) >= 2:
                first = cells[0].strip('`* ')
                if re.fullmatch(r'-?\d{1,3}', first):
                    add(first, cells[1], n)

    return claimed


# Words too generic to carry meaning in a menu label. Without this list,
# "Generate KPOINTS file" and "…or generate monolayer" look related purely
# because both contain "generate" — which is how a real mismatch hides.
GENERIC = {
    'the', 'and', 'for', 'with', 'from', 'into', 'via', 'each', 'its', 'this',
    'plot', 'plots', 'plotting', 'analysis', 'analyze', 'analysis:', 'file',
    'files', 'code', 'using', 'use', 'used', 'generate', 'generation',
    'generating', 'creation', 'create', 'provides', 'provide', 'extraction',
    'extract', 'results', 'result', 'related', 'different', 'default',
    'custom', 'option', 'options', 'output', 'input', 'inputs', 'data',
    'value', 'values', 'level', 'levels', 'given', 'along', 'well', 'other',
    'all', '2d', '3d', '4d', 'ev', 'tip', 'show', 'shows', 'showing',
}

SHORT_NOISE = {'of', 'in', 'on', 'to', 'at', 'by', 'or', 'if', 'is', 'it', 'an',
               'as', 'be', 'do', 'no', 'so', 'up', 'we', 'you', 'per', 'and'}

def distinctive(s):
    """Content-word stems of a label.

    Stems are 4-character prefixes so that inflections and abbreviations match:
    ``information``/``info`` -> ``info``, ``bands``/``band`` -> ``band``,
    ``projection``/``projected`` -> ``proj``. Two-letter tokens are kept
    because ``Sx``, ``Sy``, ``Sz`` carry real meaning in this interface.
    """
    words = re.findall(r'[a-z][a-z0-9_]*', s.lower())
    out = set()
    for w in words:
        if len(w) < 2 or w in GENERIC or w in SHORT_NOISE:
            continue
        out.add(w[:4])
    return out

def similar(a, b):
    """1.0 if the two labels share any distinctive word, else 0.0.

    Deliberately coarse: the goal is to catch labels that are about entirely
    different things, not to grade prose. Sharing one distinctive word is
    enough to believe the doc and the menu are talking about the same feature.
    """
    da, db = distinctive(a), distinctive(b)
    if not da or not db:
        return 1.0        # nothing to compare -> do not cry wolf
    return 1.0 if (da & db) else 0.0


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--settings', required=True)
    ap.add_argument('--docs', required=True)
    ap.add_argument('--similarity', type=float, default=0.5,
                    help='below this, a description pair is reported (the default '
                         'comparison is binary: shared distinctive word or not)')
    ap.add_argument('--quiet-missing', action='store_true',
                    help='do not fail on options the program accepts but the '
                         'docs omit (useful while a rewrite is in progress)')
    args = ap.parse_args()

    try:
        accepted, menu, dispatch = parse_settings(args.settings)
        claimed = parse_docs(args.docs)
    except OSError as e:
        print(f"FATAL: {e}", file=sys.stderr)
        return 2

    if not accepted or not claimed:
        print("FATAL: parsed nothing — has the file layout changed?",
              file=sys.stderr)
        return 2

    hard, soft = [], []

    # 1. documented but not accepted -> the reader hits "invalid option"
    for num, (line, desc) in sorted(claimed.items(), key=lambda kv: int(kv[0])):
        if num not in accepted:
            hard.append(f"docs:{line} documents [{num}] ({desc[:50]!r}) "
                        f"but the program does not accept it")

    # 2. accepted but undocumented -> an invisible feature
    for num in sorted(accepted, key=int):
        if num in ('0',):
            continue
        if num not in claimed:
            msg = (f"program accepts [{num}] "
                   f"({menu.get(num, '<no menu text>')[:50]!r}) "
                   f"but the docs never document it")
            (soft if args.quiet_missing else hard).append(msg)

    # 3. both sides know the number but mean different things
    for num, (line, desc) in sorted(claimed.items(), key=lambda kv: int(kv[0])):
        prog = menu.get(num)
        if not prog or num not in accepted:
            continue
        r = similar(desc, prog)
        if r < args.similarity:
            hard.append(
                f"docs:{line} [{num}] description does not match the program\n"
                f"        docs says: {desc[:72]}\n"
                f"        menu says: {prog[:72]}\n"
                f"        dispatches: {dispatch.get(num, '?')}  (similarity {r:.2f})")

    for m in soft:
        print(f"warning: {m}")
    for m in hard:
        print(f"MISMATCH: {m}")

    print(f"\n{len(claimed)} options documented, {len(accepted)} accepted by "
          f"the program, {len(hard)} hard mismatches, {len(soft)} warnings")
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())
