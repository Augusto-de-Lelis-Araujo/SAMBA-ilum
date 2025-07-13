<h1>SAMBA (Simulation and Automated Methods for Bilayer Analysis)
  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3">
  </a>
</h1>

<h2>Article available in soon</h2>

<details>
  <summary><strong>🔵 Description</strong></summary>
  <p>SAMBA is an open-source Python 3 code capable of:</p>
  <ul>
    <li>Automating the generation of twisted homo- and heterobilayers using the coincidence lattice method, ensuring low lattice mismatch and a wide variety of twist angles.</li>
    <li>Automating DFT calculations via the VASP code in a high-throughput approach, including the creation of input files for different types of DFT calculations, along with a customized execution job.</li>
    <li>Analyzing and extracting results, producing high-quality plots (via the VASProcar code) of various structural and electronic properties, as well as storing the data in JSON files.</li>
  </ul>
  <img src="etc/figures/logo.png" alt="SAMBA logo">
</details>

<details>
  <summary><strong>Authors</strong></summary>
  <ul>
    <li>Augusto de Lelis Araújo (<a href="https://orcid.org/0000-0002-6835-6113">ORCID</a>)</li>
    <li>Adalberto Fazzio (<a href="https://orcid.org/0000-0001-5384-7676">ORCID</a>)</li>
    <li>Felipe Castro de Lima (<a href="https://orcid.org/0000-0002-2937-2620">ORCID</a>)</li>
    <li>Pedro Henrique Sophia (<a href="https://orcid.org/0009-0007-5428-0596">ORCID</a>)</li>
  </ul>
</details>

<details>
  <summary><strong>Meet Institutional and Research Network:</strong></summary>
  <ul>
    <li>Ilum - School of Science <a href="https://ilum.cnpem.br/en/">link</a></li>
    <li>CNPEM - The Brazilian Center for Research in Energy and Materials <a href="https://cnpem.br/en/">link</a></li>
    <li>INCT - Materials Informatics <a href="https://inct-mi.pesquisa.ufabc.edu.br/">link</a></li>
    <li>midb.cloud database <a href="https://midb.cloud/">link</a></li>
  </ul>
  <img src="etc/figures/institucional.png" alt="Institutional Network">
</details>

<hr/>

<h2>Tutorial</h2>
<p>Click on the topics below to expand and see the details for each section.</p>

<details>
  <summary><strong>Installation</strong></summary>
  <p>The latest version of SAMBA code can be installed using the Python Package Index via the <strong>command below</strong>, while the source code is available for download via the <a href="https://pypi.org/project/SAMBA-ilum/">link</a>.</p>
  <pre><code>pip install samba_ilum</code></pre>

  <p><strong>Requirements:</strong> Make sure you have the following requirements:</p>
  <ul>
    <li>Linux or Windows environment for bilayer generation</li>
    <li>Linux environment for high-throughput DFT (requires VASPkit installed)</li>
    <li>Python 3.8+</li>
    <li>Python virtual environment is recommended (venv or conda)</li>
    <li>Pseudopotential files for high-throughput DFT (The VASP terms of use do not allow redistributing, publishing, or sharing the POTCAR files)</li>
  </ul>

  <p>During the installation, SAMBA checks the existence of the following Python modules:</p>
  <ul>
    <li><a href="https://pypi.org/project/vasprocar/">vasprocar</a></li>
    <li><a href="https://pypi.org/project/pymatgen/">pymatgen</a></li>
    <li><a href="https://pypi.org/project/scipy/">scipy</a></li>
    <li><a href="https://pypi.org/project/numpy/">numpy</a></li>
    <li><a href="https://pypi.org/project/matplotlib/">matplotlib</a></li>
    <li><a href="https://pypi.org/project/plotly/">plotly</a></li>
  </ul>
</details>

<details>
  <summary><strong>Run the code</strong></summary>
  <p>To run the code, the user must use the command below in the working directory:</p>
  <pre><code>python -m samba_ilum</code></pre>
  <p>or</p>
  <pre><code>python3 -m samba_ilum</code></pre>

  <p>When running the code, the following screen is shown to the user:</p>
  <pre><code>=============================================================
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
######################################################################</code></pre>

  <ul>
    <li><strong>Option [0]</strong>: provides the input files for the Bilayer Generator and the High-throughput DFT module, allowing the user to configure and customize the calculations to be performed.</li>
    <li><strong>Option [1]</strong>: runs the Bilayer Generator, where the selected monolayers are combined to generate bilayers for different twist angles.</li>
    <li><strong>Option [2]</strong>: runs the High-throughput DFT module, where the POSCAR files of the structures selected by the user (not limited to the bilayers obtained in option [1]) are analyzed in order to generate input files for different types of structural and electronic calculations using the VASP DFT package, along with the corresponding job submission script.</li>
    <li><strong>Option [3]</strong>: provides the default input files to be used with VASP, which the user can freely modify to further personalize or specialize the calculations according to their preferences.</li>
  </ul>
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
separation_1 = 3.00                    # Separation distance (in Angs.) between the 1st and 2nd material.
separation_2 = 3.00                    # Separation distance (in Angs.) between the 2nd and 3rd material.
vacuum       = 15.0                    # Vacuum (in Angs.) to be introduced into the Heterostructure cell.
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

Por meio deste arquivo de input, o usuário controla os detalhes referentes a geração de bicamadas para diferentes ângulos de Twisted, onde:

