<h1>SAMBA (Simulation and Automated Methods for Bilayer Analysis)
  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3">
  </a>
</h1>

<h2>Article available in soon</h2>




<details>
  <summary><strong>Description</strong></summary>
  
  ------------------------------------
  
  <p>SAMBA is an open-source Python 3 code capable of:</p>
  <ul>
    <li>Automating the generation of twisted homo- and heterobilayers using the coincidence lattice method, ensuring low lattice mismatch and a wide variety of twist angles.</li>
    <li>Automating DFT calculations via the VASP code in a high-throughput approach, including the creation of input files for different types of DFT calculations, along with a customized execution job.</li>
    <li>Analyzing and extracting results, producing high-quality plots (via the VASProcar code) of various structural and electronic properties, as well as storing the data in JSON files.</li>
  </ul>
  <img src="etc/figures/logo.png" alt="SAMBA logo">
  
  ------------------------------------
</details>




<details>
  <summary><strong>Authors</strong></summary>

  ------------------------------------
  
  <ul>
    <li>Augusto de Lelis Araújo (<a href="https://orcid.org/0000-0002-6835-6113">ORCID</a>)</li>
    <li>Adalberto Fazzio (<a href="https://orcid.org/0000-0001-5384-7676">ORCID</a>)</li>
    <li>Felipe Castro de Lima (<a href="https://orcid.org/0000-0002-2937-2620">ORCID</a>)</li>
    <li>Pedro Henrique Sophia (<a href="https://orcid.org/0009-0007-5428-0596">ORCID</a>)</li>
  </ul>

  ------------------------------------
</details>




<details>
  <summary><strong>Meet Institutional and Research Network:</strong></summary>

  ------------------------------------
  
  <ul>
    <li>Ilum - School of Science <a href="https://ilum.cnpem.br/en/">link</a></li>
    <li>CNPEM - The Brazilian Center for Research in Energy and Materials <a href="https://cnpem.br/en/">link</a></li>
    <li>INCT - Materials Informatics <a href="https://inct-mi.pesquisa.ufabc.edu.br/">link</a></li>
    <li>midb.cloud database <a href="https://midb.cloud/">link</a></li>
    <li>Ilum - School of Science <a href="https://ilum.cnpem.br/en/" target="_blank">link</a></li>
  </ul>
  <img src="etc/figures/institucional.png" alt="Institutional Network"> 

  ------------------------------------
</details>




<h2>Tutorial</h2>
<p>Click on the topics below to expand and see the details for each section.</p>




<details>
  <summary><strong>Installation</strong></summary>

  ------------------------------------
  
  <p>The latest version of SAMBA code can be installed using the Python Package Index via the <strong>command below</strong>, while the source code is available for download via the <a href="https://pypi.org/project/SAMBA-ilum/">link</a>.</p>
  <pre><code>pip install samba_ilum</code></pre>

  ------------------------------------

  <p><strong>Requirements:</strong> Make sure you have the following requirements:</p>
  <ul>
    <li>Linux or Windows environment for bilayer generation</li>
    <li>Linux environment for high-throughput DFT (requires VASPKIT installed <a href="https://vaspkit.com/installation.html" target="_blank">link</a>)</li>
    <li>Python 3.8+</li>
    <li>Python virtual environment is recommended (venv or conda)</li>
    <li>Pseudopotential files for high-throughput DFT (The VASP terms of use do not allow redistributing, publishing, or sharing the POTCAR files)</li>
  </ul>

  ------------------------------------

  <p>During the installation, SAMBA checks the existence of the following Python modules:</p>
  <ul>
    <li>VASProcar <a href="https://pypi.org/project/vasprocar/">link</a></li>
    <li>pymatgen <a href="https://pypi.org/project/pymatgen/">link</a></li>
    <li>SciPy <a href="https://pypi.org/project/scipy/">link</a></li>
    <li>NumPy <a href="https://pypi.org/project/numpy/">link</a></li>
    <li>Matplotlib <a href="https://pypi.org/project/matplotlib/">link</a></li>
    <li>Plotly <a href="https://pypi.org/project/plotly/">link</a></li> 
  </ul>

------------------------------------
</details>



<details>
  <summary><strong>Run the code</strong></summary>

  ------------------------------------
  
  <p>To run the code, the user must use the command below in the working directory:</p>
  <pre><code>python -m samba_ilum</code></pre>
  <p>or</p>
  <pre><code>python3 -m samba_ilum</code></pre>

  ------------------------------------

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

------------------------------------
</details>




<details>
<summary><strong>Generating bilayers</strong></summary>

------------------------------------

