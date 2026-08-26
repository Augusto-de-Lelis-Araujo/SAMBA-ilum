# Quantum ESPRESSO — read this before your first run

VASProcar supports QE, but its file expectations differ from the naming most
QE tutorials use. **Getting the names wrong causes the program to hang
silently — no output, no error, no exit.** That is the single most common way
a QE user loses an afternoon here, so it comes first.

## The `bands.in` trap

VASProcar expects **`bands.in` to be the input of `bands.x`** — the
post-processing step. Most QE tutorials use `bands.in` for the **`pw.x`**
run with `calculation='bands'`, and give the `bands.x` input another name
(`bandsx.in`, `bands_pp.in`, `bands.pp.in`…).

Tell them apart by what is inside:

```fortran
! pw.x input  -- NOT what VASProcar wants as bands.in
&CONTROL
    calculation='bands'
    prefix='BiAs'
    outdir = './outdir'
/
&SYSTEM
    ...
```

```fortran
! bands.x input -- THIS is what VASProcar wants as bands.in
&bands
    prefix = 'BiAs'
    outdir = './outdir'
    filband = 'bands.dat'
    lsym = .false.
/
```

**The rule: the file VASProcar reads as `bands.in` must contain a `filband`
line.** If it does not, VASProcar looks for `filband` until the end of the
file and then keeps looking — forever.

> [!CAUTION]
> **Symptom of getting this wrong:** you select a band-structure option, the
> program prints nothing further, and never returns. `output/` contains only
> `BibTeX.dat` and `DOI.png`. There is no error message, no traceback, and no
> timeout. If that happens, press Ctrl-C and check your `bands.in` for a
> `filband` line before anything else.
>
> This affects released versions up to at least 1.1.22.139. It is a known
> defect, not something you have done wrong.

Fixing it is a rename, not a rerun:

```bash
cp bandsx.in bands.in        # keep a copy of the pw.x input under another name first
```

## Files VASProcar expects

The program prints this list when you choose the QE backend — but only at
runtime, so here it is up front:

| Role | Expected name | Produced by |
|---|---|---|
| SCF input / output | `scf.in`, `scf.out` | `pw.x` |
| NSCF input / output | `nscf.in`, `nscf.out` | `pw.x` |
| **bands.x input** | `bands.in` — **must contain `filband`** | you |
| bands.x output | `bands.out` | `bands.x` |
| eigenvalue file | whatever `filband` names, e.g. `bands.dat` | `bands.x` |
| gnuplot companion | `<filband>.gnu`, e.g. `bands.dat.gnu` | `bands.x` |
| projections (optional) | `projwfc.in`, `projwfc.out` | `projwfc.x` |
| projected wavefunctions | `<filproj>.projwfc_up` | `projwfc.x` |
| projected DOS | `<filpdos>.pdos_atm#…` | `projwfc.x` |

> [!IMPORTANT]
> The projection options (`31`, `32`, `33`, `35`, `37`) need **`projwfc.x` to
> have been run already**. VASProcar does not compute projections; it reads
> them. If you have not run `projwfc.x`, those options have nothing to work
> with.

## What the QE menu offers

The QE menu is **smaller than the VASP menu**, and the numbers are not the
same as the ones in VASP-oriented documentation.

| Type | What you get |
|---|---|
| `10` | Band structure along the k-path |
| `30` | Density of states: DOS, projected DOS, local DOS |
| `31` | Orbitals S, P, D, F projected onto the bands |
| `32` | Atomic contribution projected onto the bands |
| `33` | Atomic-orbital contribution — character of the states |
| `35` | Atomic/orbital contribution table + penetration length |
| `37` | Total angular momentum J, 2D projection — **QE only**, needs spin-orbit coupling |
| `7` / `-7` | version check / install modules |
| `8`, `9` | SAMBA, DFT2kp |

> [!WARNING]
> `30` is the **density of states**; `31` is the **orbital projection**.
> Documentation published before 2026-08-25 has these two swapped. A QE user
> looking for projected bands wants **`31`** — following the old numbering
> gives a density of states that can be mistaken for one.

Not available on the QE backend, whatever older documentation implies:

- **`999`** (the info summary) — VASP only
- **`[2]` spin menu** (`20`–`23`) — VASP only
- **`[4]` densities/optics** (`40`–`43`) — VASP only
- **`[5]` file tools** (`50`–`57`) — VASP only

## First run

```bash
cd /path/to/your/qe/calculation
python -m vasprocar
```

The first question is which DFT code you used. Answer **`2`** for QE:

```
##############################################################
# Which package was used for the DFT calculations? ===========
# [1] VASP (Vienna Ab initio Simulation Package)
# [2] QE (Quantum ESPRESSO)
# [3] SIESTA: Hamiltonian analysis using the sisl package
##############################################################
```

If your directory contains only QE files this question is skipped and QE is
detected automatically. It appears when detection is ambiguous — for instance
if a stray `KPOINTS` or `CHGCAR` from a VASP run is also present.

> [!CAUTION]
> Answering this wrongly runs the other backend's parser on your files. There
> is no confirmation step.

Then pick a task from the table above. Output goes to `./output/`.

## Checklist before you report a problem

1. Does `bands.in` contain a `filband` line? *(the hang)*
2. Does the file named by `filband` exist, and its `.gnu` companion?
3. For any projection option: did you run `projwfc.x`?
4. Are you using an **absolute** path if you passed a directory argument?
5. Does the version in the banner match the documentation you are reading?

If all five are yes and it still fails, open an issue with the banner line,
your directory listing, and the last 20 lines of terminal output.
