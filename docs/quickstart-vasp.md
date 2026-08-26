# Your first figure in 10 minutes (VASP)

You need a finished VASP calculation with `CONTCAR`, `OUTCAR`, `PROCAR` and
`KPOINTS`. `PROCAR` exists only if you ran with **`LORBIT = 11`**.

Every command below was executed against a real SOC calculation while writing
this page.

## Step 1 — check that VASProcar understands your calculation

```bash
cd /path/to/your/calculation
python -m vasprocar
```

At the task menu type **`999`**, then `0` to leave.

This reads your files and writes `output/info.txt`. Nothing else. Open it:

```
LNONCOLLINEAR = .TRUE. (Non-collinear Calculation)
LSORBIT = .TRUE. (Calculation with SO coupling)
----------------------------------------------------
No. of k-points = 960;  No. of bands = 20
No. of ions = 2;  No. of electrons = 10.0
---------------------------------------------------
LORBIT = 11;  ISPIN = 1 (without spin polarization)
---------------------------------------------------
Last occupied band = 10
First empty band = 11
Conduction band minimum (CBM) = -3.0052 eV  -  k-point 469
Valence band maximum (VBM)    = -3.031 eV  -  k-point 467
GAP (indirect) = 0.0258 eV
```

**Read this before making any figure.** It is the cheapest way to catch a
misunderstanding:

- Do the flags match the calculation you ran? If you ran spin-polarised and it
  says `ISPIN = 1`, stop — every figure downstream would be wrong.
- Is the electron count right? The occupied-band count follows from it.
- Is the gap plausible for your system?

`info.txt` is also what you should attach to a bug report.

## Step 2 — check your KPOINTS labels

> [!IMPORTANT]
> For a band structure, **every k-point line in your `KPOINTS` file needs a
> label** in the fourth column. If they are missing, option `[10]` stops and
> tells you to add them — before producing anything.

Line-mode `KPOINTS`, correctly labelled:

```
Special k-points for band structure
240
Line-mode
reciprocal
   0.5000   0.0000   0.0000    M
   0.3333   0.3333   0.0000    K

   0.3333   0.3333   0.0000    K
   0.0000   0.0000   0.0000    G
```

The trailing `M`, `K`, `G` are the labels. Add them by hand if your file has
none — VASP ignores them, VASProcar needs them.

## Step 3 — the band structure

```bash
python -m vasprocar
```

Type **`1`** (Energy), then **`10`** (band structure, defaults).

You will get `output/Bands/`:

| File | What it is |
|---|---|
| `Bands.png` | the figure |
| `Bands.dat` | the numbers — k-axis distance and one column per band |
| `Bands.py` | the matplotlib script that drew the figure |
| `Bands.agr` | Grace/xmgrace project, if enabled |

`Bands.py` is the useful one. Restyle the figure — colours, limits, fonts —
by editing it and re-running it, with no need to re-parse the PROCAR.

> [!WARNING]
> **`[10]` shifts the energy zero to E_F by default.** Your y-axis is
> `E − E_F`, not the raw eigenvalues. This is almost always what you want,
> but it is applied without asking. Use `[-10]` if you need to control it, or
> any other parameter.

## Step 4 — labels and limits

`[10]` uses defaults for everything. **`[-10]`** walks you through the same
analysis asking for each choice: energy window, which bands, k-point labels,
Greek letters (Γ instead of `G`), output formats, and whether to shift E_F.

Use `[10]` to see whether the data is right. Use `[-10]` for the figure that
goes in the paper.

## Where to go next

| You want | Read |
|---|---|
| any other analysis | [Option reference](options.md) |
| to run this unattended, on many directories | [Automation](automation.md) |
| something went wrong | [Troubleshooting](troubleshooting.md) |
| Quantum ESPRESSO instead | [QE guide](quickstart-qe.md) |

## If `python -m vasprocar` is not what you should type

Two traps, both common:

**The bare `vasprocar` command fails** in released versions up to 1.1.20.061:

```
ImportError: cannot import name 'main' from 'vasprocar'
```

Use `python -m vasprocar` instead.

**A relative path argument fails.** These are not equivalent:

```bash
cd /data/my-run && python -m vasprocar     # correct
python -m vasprocar /data/my-run           # correct (absolute)
python -m vasprocar ./my-run               # FAILS
```

The relative form dies with `FileNotFoundError: .../output`, and before that
it defeats backend detection — so it may ask which DFT code you used and then
run the wrong parser. Use `cd`, or an absolute path.