<details>
  <summary><strong>1st step): Create a working directory and, inside it, create a folder where you will place the POSCAR files of the monolayers to be used for bilayer generation</strong></summary>

  **Note:** Both the name of the folder containing the POSCAR files and the labels of these files are freely chosen by the user.

  **Note:** The POSCAR files for bilayer generation must follow the following criteria (compare the criteria with the model in POSCAR file - example):

  <details>
    <summary><strong>POSCAR file - example</strong></summary>

    <pre><code>SAMBA Pt4Se6Hg2_75eb2b2b9759445a 
1.0 
 7.419406617232910 0.00000000000000 0.0 
-3.709703308616455 6.42539461153006 0.0 
 0.0000000 0.0000000 18.526402379698077 
Pt Se Hg  
4 6 2  
Direct 
0.0 0.5 0.5 
0.0 0.0 0.5 
0.5 0.5 0.5 
0.5 0.0 0.5 
0.3363234295508661 0.1681617147754295 0.5707808825560079 
0.8318382852245705 0.6636765704491339 0.5707808825560079 
0.8318382852245705 0.1681617147754295 0.5707808825560079 
0.1681617147754295 0.8318382852245705 0.4292191174439921 
0.1681617147754295 0.3363234295508661 0.4292191174439921 
0.6636765704491339 0.8318382852245705 0.4292191174439921 
0.3333333333333357 0.6666666666666643 0.5951699375852613 
0.6666666666666643 0.3333333333333357 0.4048300624147387</code></pre>  

  </details>

  <details>
    <summary><strong>Criteria for the POSCAR file</strong></summary>

    - Devem estar inseridos dentro da pasta definida por **dir_poscar**;
    - Devem corresponder a redes 2D cujos vetores (A1,A2) estejam no plano KxKy, enquanto o vetor A3 deve estar no eixo-z;
    - Devem ser escritos em coordenadas diretas;

    - **Opcional:** O usuário pode inserir um identificador (**ID**) para associar cada bicamada gerada à sua respectiva monocamada de origem. Para isso, basta incluir o ID na primeira linha do arquivo POSCAR, logo após a palavra SAMBA. O código interpreta como ID a última string presente nessa linha inicial;

    - **Opcional:** É recomendável utilizar **células unitárias**, uma vez que o uso de **supercélulas** pode ocultar possíveis configurações e tornar a execução do código mais lenta. Durante a execução, o SAMBA verifica se as células na pasta definida por dir_poscar são unitárias ou não, e perguntará ao usuário se deseja continuar o cálculo mesmo assim;

    - **Observação:** Para garantir a correta obtenção dos diferentes ângulos de twisted, a célula deve ser construída de modo que o **eixo de menor rotação em torno do eixo z** esteja posicionado na **origem da célula**. Caso o código identifique que esse eixo está fora da origem, ele irá automaticamente transladar os íons para corrigir essa posição. A célula original será preservada no diretório "**POSCAR_original**".

  </details>

  - **2nd step:** In the working directory, run the SAMBA code and choose **option [0]** to create the input file **SAMBA_HeteroStructure.input**.

  - **2nd step**: Edit the input file **SAMBA_HeteroStructure.input**, specifying the details of the bilayers to be generated using the tags described below.

  <details>
    <summary><strong>SAMBA_HeteroStructure.input (Sample file)</strong></summary>

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
crit_distorc_lattice = 3              # Percentage variation % of the module between the vectors (A and B) of the same lattice: A1_with_B1 and A2_with_B2
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

  <details>
    <summary><strong>SAMBA_HeteroStructure.input (description and adjustments)</strong></summary>

    Por meio deste arquivo de input, o usuário controla os detalhes referentes a geração de bicamadas para diferentes ângulos de Twisted, onde:

    - **dir_poscar** define o nome do diretório contendo os arquivos POSCAR das monolayers a serem utilizadas na geração das bicamadas;
    - **dir_o** define o nome do diretório a ser criado pelo código, e onde serão armazenado os arquivos estruturais das bicamadas geradas;
    - **loop_ht** define como os arquivos POSCAR serão utilizados para a geração das bicamadas, onde:

      Para **loop_ht=0**, o usuário deve informar em **Lattice1** e **Lattice2**, o nome dos arquivos POSCAR das camadas inferior e superior do empilhamento, respectivamente. Neste caso, somente a bicamada entre estes dois materiais selecionados é criada;

      Para **loop_ht=1**, o código irá operar em loop, criando bicamadas, referente a combinação par a par, de todos os arquivos estruturais contidos no diretório definido por **dir_poscar**;

    - **separation_1** define a distância de separação vertical (em Å) entre as monolayers no empilhamento;
    - **vacuum** define a separação vertical (em Å) entre imagens periódicas da célula ao longo do eixo-z (devido a condição de contorno periódica do cálculo de DFT), usualmente são utilizados valores acima de 10Å;
    - **cell_fator** define o fator de multiplicação dos vetores A1 e A2 das células presentes em **dir_poscar**, para criação das respectivas supercélulas;
    - **crit_mod_vector** define a tolerância percentual (%) na comparação dos módulos dos vetores de rede A e B entre duas redes diferentes (A1 com A2 e B1 com B2). Serve para verificar se as duas redes têm tamanhos de vetores semelhantes;
    - **crit_distorc_lattice** define a tolerância percentual (%) para a diferença entre os vetores A e B de uma mesma rede (A1 com B1 e A2 com B2). Esse valor mede quanto a rede está distorcida (quanto foge de uma rede quadrada ou hexagonal ideal, por exemplo);
    - **crit_angle_perc** define a tolerância percentual (%) na variação do ângulo formado entre os vetores de rede, entre as duas redes;
    - **crit_angle_diff** define a tolerância absoluta (em graus º) da diferença angular, entre as duas redes. É uma critério complementar ao **crit_angle_perc**;
    - **crit_area** define a tolerância percentual (%) na diferença de área, entre as duas redes;
    - **ions_crit_i e ions_crit_f** definem os limites inferior e superior para o número de átomos das estruturas geradas. Esses critérios permitem a obtenção de heteroestruturas com dimensões desejadas, além de evitar problemas computacionais;
    - **angle_min e angle_max** definem os limites inferior e superior para o ângulo de abertura das estruturas geradas. Esses critérios evitam casos em que as redes se alinham de forma quase paralela (0° ou 180°), levando a células muito alongadas, gerando sistemas não fisicamente interessante ou podendo levar a erros numéricos;
    - **mismatch_type**  define como o lattice mismatch será resolvido: qual material será deformado, e qual permanecerá sem deformação, onde:

      **mismatch_type=0** distribui uniformemente a distorção estrutural entre os materiais do empilhamento;

      **mismatch_type=1** aplica a distorção estrutural sobre a monocamada inferior do empilhamento;

      **mismatch_type=2** aplica a distorção estrutural sobre a monocamada superior do empilhamento;

    - **rot_angle_calc** define a referência geométrica usada para medir o ângulo de rotação entre as camadas, onde:

      **rot_angle_calc='center_cell'** define o ângulo necessário para alinhar o vetor central (conectando a origem ao centro da células) de ambas as células;

      **rot_angle_calc='A1'** define o ângulo necessário para alinhar o vetor A1 de ambas as células;

      **rot_angle_calc='A2'** define o ângulo necessário para alinhar o vetor A2 de ambas as células.

  </details>

