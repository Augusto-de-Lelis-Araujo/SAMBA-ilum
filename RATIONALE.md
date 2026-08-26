# Why the new tutorial is shaped this way

Step 4 of the plan. Every structural decision below answers a specific finding
from `../findings/synthesis.md` (six first-contact student sessions),
`../findings/capability_gap.md` (author-side comparison against the code) or
`../findings/github_limits.md` (the medium). Nothing here is a matter of taste
that could not be traced back to evidence.

**`../README.md` — the document under test — was not modified.** This is a
parallel proposal.

## What is here

```
new_tutorial/
├── README.md                     the new front page (~150 lines, was 2505)
├── docs/
│   ├── quickstart-vasp.md        zero to a first figure
│   ├── quickstart-qe.md          the entirely undocumented backend
│   ├── options.md               every option, correct numbers
│   ├── automation.md             the unattended path
│   └── troubleshooting.md        every blocker students actually hit
├── tools/
│   └── check_docs_vs_code.py     the drift gate
└── .github/workflows/
    └── docs-consistency.yml      runs the gate + 4 cheaper checks
```

## Decision → evidence

| Decision | Answers |
|---|---|
| **Split one 2505-line README into a front page + 5 pages** | Navigation was the only friction **all 6/6** students hit. github_limits §2: `<details>` forfeits anchors, the free heading-TOC, and reliable in-page search; 0 internal anchors existed in 2506 lines. Splitting is the only branching mechanism GitHub offers (§5.2). |
| **Real markdown headings; `<details>` only for long transcripts** | Restores anchors + auto-TOC for free (github_limits §2a/2b). The 135 collapsed blocks made content unfindable and unlinkable. |
| **Quickstart is the first link, and ends in a figure** | The #1 requested change in the students' own "Unblocker" fields. t01 calculated that one verified command block plus a 5-line first-figure path would have removed *every blocker* in her report. Mean "first result" score was 1.7/5. |
| **`python -m vasprocar`, never the bare `vasprocar`** | Verified crash in the published package: `ImportError: cannot import name 'main'` (BUG-18, live in 1.1.20.061). 5/6 students hit the broken launch command. |
| **Path rules stated with a CAUTION, `cd` shown first** | 6/6 students. The relative-path form fails *and* silently defeats backend detection, so it can run the wrong parser (capability_gap G-6, BUG-01). |
| **`999` taught first, before any figure** | Undocumented (G-5) yet repeatedly the thing that let students verify what the tool had understood. t01 confirmed her non-collinear run from `info.txt` alone. |
| **Corrected option numbers, with a WARNING naming the old ones** | capability_gap G-1: 9 numbers ran a different analysis; `30`/`31` swapped; `[5]` shifted by 1–3. 4/6 students hit it. The old→new table is kept because readers arrive holding the old numbers. |
| **`[7]` vs `[-7]` called out explicitly** | G-2. `[7]` only checks a version; the installer is `[-7]`, previously undocumented — the exact thing a reader with a missing module needs. |
| **The DFT-package prompt documented, with a CAUTION** | G-3. The program's *first* question was absent from the tutorial. 4/6 students met it unprepared; answering wrongly runs the other backend's parser. |
| **A whole page for QE, opening with the `bands.in` trap** | G-4: QE appeared 5× in 2505 lines, all about DFT2kp; SIESTA 0×. t03 and t05 independently lost their entire sessions to a silent infinite hang. Cause confirmed on a fixture copy: `bands.in` is the pw.x input (no `filband`), and the reader scans past EOF forever (BUG-07). |
| **Per-backend "what each menu accepts" table** | t03 was blocked because the documented automation route `[6]` **does not exist** on the QE menu. Backend surfaces differ and nothing said so. |
| **Every optional dependency named at point of use** | G-7. `pymatgen` (for `[51]`) and `sisl` (SIESTA) are undeclared in `setup.py` (BUG-31) *and* unmentioned. `[51]` is also where the old `[51]`→ KPOINTS mis-numbering sends people. |
| **macOS listed; Windows given real commands** | 5/6 flagged macOS's absence. t04 showed the Windows fallback the README offers uses `python3`, which Windows lacks; conda unmentioned; Grace has no Windows build. |
| **Defaults' hidden behaviour stated ("`[10]` shifts E_F")** | 5/6 hit "The parameters listed below are applied automatically" followed by no list (27×). t01 nearly accepted a band structure on an undocumented energy zero — synthesis §3.2, the worst outcome in the audit. |
| **An automation page, verified headless** | t03's blocker. The capability exists and is good; the words *batch*, *non-interactive*, *headless*, *stdin*, *config file* appear **nowhere** in 2505 lines. Verified for this page: `inputs/` present, no stdin, `DISPLAY` unset → exit 0, figures written. |
| **Troubleshooting ordered by observed frequency** | Built from the 106 friction entries, not from imagination. |
| **`> [!WARNING]` / `[!CAUTION]` alerts** | github_limits §4: native GitHub feature, previously unused. The traps needed a visual channel prose was not providing. |
| **A mermaid decision tree** | github_limits §4. Replaces menu-dump prose with the "which option do I want?" question readers actually have — and makes a 30/31-style swap visible at a glance. |
| **No placeholders, ever** | 6/6 students. 51 lone `...` descriptions and 5 `Note: bla bla bla…` shipped in the tutorial; for t04 the DOS feature he came for *was* a `...`. A documented-but-empty section is worse than an absent one: it costs the reader the search. |
| **`tools/` + CI workflow** | The structural finding (synthesis §3.4): three drifts were caused by **fixes** — BUG-46 corrected prompts to `[0] NO` (README still says `[0] NOT` 17×), BUG-35 moved KPOINTS output (README still promises `output/`), BUG-32 removed `DFT = '_VASP/'` (README documents it in 9 listings, 0 templates have it). Correcting prose fixes today; the gate fixes the mechanism. |

