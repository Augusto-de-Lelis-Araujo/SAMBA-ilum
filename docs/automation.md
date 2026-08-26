# Running VASProcar unattended

**Yes, it can run with no human present.** No prompts, no display, no stdin.
This page shows how; the mechanism is input files, not command-line flags.

Verified while writing this page: with an `inputs/` directory in place, no
stdin (`< /dev/null`), `DISPLAY` unset and `MPLBACKEND=Agg`, VASProcar exited
`0` and wrote `output/info.txt` and a complete `output/Bands/` set.

## How it works

If a directory named **`inputs/`** exists in your calculation directory,
VASProcar looks inside it for files named `input.vasprocar.<task>`. If it
finds any, it **skips the menu entirely** and runs each one in turn, reading
every parameter from the file.

```
my-calculation/
├── CONTCAR
├── OUTCAR
├── PROCAR
├── KPOINTS
├── inputs/
│   ├── input.vasprocar.info
│   └── input.vasprocar.bands
└── output/          ← created for you
```

```bash
cd my-calculation
python -m vasprocar          # runs both tasks, asks nothing, exits
```

## Getting the templates

Run VASProcar interactively once and choose **`6`**. It offers one template
per task, or `[1]` for all of them, and writes them into `inputs/`.

Then edit the ones you want, delete the ones you do not, and the directory is
ready to be copied to every calculation you need to process.

## The tasks you can automate

Ten. The filename determines which analysis runs, and the file supplies the
parameters the interactive `[-n]` path would have asked for:

| File `inputs/input.vasprocar.…` | Runs | Equivalent to |
|---|---|---|
| `info` | basic information extraction | `999` |
| `bands` | band structure 2D | `-10` |
| `contour_levels` | constant-energy contours | `-11` |
| `spin` | spin components on bands | `-20` |
| `spin_video` | spin texture video | `-23` |
| `dos` | DOS / pDOS / lDOS | `-30` |
| `orbitals` | orbital S,P,D,F projection | `-31` |
| `atomic` | atomic-contribution projection | `-32` |
| `locpot` | electrostatic potential | `-40` |
| `chgcar` | charge density | `-41` |

> [!IMPORTANT]
> Tasks run in the order of the table above, **not** the order you created the
> files. If you want `info` to run first so you can check the parse before the
> figures, note that it currently runs **last**. Run it as a separate job if
> the ordering matters to you.

> [!NOTE]
> Only these ten are automatable. The spin textures `[21]`/`[22]`, the
> isosurfaces `[13]`/`[14]`, the dielectric function `[43]` and every `[5]`
> file tool have no input-file equivalent and must be driven interactively.

## In a scheduler

Nothing special is required — no flags, no environment variables beyond a
headless matplotlib backend:

```bash
#!/bin/bash
#SBATCH --job-name=vasprocar
#SBATCH --time=00:30:00

export MPLBACKEND=Agg          # no display on a compute node

cd "$SLURM_SUBMIT_DIR/my-calculation"
python -m vasprocar < /dev/null
```

Over many directories:

```bash
for d in /data/runs/*/; do
    cp -r /templates/inputs "$d"
    ( cd "$d" && MPLBACKEND=Agg python -m vasprocar < /dev/null ) \
        > "$d/vasprocar.log" 2>&1
done
```

> [!TIP]
> `MPLBACKEND=Agg` is good practice on a headless node, though the automated
> path does not open windows. Redirecting stdin from `/dev/null` guarantees
> nothing can ever block waiting for input.

## Things to know before you trust it in a pipeline

**Use `cd`, or an absolute path.** A relative path argument fails with
`FileNotFoundError: .../output` and defeats backend detection. In a loop,
`cd` into each directory as above.

**Check the exit code, but do not rely on it alone.** A successful automated
run exits `0`. Verify that the files you expect actually appeared:

```bash
python -m vasprocar < /dev/null || echo "FAILED: $PWD"
[ -f output/Bands/Bands.dat ] || echo "NO OUTPUT: $PWD"
```

**Parse `output/info.txt` as your sanity gate.** It records the flags, counts,
E_F and gap VASProcar believed. Comparing `ISPIN`/`LSORBIT` against what you
submitted catches a mis-detected backend before you inherit a directory of
wrong figures.

**Quantum ESPRESSO cannot be automated this way.** The `inputs/` mechanism is
populated only on the VASP backend, and `[6]` does not appear in the QE menu.
QE runs must be driven interactively — or by piping answers to stdin, which is
not a documented interface and may change.

**Interactive runs end with a traceback.** When you *do* pipe answers, the
final "Do you want to perform another task?" prompt reads stdin without EOF
handling, so the log ends in `EOFError`. Harmless — the outputs are already
written — but it makes naive `stderr`-is-failure checks report false
failures. The automated `inputs/` path does not have this problem.

**There is no `--help` and no flags.** Unrecognised command-line arguments are
ignored silently.