- **dir_poscar** refere-se ao nome do diretório contendo os arquivos POSCAR das monolayers a serem utilizadas na geração das bicamadas;
- **dir_o** é o nome do diretório a ser criado pelo código, e onde serão armazenado os arquivos estruturais das bicamadas geradas;
- **loop_ht** define como os arquivos POSCAR serão utilizados para a geração das bicamadas, onde:
  
  Para **loop_ht=0**, o usuário deve informar em **Lattice1** e **Lattice2**, o nome dos arquivos POSCAR das camadas inferior e superior do empilhamento, respectivamente. Neste caso, somente a bicamada entre estes dois materiais selecionados é criada;

  Para **loop_ht=1**, o código irá operar em loop, criando bicamadas, referente a combinação par a par, de todos os arquivos estruturais contidos no diretório definido por **dir_poscar**;
  
- **separation_1** refere-se a distância de separação vertical (em Å) entre as monolayers no empilhamento;
- **vacuum** refere-se a separação vertical (em Å) entre imagens periódicas da célula ao longo do eixo-z (devido a condição de contorno periódica do cálculo de DFT), usualmente são utilizados valores acima de 10Å;
- **cell_fator** refere-se ao fator de multiplicação dos vetores A1 e A2 das células presentes em **dir_poscar**, para criação das respectivas supercélulas;
- **crit_mod_vector** Define a tolerância percentual (%) na comparação dos módulos dos vetores de rede A e B entre duas redes diferentes (A1 com A2 e B1 com B2). Serve para verificar se as duas redes têm tamanhos de vetores semelhantes;
- **crit_distorc_lattice** Define a tolerância percentual (%) para a diferença entre os vetores A e B de uma mesma rede (A1 com B1 e A2 com B2). Esse valor mede quanto a rede está distorcida (quanto foge de uma rede quadrada ou hexagonal ideal, por exemplo);
- **crit_angle_perc** Define a tolerância percentual (%) na variação do ângulo formado entre os vetores de rede, entre as duas redes;
- **crit_angle_diff** Define a tolerância absoluta (em graus º) da diferença angular, entre as duas redes. É uma critério complementar ao **crit_angle_perc**;
- **crit_area** Define a tolerância percentual (%) na diferença de área, entre as duas redes;
- **ions_crit_i e ions_crit_f** Limites inferior e superior para o número de átomos das estruturas geradas. Esses critérios permitem a obtenção de heteroestruturas com dimensões desejadas, além de evitar problemas computacionais;
- **angle_min e angle_max** Limites inferior e superior para o ângulo de abertura das estruturas geradas. Esses critérios evitam casos em que as redes se alinham de forma quase paralela (0° ou 180°), levando a células muito alongadas, gerando sistemas não fisicamente interessante ou podendo levar a erros numéricos;
- **mismatch_type** Esse parâmetro define como o lattice mismatch será resolvida: quem será deformado, e quem permanecerá com sua rede original, onde:

  **mismatch_type=0** a distorção estrutural é distribuida uniformemente entre os materiais do empilhamento.
  
  **mismatch_type=1** a distorção estrutural é aplicada sobre a monocamada inferior do empilhamento.
  
  **mismatch_type=2** a distorção estrutural é aplicada sobre a monocamada superior do empilhamento.
  
- **rot_angle_calc** Define a referência geométrica usada para medir o ângulo de rotação entre as camadas;
  
  **rot_angle_calc='center_cell'** defino o ângulo necessário para alinhar o vetor central (conectando a origem ao centro da células) de ambas as células.
  
  **rot_angle_calc='A1'** defino o ângulo necessário para alinhar o vetor A1 de ambas as células.
  
  **rot_angle_calc='A2'** defino o ângulo necessário para alinhar o vetor A2 de ambas as células.
  
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
k_dens_bader = 12     # Bader Charge Calculation:           number of k-points per Å^-1
n_kpoints    = 50     # Band calculation (nscf):            number of k-points in each section of the band plot
nions_split  = 100    # number of ions in the POSCAR file, so that the band calculation is performed in steps (split)
vacuum       = 15.0   # Vacuum applied to Heterostructure
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

Por meio deste arquivo de input, o usuário controla os detalhes cálculos de DFT a serem realizados em abordagem high-throughput, onde:

- **dir_virtual_python**
- **dir_o**
- **type_lattice**
- **tasks**
- **type**
- **ispin**
- **dipol**
- **magnet_mode**
- **U_correction**
- **vdW**
- **vdWDF**
- **ENCUT_min**
- **fator_encut**
- **type_k_dens**
- **k_dens_relax**
- **k_dens_scf**
- **k_dens_dos**
- **k_dens_bader**
- **n_kpoints**
- **nions_split**
- **vacuum**
- **NCORE**
- **k_dens_a_scan**
- **factor_var**
- **k_dens_z_scan**
- **k_dens_xy_scan**
- **r_displacement_A1**
- **r_displacement_A2**
- **k_dens_xyz_scan**
- **displacement_Z**
- **displacement_xyz_A1**
- **displacement_xyz_A2**
  
</details>

-----------------------------------------------

</details>

<details>
<summary><strong>Option [1]: running the Bilayer Generator</strong></summary>
</details>

<details>
<summary><strong>Option [2]: running the High-throughput DFT</strong></summary>
</details>

<details>
<summary><strong>Option [3]: Customizing DFT Calculation Inputs</strong></summary>
</details>

-----------------------------------------------

<img src="etc/figures/institucional.png" alt="Institutional Network">