</details>
















<details>
<summary><strong>Option [2]: running the High-throughput DFT</strong></summary>

------------------------------------

<details>
<summary><strong>SAMBA_WorkFlow.input (Sample file)</strong></summary>

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
                      # Choice: 'none', 'DF', 'DF2', 'optPBE', 'optB88', 'optB86b', 'rev-DF2', 'DF-cx', 'DF3-opt1', 'DF3-opt2'
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

------------------------------------
</details>

<details>
<summary><strong>SAMBA_WorkFlow.input (description and adjustments)</strong></summary>

Por meio deste arquivo de input, o usuário controla os detalhes cálculos de DFT a serem realizados em abordagem high-throughput, onde:

- **dir_virtual_python** define o caminho onde o ambiente virtual python esta localizado;
- **dir_o** define o nome do diretório de saída (a ser criado pelo código), onde os arquivos de input do cálculo high-throughput DFT serão gerados;
- **replace_type_pseudo** e **replace_type_XC** são informações do cálculo de DFT a serem inseridos nos arquivos .json;
- **type_lattice** define o tipo de rede a ser analisada, onde:
  
  **type_lattice=1** define que as estruturas analisadas são redes 1D (periódicas em X);
  
  **type_lattice=2** define que as estruturas analisadas são redes 2D (periódicas em XY);
  
  **type_lattice=3** define que as estruturas analisadas são redes 3D (materiais bulk);s
- **tasks** define todos os diferentes cálculos de DFT a serem realizados na abordagem high-throughput, para todas as estruturas presentes no diretório "Structures";
- **type** define se os cálculos em **tasks** incluirão o acoplamento spin-órbita (SOC), onde:

  **type=['sem_SO','com_SO']** define que todos os cálculos são realizados desconsiderando o SOC;
  
  **type=['com_SO']** define que o SOC é incluído nos cálculos;
  
  **type=['sem_SO','com_SO']** define que todos os cálculos são realizados, tanto "com" quanto "sem" SOC;