## The gate

`tools/check_docs_vs_code.py` parses the option→module dispatch and menu
allowlists out of `_settings.py`, parses the numbers the docs claim, and fails
the build on disagreement. Standard library only, no network.

Validated in both directions:

| Target | Result |
|---|---|
| the pre-2026-08-25 `README.md` | **exit 1**, 10 hard mismatches — incl. `[36]` documented-but-absent, and the `[51]`/`[53]`/`[54]`/`[55]` shift |
| `docs/options.md` (this rewrite) | **exit 0**, 38 options documented, 0 mismatches |

It would have caught every BLOCKER in capability_gap the day it was
introduced. Its documented limitation is real and stated in the file: it
detects *disagreement*, it does not certify agreement — against the old README
the 30/31 swap is caught at `[31]` but slips at `[30]`, where "2D Projection of
Orbitals" and "projected-DOS" share a stem. One half of a swap failing the
build is enough to put a human on the pair.

The workflow adds four cheaper checks, each from a real finding: images
resolve (G-9), documented version matches the code (G-8), no untranslated
Portuguese (5/6 students), no placeholders (6/6).

## What this rewrite does not do

Stated plainly so it is not mistaken for finished work:

- **It is a proposal, not a merge.** Paths in the workflow assume the released
  layout (`vasprocar/`, not `vasprocar_dev/`) and need adjusting to wherever it
  lands.
- **It does not cover the whole surface.** `[21]`–`[23]`, `[13]`/`[14]`,
  `[34]`–`[37]`, `[40]`–`[43]` and most of `[5]` are correctly *listed* in
  `options.md` but have no worked example. The old README's per-option
  transcripts are a genuine asset and should be migrated into per-page
  sections — with their numbers corrected and their `...` filled in.
- **SIESTA is still undocumented** beyond "it exists and needs `sisl`". The
  backend's surface was never exercised in this audit.
- **The images were not recovered.** All 8–9 referenced files are absent from
  this tree; confirm against the live repository, since this may be a copying
  artefact rather than a real defect.
- **Nothing here was reviewed by a domain expert.** The physics wording is
  derived from the program's own menu text and the audit's reference notes; the
  author should check it before publishing.
- **No claim is made that the underlying bugs are fixed.** BUG-01 (relative
  path), BUG-07 (QE hang) and BUG-31 (undeclared deps) are open. The tutorial
  documents the workarounds; the defects remain in `../../bugs/bug.md`.
