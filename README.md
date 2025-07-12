# SAMBA (Simulation and Automated Methods for Bilayer Analysis) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
## Article available in soon

<details>
<summary><strong>Description</strong></summary>

SAMBA is an open-source Python 3 code capable of:
- Automating the generation of twisted homo- and heterobilayers using the coincidence lattice method, ensuring low lattice mismatch and a wide variety of twist angles.
- Automating DFT calculations via the VASP code in a high-throughput approach, including the creation of input files for different types of DFT calculations, along with a customized execution job.
- Analyzing and extracting results, producing high-quality plots (via the VASProcar code) of various structural and electronic properties, as well as storing the data in JSON files.

<img src="etc/figures/logo.png">

</details>

<details>
<summary><strong>Authors</strong></summary>
  
- Augusto de Lelis Araújo ([ORCID](https://orcid.org/0000-0002-6835-6113))
- Adalberto Fazzio ([ORCID](https://orcid.org/0000-0001-5384-7676))
- Felipe Castro de Lima ([ORCID](https://orcid.org/0000-0002-2937-2620))
- Pedro Henrique Sophia ([ORCID](https://orcid.org/0009-0007-5428-0596))

</details>

<details>
<summary><strong>Meet Institutional and Research Network:</strong></summary>
  
- Ilum - School of Science [link](https://ilum.cnpem.br/en/)
- CNPEM - The Brazilian Center for Research in Energy and Materials [link](https://cnpem.br/en/)
- INCT - Materials Informatics [link](https://inct-mi.pesquisa.ufabc.edu.br/)
- midb.cloud database [link](https://midb.cloud/)

<img src="etc/figures/institucional.png">

</details>

-------------------------------

## Tutorial
Click on the topics below to expand and see the details for each section.

<details>
<summary><strong>Installation</strong></summary>

The latest version of SAMBA code can be installed using the Python Package Index via the **command below**, while the source code is available for download via the [link](https://pypi.org/project/SAMBA-ilum/).  
```bash
pip install samba_ilum
```

**Requirements:** Make sure you have the following requirements
- Linux or Windows environment for bilayer generation
- Linux environment for high-throughput DFT (requires VASPkit installed)
- Python 3.8+
- Python virtual environment is recommended (`venv` or `conda`)
- Pseudopotential files for high-throughput DFT (The VASP terms of use do not allow redistributing, publishing, or sharing the POTCAR files)

During the installation, SAMBA checks the existence of the following Python modules:
- vasprocar [link](https://pypi.org/project/vasprocar/)
- pymatgen [link](https://pypi.org/project/pymatgen/)
- scipy [link](https://pypi.org/project/scipy/)
- numpy [link](https://pypi.org/project/numpy/)
- matplotlib [link](https://pypi.org/project/matplotlib/)
- plotly [link](https://pypi.org/project/plotly/)

</details>

<details>
<summary><strong>Run the code</strong></summary>
  
For run the code, the user must use the command below in the work directory.
```bash
python -m samba_ilum
```
or
```bash
python3 -m samba_ilum
```

When running the code, the following screen is shown to the user.

```text
=============================================================
SAMBA_ilum v1.0.0.510 Copyright (C) 2025 --------------------
Adalberto Fazzio's research group (Ilum|CNPEM)
Author: Augusto de Lelis Araujo -----------------------------
=============================================================
   _____ ___    __  _______  ___       _ __
  / ___//   |  /  |/  / __ )/   |     (_) /_  ______ ___
  \__ \/ /| | / /|_/ / __  / /| |    / / / / / / __ `___\
 ___/ / ___ |/ /  / / /_/ / ___ |   / / / /_/ / / / / / /
/____/_/  |_/_/  /_/_____/_/  |_|  /_/_/\__,_/_/ /_/ /_/
Simulation and Automated Methods for Bilayer Analysis v1.0.0.510

######################################################################
# What do you want to run? ===========================================
# ====================================================================
# [0] Generate SAMBA execution inputs
# --------------------------------------------------------------------
# [1] Heterostructure Generator
# [2] WorkFlow: High Throughput DFT (inputs + job)
# --------------------------------------------------------------------
# [3] Customize internal WorkFlow inputs (INPUTS folder)
######################################################################
```

- **Option [0]** provides the input files for the Bilayer Generator and the High-throughput DFT module, allowing the user to configure and customize the calculations to be performed.
- **Option [1]** runs the Bilayer Generator, where the selected monolayers are combined to generate bilayers for different twist angles.
- **Option [2]** runs the High-throughput DFT module, where the POSCAR files of the structures selected by the user (not limited to the bilayers obtained in option [1]) are analyzed in order to generate input files for different types of structural and electronic calculations using the VASP DFT package, along with the corresponding job submission script.
- **Option [4]** provides the default input files to be used with VASP, which the user can freely modify to further personalize or specialize the calculations according to their preferences.

The following sections provide a more detailed explanation of each option.

</details>

<details>
<summary><strong>Option [0]: Generate SAMBA execution inputs</strong></summary>

<p>This option generates the following input files for the SAMBA code:</p>
<ul>
  <li>SAMBA_HeteroStructure.input</li>
  <li>SAMBA_WorkFlow.input</li>
</ul>

<hr/>

<details>
<summary><strong>SAMBA_HeteroStructure.input</strong></summary>

<details>
<summary><strong>Sample file</strong></summary>

<pre><code>=============================================================
# SAMBA Copyright (C) 2025

#=========================================================================================================================
# Important notes !!! ====================================================================================================
#=========================================================================================================================
# Use only 2D lattices whose vectors (A1,A2) lie in the KxKy plane, and whose vector A3 lies in the z-axis direction -----
# A1 = (A1x, A1y, 0.0)  |  A2 = (A2x, A2y, 0.0)  |  A3 = (0.0, 0.0, A3z)
#-------------------------------------------------------------------------------------------------------------------------
# Use a 2D unit cell for each material, non-unit cells limit the number of structures generated, in addition to introducing
# "slowness" in the code execution ---------------------------------------------------------------------------------------
#=========================================================================================================================

#=========================================================================================================================
# Tuning parameters: =====================================================================================================
#=========================================================================================================================
dir_o = 'Structures'                   # Heterostructures Output Directory
dir_poscar = 'POSCAR'                  # Location directory of POSCAR files to be used

#=============================================================================================================
# Enable or Disable code execution in Loop: functional only to generate bilayers (n_Lattice = 2) =============
#=============================================================================================================
loop_ht = 0                            # [0] Disables; [1] Enables the loop, generating heterostructures for all combinations of
                                       #                                    POSCAR files contained in the "dir_poscar" directory
#===============================================================
# Parameters if the loop is Disabled ===========================
#===============================================================
if (loop_ht == 0):
   n_Lattice = 2                       # number of materials to be stacked, use 2 or 3.
   Lattice1  = 'C2.vasp'               # 1st Material "Substrate: Material initially kept fixed
   Lattice2  = 'hBN.vasp'              # 2nd Material "Material to be deposited on the Substrate"
   Lattice3  = 'SnTe.vasp'             # 3rd Material "Material to be deposited on the 2nd Material"

#===============================================================
# Other parameters =============================================
#===============================================================
separacao1 = 3.00                      # Separation distance (in Angs.) between the 1st and 2nd material.
separacao2 = 3.00                      # Separation distance (in Angs.) between the 2nd and 3rd material.
vacuum     = 15.0                      # Vacuum (in Angs.) to be introduced into the Heterostructure cell.
#----------------------------------
cell_fator = [10, 10]                  # Multiplication factor of the unit cell as a function of vectors A1, A2.
                                       # Note: Very high values ​​can lead to excessive code slowness.
#----------------------------------
crit_mod_vector  = 3                   # Percentage variation % of the module between the vectors (A and B) of the lattices: A1_with_A2 and B1_with_B2
crit_distorc_lattice = 3               # Percentage variation % of the module between the vectors (A and B) of the same lattice: A1_with_B1 and A2_with_B2
crit_angle_perc = 2                    # Percentage variation % of the angle formed between the vectors (A and B) of the lattices: Theta1_with_Theta2
crit_angle_diff = 2                    # Variation (in module) of the angle in degrees (º) formed between the vectors (A and B) of the lattices: Theta1_with_Theta2
crit_area = 5                          # Percentage variation % of the area of ​​the lattices that will make up the Heterostructure: Area1_with_Area2
#----------------------------------
ions_crit_i = 1                        # Criterion for the minimum number of atoms allowed in the Heterostructure.
ions_crit_f = 100                      # Criterion for the maximum number of atoms allowed in the Heterostructure.
                                       # Note: When looping many structures, I advise sweeping small ranges of ions for example: (1, 10); (10, 20); (50,60)
#----------------------------------
                                       # By default we will always have: angle > 0.0 and angle < 180.0
angle_min = 15.0                       # Minimum opening angle between vectors A1 and A2
angle_max = 165.0                      # Maximum opening angle between vectors A1 and A2
#----------------------------------
mismatch_type = 0                      # Applied deformation: [0] Distributed proportionally among the materials
                                       #                      [1], [2] or [3] keeps the 1st, 2nd or 3rd material fixed, deforming the others.
#----------------------------------    
rot_angle_calc = 'center_cell'         # 'center_cell', 'A1' or 'A2': Vector with respect to which the rotation angle between the materials is calculated  
#----------------------------------</code></pre>

</details>

</details>

<hr/>

<details>
<summary><strong>SAMBA_WorkFlow.input</strong></summary>

<details>
<summary><strong>Sample file</strong></summary>

<pre><code># SAMBA Copyright (C) 2025


#=======================================================
# Python virtual environment directory -----------------
dir_virtual_python = '/home/dlelis/codes/python_virtual'
#=======================================================
# Workflow Output Directory ----------------------------
dir_o = 'WorkFlow_output'
#=======================================================
# information to be added to the database --------------
replace_type_pseudo = 'PAW_PBE'; replace_type_XC = 'GGA'
#=======================================================


#=======================================================
type_lattice = 2                            # [1] 1D lattices (Periodic in X);   [2] 2D lattices (Periodic in XY);   [3] 3D lattices - Bulk
#=======================================================
tasks = ['relax', 'scf', 'bands', 'dos']    # tasks = ['z-scan', 'xy-scan', 'relax', 'scf', 'bands', 'dos', 'bader']
type  = ['sem_SO','com_SO']                 # type  = ['sem_SO','com_SO']
#=======================================================
ispin = 2                 # [1] for non-spin-polarized calculation; [2] for spin-polarized calculation
#=======================================================
dipol = 'none'            # Use the options:  'none',  'center_cell'  or  'center_mass'
#=======================================================
magnet_mode = 'default'   # Use the options:  'default',  'MAGMOM=0'  or  'NUPDOWN=0'
#=======================================================
U_correction = 0          # Hubbard Correction (U): [0] to disable, [1] to enable
#=======================================================
vdW = 0               # Van der Waals correction used:  [0] disables van der Waals correction.
                      # Correction applied to all calculations (with and without OS)
#-------------------------------------------------------
vdWDF = 'none'        # Non-local functional vdW_DF used: 'none' disables the non-local functional vdW_DF.
                      # Choice: 'none', 'DF', 'DF2', 'optPBE', 'optB88', 'optB86b', 'rev-DF2', 'DF-cx', 'DF3-opt1', 'DF3-opt2', 'rVV10', 'SCAN+rVV10', 'r2SCAN+rVV10', 'PBE+rVV10L'
                      # Note:  Functional applied only in structural optimization calculations ('xyz-scan', 'xy-scan', 'z-scan', 'a-scan', 'relax')
                      # Note:  vdW != 0 will override any choice of vdWDF
#=======================================================
ENCUT_min = 500       # Minimum value for cut-off energy in eV
                      # Note:  If (ENCUT_min < ENCUT*encut_factor), then ENCUT_min = ENCUT*encut_factor
                      #            ENCUT refers to the highest cutting energy value present in the POTCAR file
fator_encut = 1.3     # Multiplication factor for the criterion of the cutting energy used
#=======================================================
type_k_dens  = 1      # [1] KPOINTS (Monkhorst-Pack);   [2] KPOINTS (Gamma);   [3] INCAR (KSPACING Monkhorst-Pack);   [4] INCAR (KSPACING Gamma)
k_dens_relax = 12     # Relaxation calculation:             number of k-points per Å^-1
k_dens_scf   = 12     # Self-consistent calculation (scf):  number of k-points per Å^-1
k_dens_dos   = 12     # DOS Calculation:                    number of k-points per Å^-1
k_dens_bader = 12     # Bader Charge Calculation:           number of k-points perr Å^-1
n_kpoints    = 50     # Band calculation (nscf):            number of k-points in each section of the band plot
nions_split  = 100    # number of ions in the POSCAR file, so that the band calculation is performed in steps (split)
vacuo        = 15.0   # Vacuum applied to Heterostructure
NCORE        = 8      # Number of "cores" per "node"


#============================
# a-scan parameters =========
# Functional for 3D bulk ====
#============================
k_dens_a_scan = 6       # a-scan calculation: number of k-points per Å-1
factor_var    = 5       # % variation of the lattice parameter (modulo the smallest lattice vector)


#============================
# z-scan parameters =========
#============================
k_dens_z_scan = 6        # z-scan calculation: number of k-points per Å-1


#============================
# xy-scan parameters ========
#============================
k_dens_xy_scan = 6                                                                    # xy-scan calculation: number of k-points per Å-1
r_displacement_A1 = [0.0, (1/8), (1/6), (1/4), (1/3), (1/2), (2/3), (3/4), (5/6)]     # Displacements in the direction of vector A1 (2nd material)
r_displacement_A2 = [0.0, (1/8), (1/6), (1/4), (1/3), (1/2), (2/3), (3/4), (5/6)]     # Displacements in the direction of vector A2 (2nd material)


#============================
# xyz-scan parameters =======
#============================
k_dens_xyz_scan = 6                                       # xyz-scan calculation: number of k-points Å-1
displacement_Z = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]      # Vertical separation (z-axis) between layers
displacement_xyz_A1 = [0.0, 0.2, 0.4, 0.6, 0.8]           # Displacements in the direction of vector A1 (2nd material)
displacement_xyz_A2 = [0.0, 0.2, 0.4, 0.6, 0.8]           # Displacements in the direction of vector A2 (2nd material)</code></pre>

</details>
  
</details>

-----------------------------------------------

</details>
































<details>
<summary><strong>Arquivos Estruturais</strong></summary>

### Formatos Suportados
O código utiliza arquivos no formato `POSCAR` (usado pelo VASP) ou `.xyz` para ler as coordenadas atômicas iniciais. A estrutura do arquivo deve seguir o padrão convencional.

**Exemplo de estrutura de diretório:**

</details>




<details>
<summary><strong>Exemplo 01</strong></summary>

### Formatos Suportados
O código utiliza arquivos no formato `POSCAR` (usado pelo VASP) ou `.xyz` para ler as coordenadas atômicas iniciais. A estrutura do arquivo deve seguir o padrão convencional.

**Exemplo de estrutura de diretório:**

</details>






<details>
<summary><strong>Exemplo 02</strong></summary>

### Formatos Suportados
O código utiliza arquivos no formato `POSCAR` (usado pelo VASP) ou `.xyz` para ler as coordenadas atômicas iniciais. A estrutura do arquivo deve seguir o padrão convencional.

**Exemplo de estrutura de diretório:**

</details>