- **ispin** define a polarização de spin do cálculo, onde:

  **ispin=1**: non-spin-polarized calculations are performed (for calculations without SOC);
  
  **ispin=2**: spin-polarized calculations (collinear) are performed (for calculations without SOC);
- **dipol** define se a correção de dipolo é incluida ou não nos cálculos, onde:
  
  **dipol='none'** desativa a correção de dipolo;
  
  **dipol='center_cell'** ativa a correção de dipolo; definindo o centro da célula como a região em relação ao qual o momento de dipolo total na célula é calculado;
  
  **dipol='center_mass'** ativa a correção de dipolo; definindo o centro de massa da célula como a região em relação ao qual o momento de dipolo total na célula é calculado;
- **magnet_mode** define como a magnetização é cálculada para cálculos não-colineares ou com polarização de spin ativada, onde:
  
  **magnet_mode='default'** define o padrão do VASP onde a tag MAGMOM é definida como número_de_ions&#42;1.0 para ISPIN=2 "cálculo com polarização de spin", ou 3&#42;número_de_ions&#42;1.0 "cálculo com SOC";
  
  **magnet_mode='MAGMOM=0'** define os momentos magnéticos iniciais dos ions da rede como zero, onde a tag MAGMOM é definida como número_de_ions**x**0 para ISPIN=2 "cálculo com polarização de spin", ou 3**x**número_de_ions**x**0 "cálculo com SOC";
  
  **magnet_mode='NUPDOWN=0'** define a diferença entre o número de elétrons nos componentes de spin para cima e para baixo, como sendo zero no cálculo;
- **U_correction**: Ativa ou desativa a correção de Hubbard, para metais de transição com elétrons 3d/4d/5d ou Lantanídeos/actinídeos com elétrons com elétrons 4f/5f, onde:

  **U_correction=0** (no correction);
  
  **U_correction=1** ativa a correção, aplicado aos seguintes ions (Cr, Mn, Fe, Co, Ni, Cu, La, Ce, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, U). **Vide ??? caso deseje ajustar os valores da correção U aplicados para cada ion**.
  
- **vdW** specifies a vdW dispersion term of the atom-pairwise or many-body type, where:

  **vdW=0** (no correction);
  
  **vdW=integer>0** define o método utilizado para a correção de dispersão adicionada à energia total, às forças atômicas e ao tensor de tensão. Para consultar os diferentes métodos implementados no VASP, consulte o <a href="https://www.vasp.at/wiki/index.php/IVDW" target="_blank">link</a>;
- **vdWDF** defines the semilocal exchange-correlation functional for vdW correction, where:

  **vdWDF='none'** (no correction);
  
  Para ativar a correção, escolha um dos seguintes funcionais semilocal de troca-correlação ('DF', 'DF2', 'optPBE', 'optB88', 'optB86b', 'rev-DF2', 'DF-cx', 'DF3-opt1', 'DF3-opt2'), para mais detalhes a respeito de cada funcional consulte o <a href="https://www.vasp.at/wiki/index.php/Nonlocal_vdW-DF_functionals" target="_blank">link</a>;
- **ENCUT_min** Valor minimo para a energia de corte (em eV) utilizado para a expansão em ondas planas da função de onda;
- **fator_encut** Fator de multiplicação aplicado a energia de corte;
  
  **Note:**  If (ENCUT_min < ENCUT*fator_encut), then ENCUT_min = ENCUT*encut_factor, where ENCUT refers to the highest cutting energy value present in the POTCAR file;
- **type_k_dens** define o método utilizado para os vetores de Bloch (pontos-k) usados para amostrar a zona de Brillouin em cálculos auto-consistentes (scf), escolha entre (para mais detalhes consulte o <a href="[https://www.vasp.at/wiki/index.php/Nonlocal_vdW-DF_functionals](https://www.vasp.at/wiki/index.php/KPOINTS)" target="_blank">link</a>):

  **type_k_dens=1** para utilizar Monkhorst-Pack;
  
  **type_k_dens=1** para utilizar Gamma;
  
  **type_k_dens=1** para utilizar KSPACING Monkhorst-Pack;
  
  **type_k_dens=1** para utilizar KSPACING Gamma;
  
