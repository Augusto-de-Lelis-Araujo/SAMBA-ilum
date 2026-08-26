# Option reference

Every task VASProcar can run, by the number you actually type.

> [!IMPORTANT]
> The numbers below were generated from the program's own menu allowlists and
> dispatch table (`src/_settings.py`) for version **1.1.22.139**, not
> transcribed by hand. If you are running a different version, check it with
> `[7]` — and if any number here disagrees with what the program prints, trust
> the program and open an issue.

Each task has two forms: **`[n]` runs with sensible defaults**, **`[-n]` asks
you for every parameter**. Only the positive form is listed; the negative form
of any listed number also works.

## Before anything else

| Type | What it does | Needs |
|---|---|---|
| `999` | Read the input files and write `output/info.txt`: flags, k-point and band counts, lattice, reciprocal vectors, E_F, total energy, band gap, VBM/CBM | CONTCAR (or POSCAR) + OUTCAR |

Run this first, always. It is fast, it writes nothing but a text file, and it
tells you whether VASProcar understood your calculation before you spend time
on a figure. If `info.txt` says `ISPIN = 1` for a run you know was
spin-polarised, stop there — everything downstream would be wrong.

**VASP only.** The QE menu does not accept `999`.

## `[1]` Energy — bands and constant-energy surfaces

| Type | What you get |
|---|---|
| `10` | Band structure, 2D plot along the k-path |
| `11` | Constant-energy contours on the 2D Brillouin zone — one plot per energy, showing every band that crosses it |
| `12` | Band topography on the 2D BZ — one plot, one band, several energy contours |
| `13` | Band structure, 3D surface plot `[ki, kj, E]` |
| `14` | Band isosurface `[kx, ky, kz, E]` |

> [!NOTE]
> `11` was called "Fermi surface" in older documentation. It is a
> constant-energy contour at whatever energy you choose; with one energy
> requested automatically it uses E_F, which is the Fermi surface proper.

## `[2]` Spin — components and textures

Requires a **non-collinear** calculation (`LSORBIT = .TRUE.`). On a collinear
run the menu refuses with an explanation; that refusal is correct behaviour,
not a bug.

| Type | What you get |
|---|---|
| `20` | Sx, Sy, Sz projected onto the band structure along the k-path |
| `21` | 2D / 3D / isosurface plots of Sx, Sy, Sz and the SiSj, SxSySz vectors |
| `22` | Sx, Sy, Sz and the SiSj vector along one constant-energy contour |
| `23` | Video of the spin components or SiSj vectors as energy varies |

## `[3]` Projections and density of states

> [!WARNING]
> `30` is the **density of states**; `31` is the **orbital projection**. These
> two were documented the other way round before 2026-08-25. If you followed
> older instructions you may have produced the wrong figure — both numbers run
> without error and both give a plausible-looking plot.

| Type | What you get |
|---|---|
| `30` | Density of states: total DOS, projected DOS, local DOS |
| `31` | Orbitals S, P, D, F projected onto the bands |
| `32` | Atomic contribution projected onto the bands (which atoms each state lives on) |
| `33` | Atomic-orbital contribution — the "character" of each state |
| `34` | Orbital S/P/D/F intensity as a colour map over the 2D BZ |
| `35` | Atomic and orbital contribution per state as a **table**, plus a penetration-length plot |
| `37` | 2D projection of total angular momentum J — **Quantum ESPRESSO only**, and only for calculations with spin-orbit coupling |

`36` does not exist. Older documentation described the feature now at `35`
under the number `36`.

## `[4]` Densities and optical response

| Type | What you get | Needs |
|---|---|---|
| `40` | Planar-averaged electrostatic potential along x, y, z | `LOCPOT` |
| `41` | Planar-averaged charge density along x, y, z | `CHGCAR` |
| `42` | Planar-averaged partial charge density | `PARCHG` |
| `43` | Dielectric function, real and imaginary parts | `vasprun.xml` from a run with `LOPTICS = .TRUE.` |

> [!NOTE]
> `43` needs a `<dielectricfunction>` block in `vasprun.xml`. Without
> `LOPTICS = .TRUE.` the file has none, and the tool tells you so instead of
> plotting.

## `[5]` File creation, correction and manipulation

> [!WARNING]
> These five numbers moved. Documentation written before 2026-08-25 lists
> "Generate KPOINTS" as `51`, "Merge POTCAR" as `53`, "Check and fix" as `55`
> and the multiple-PROCAR tip as `54`. All four are wrong for this version —
> use the table below. Typing the old number runs a different tool that may
> write files.

| Type | What it does | Writes |
|---|---|---|
| `50` | POSCAR: convert between Direct and Cartesian coordinates | `output/<name>_Direct.vasp` or `_Cartesian.vasp` |
| `51` | POSCAR manipulation: recover the unit cell from a supercell, or build a monolayer/stack from a bulk structure. Asks which of the two. | `output/` |
| `52` | POSCAR: replace ions or create vacancies | `output/` |
| `53` | 3D Brillouin-zone plot and k-point scan | `output/` |
| `54` | Generate a KPOINTS file — 2D plane or 3D mesh in the BZ | **`KPOINTS_generated/`**, not `output/` |
| `55` | Combine/merge several POTCAR files | `output/` |
| `56` | Check and fix VASP output files (repairs merged numeric columns) | a `<name>_Original` backup beside the file it fixes |
| `57` | Prints advice on using multiple PROCAR files. Writes nothing. | — |

> [!IMPORTANT]
> `51` needs **pymatgen**, which is not installed automatically:
> `pip install pymatgen`. Without it the option stops with
> `ModuleNotFoundError`.

Unlike every other menu, `[5]` does **not** need CONTCAR/OUTCAR/PROCAR. These
are file tools; they read the file you name. `50`, `51` and `52` want a POSCAR
or CONTCAR; `55` wants POTCARs; `56` wants the damaged file.

## `[6]` Automation via input files

`6` writes a template into your directory. Edit it, leave it there, and the
next run reads it instead of prompting — this is how you drive VASProcar from
a batch script or a scheduler.

See [automation.md](automation.md) for the templates and what each variable
does.

## Maintenance and companion tools

| Type | What it does |
|---|---|
| `7` | Check whether your VASProcar is up to date (queries PyPI; needs network) |
| `-7` | **Install or update the Python modules** VASProcar needs |
| `8` | Install / run **SAMBA** — twisted bilayer generation and high-throughput DFT |
| `9` | Install **DFT2kp** — effective k·p models from QE output |

> [!WARNING]
> `7` and `-7` are different things. `7` only reports a version number.
> The one that installs modules is `-7`. Older documentation listed `[7]` as
> "Install/Update Python modules"; that has never been what `7` does in this
> version.

## What each backend accepts

The menus differ per backend, and the program rejects out-of-range numbers
rather than crashing on them.

| Backend | Accepts |
|---|---|
| **VASP** | `999`, `10`–`14`, `20`–`23`, `30`–`35`, `40`–`43`, `50`–`57`, `6`, `7`, `-7`, `8`, `9` |
| **Quantum ESPRESSO** | `10`, `30`, `31`, `32`, `33`, `35`, `37`, `7`, `8`, `9` |
| **SIESTA** | `1` (install `sisl`), `10`, `20` |

Notable consequences, all of which surprised test users:

- **QE has no `999`.** The info summary is VASP-only.
- **QE has no spin menu** (`20`–`23`) and no `[4]` or `[5]` tools.
- **QE `37`** exists only on the QE side; typing it on VASP is refused.
- **SIESTA is a much smaller surface** than either, and needs `sisl`
  (`pip install sisl`) which is not installed automatically.
