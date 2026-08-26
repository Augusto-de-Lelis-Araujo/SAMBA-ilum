# Troubleshooting

Every entry here was hit by a real first-time user during the 2026-08-25
usability audit. Ordered by how often people ran into it.

## It will not start

### `ImportError: cannot import name 'main' from 'vasprocar'`

The `vasprocar` console script is broken in released versions up to and
including 1.1.20.061. Use the module form:

```bash
python -m vasprocar
```

### `No module named vasprocar`

Either it is not installed (`pip install vasprocar`), or it is installed in a
different Python than the one you are running. Check:

```bash
python -c "import vasprocar, sys; print(sys.executable, vasprocar.__file__)"
```

On Windows use `python`, not `python3` — `python3` usually does not exist
there, even though older documentation suggests it.

### `FileNotFoundError: .../output`

You passed a **relative** path. Use `cd`, or give an absolute path:

```bash
cd /data/my-run && python -m vasprocar      # correct
python -m vasprocar /data/my-run            # correct
python -m vasprocar ./my-run                # this error
```

A relative path also silently breaks backend detection, so you may be asked
which DFT code you used and then have the wrong parser run on your files.

## It asks something I did not expect

### "Which package was used for the DFT calculations?"

The first prompt, when VASProcar cannot tell which code produced your files.
Answer `1` VASP, `2` QE, `3` SIESTA.

It appears when the directory is ambiguous — for example a QE run that also
contains a leftover `KPOINTS`, or when a relative path prevented detection
from seeing anything at all.

> [!CAUTION]
> There is no confirmation. Answering wrongly runs the other backend's parser
> on your files.

### "Attention: edit the KPOINTS file and add a label to every k-point"

Not an error — a prerequisite. Band-structure plotting needs a label in the
fourth column of every k-point line in `KPOINTS`:

```
   0.5000   0.0000   0.0000    M
   0.3333   0.3333   0.0000    K
```

Add them by hand. VASP ignores that column; VASProcar uses it for the axis.

## It produces nothing, and does not come back

### QE band structure or projections hang silently

**Cause:** `bands.in` must be the input of **`bands.x`** — the file containing
a `filband` line. Most QE tutorials use `bands.in` for the `pw.x` run and give
the `bands.x` input another name (`bandsx.in`, `bands_pp.in`).

When `filband` is absent, VASProcar scans for it past the end of the file and
never stops. No error, no timeout, no output beyond `BibTeX.dat` and
`DOI.png`.

**Fix:** make sure the file named `bands.in` contains `filband`:

```bash
grep filband bands.in     # must print something
cp bandsx.in bands.in     # if it does not, and bandsx.in is your bands.x input
```

Setting `MPLBACKEND=Agg` does **not** help — it is not a plotting problem.

Full detail: [QE guide](quickstart-qe.md).

### A projection option produces nothing (QE)

Options `31`, `32`, `33`, `35`, `37` read projections; they do not compute
them. Run `projwfc.x` first.

## It finished, but I do not trust the figure

### The energy axis is not what I expected

`[10]` and the other `[n]` defaults **shift the energy zero to E_F without
asking**. Your axis is `E − E_F`. Use `[-n]` to control it.

### I used an option number from older documentation

Several numbers changed. If you followed a guide written before 2026-08-25,
check these:

| Old docs said | Actually is now |
|---|---|
| `30` orbital projections | `31` — `30` is the **DOS** |
| `31` DOS | `30` — `31` is the **orbital projection** |
| `36` table + penetration length | `35` |
| `51` generate KPOINTS | `54` |
| `53` merge POTCAR | `55` |
| `55` check and fix files | `56` |
| `54` multiple-PROCAR tip | `57` |
| `[7]` install modules | `[-7]` — `[7]` only checks the version |

Both numbers in the `30`/`31` swap run without error and both produce a
plausible figure, so nothing warns you. If you have a DOS that should be an
orbital projection, this is why.

### My output is not in `output/`

Almost everything goes to `./output/<Task>/`. The exception: the KPOINTS
generator `[54]` writes to **`KPOINTS_generated/`**.

## Automation and batch runs

### The run ends with `EOFError: EOF when reading a line`

Expected, and harmless if your work is done. After each task VASProcar asks
"Do you want to perform another task?"; that prompt reads stdin without EOF
handling, so a piped run ends with a traceback once the input runs out.

Your figures and `.dat` files are already written. To keep logs clean, feed a
final `0`:

```bash
printf '999\n0\n' | python -m vasprocar /abs/path
```

Note that this prompt also rejects non-numeric input with a `ValueError`,
unlike the menus, which re-prompt.

### There is no `--help` and no command-line flags

Correct — there are none. Unrecognised arguments are ignored silently. Driving
VASProcar non-interactively is done with **input files** (option `[6]`), not
flags: see [Automation](automation.md).

### `[6]` is not in my menu

`[6]` exists on the VASP backend only. The QE menu offers
`10, 30, 31, 32, 33, 35, 37, 7, 8, 9` and nothing else.

## Missing optional dependencies

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: pymatgen` on `[51]` | `pip install pymatgen` |
| SIESTA backend unavailable | `pip install sisl` |
| `.agr` files you cannot open | install [Grace/xmgrace](https://plasma-gate.weizmann.ac.il/Grace/) — no Windows build exists; use the `.py` script or the `.dat` file instead |

## Reporting a problem

Include:

1. the version line VASProcar prints at startup;
2. your OS and how you installed;
3. `output/info.txt` if you got that far;
4. a listing of your working directory;
5. the last ~20 lines of terminal output.

Note that three versions are currently in circulation — 1.1.19.188 in older
documentation, 1.1.20.061 on PyPI, 1.1.22.139 in the development tree — so the
version line matters.