- **k_dens_relax** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1 e A2), para amostrar a zona de Brillouin no cálculo de relaxação estrutural;
- **k_dens_scf** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1 e A2), para amostrar a zona de Brillouin no cálculo da densidade de carga;
- **k_dens_dos** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1 e A2), para amostrar a zona de Brillouin no cálculo da densidade de estados;
- **k_dens_bader** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1 e A2), para amostrar a zona de Brillouin nos cálculos de densidade de carga para obtenção da carga de Bader;
- **n_kpoints** define o número de ponto-k para cada linha de alta-simetria (intervalo de pontos-k) no cálculo da estrutura de bandas;
- **nions_split** define o núemro de átomos minimo na estrutura, para que o cálculo da estrutura de bandas seja segmentado/splitado em diferentes cálculos, cada um referente a uma determinada linha de alta-simetria (intervalo de pontos-k) definido no arquivo KPOINTS;

  **Observação:** Este método é utili para o cálculo da estrutura de bandas em sistemas muito grandes (grande número de ions) onde o poder computacional disponível é limitado.
- **vacuum** define a separação vertical (em Å) entre imagens periódicas da célula ao longo do eixo-z (devido a condição de contorno periódica do cálculo de DFT), usualmente são utilizados valores acima de 10 Å;
- **NCORE** define o número of "cores" por "node", utilizado pelo VASP para processar as bandas em paralelo.
- **k_dens_a_scan** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1, A2 e A3), para amostrar a zona de Brillouin no cálculo a-scan (a-scan é uma varredura pelo parâmetro de rede "a" ideal, indicado para sistemas bulk 3D);
- **factor_var** define a variação percentual (%) máxima em relação ao parâmetro de rede inicial, co cálculo a-scan;
- **k_dens_z_scan** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1, A2), para amostrar a zona de Brillouin no cálculo z-scan;
- **k_dens_xy_scan** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1, A2), para amostrar a zona de Brillouin no cálculo xy-scan;
- **r_displacement_A1** define a componente do deslocamento lateral (em relação ao vetor de rede A1) efetuado sobre a camada superior do empilhamento, no cálculo xy-scan;
- **r_displacement_A2** define a componente do deslocamento lateral (em relação ao vetor de rede A2) efetuado sobre a camada superior do empilhamento, no cálculo xy-scan;
- **k_dens_xyz_scan** define o número de pontos-k por Å^-1 (em relação a direção definida pelo vetores A1 e A2), para amostrar a zona de Brillouin no cálculo xyz-scan (xyz-scan é uma combinação dos cálculos z_scan e xy_scan em um único processo);
- **displacement_Z** define os valores de separação vertical iniciais entre as camadas do empilhamento, no cálculo xyz-scan;
- **displacement_xyz_A1** define a componente do deslocamento lateral (em relação ao vetor de rede A1) efetuado sobre a camada superior do empilhamento, no cálculo xyz-scan;
- **displacement_xyz_A2** define a componente do deslocamento lateral (em relação ao vetor de rede A2) efetuado sobre a camada superior do empilhamento, no cálculo xyz-scan;
  
</details>

<details>
  <summary><strong>Structure of files and directories for code execution</strong></summary>


  <details>
  <summary><strong>pseudo files (example)</strong></summary>

  <pre><code>POTCAR_H
POTCAR_C
POTCAR_O
POTCAR_Al
POTCAR_Bi
POTCAR_Pd
POTCAR_Se
POTCAR_Cd
POTCAR_Te
POTCAR_S
POTCAR_Au
POTCAR_Ge
POTCAR_Si
POTCAR_Mg
POTCAR_Pb
POTCAR_Hg
POTCAR_Sn
POTCAR_Cr
...</code></pre>  

  </details>  
  
  Para a geração dos inputs necessários a execução dos cálculos High-Throughput DFT, os seguintes critérios devem ser satisfeitos:

  - O usuário deve inserir os arquivos POSCAR dentro de uma pasta chamada **Structures**;
  - Os arquivos POSCAR devem ser escritos em coordenadas diretas;
  - O usuário deve fornecer os arquivos de pseudopotencial (para cada ion presente nos arquivos POSCAR) dentro de uma pasta chamada "**POTCAR**";
  - Os arquivos de pseudopotencial, devem ser rotulados seguindo o padrão presente em em **pseudo files (example)**);
  - O código deve ser executado em **ambiente Linux**, com o pacote **VASPKIT** devidamente instalado, para a configuração do VASPKIT consulte o <a href="https://vaspkit.com/installation.html" target="_blank">link</a>.
 
</details>

------------------------------------

</details>




<details>
<summary><strong>Option [3]: Customizing DFT Calculation Inputs</strong></summary>

------------------------------------

------------------------------------

</details>




<img src="etc/figures/institucional.png" alt="Institutional Network">
