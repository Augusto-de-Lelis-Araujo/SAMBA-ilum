<h1>SAMBA (Simulation and Automated Methods for Bilayer Analysis)
  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3">
  </a>
</h1>

<h2>Article available in soon</h2>

<details>
  <summary><strong>Description</strong></summary>
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
    <li><strong>Option [4]</strong>: provides the default input files to be used with VASP, which the user can freely modify to further personalize or specialize the calculations according to their preferences.</li>
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
      <pre><code>
=============================================================
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
                                       # POSCAR files contained in the "dir_poscar" directory
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
cell_fator = [10, 10]                  # Multiplication factor of the unit cell as a function of vectors A1, A2.
crit_mod_vector  = 3                   # % variation of module between A1_with_A2 and B1_with_B2
crit_distorc_lattice = 3              # % variation of module between A1_with_B1 and A2_with_B2
crit_angle_perc = 2                    # % variation of angle Theta1_with_Theta2
crit_angle_diff = 2                    # absolute angle variation (º)
crit_area = 5                          # % variation of area
ions_crit_i = 1                        # min number of atoms
ions_crit_f = 100                      # max number of atoms
angle_min = 15.0                       # min twist angle
angle_max = 165.0                      # max twist angle
mismatch_type = 0                      # deformation control
rot_angle_calc = 'center_cell'         # rotation reference
      </code></pre>
    </details>
  </details>

  <hr/>

  <details>
    <summary><strong>SAMBA_WorkFlow.input</strong></summary>
    <!-- conteúdo aqui -->
  </details>
</details>

<hr/>

<details>
  <summary><strong>Arquivos Estruturais</strong></summary>
  <p><strong>Formatos Suportados</strong></p>
  <p>O código utiliza arquivos no formato <code>POSCAR</code> (usado pelo VASP) ou <code>.xyz</code> para ler as coordenadas atômicas iniciais. A estrutura do arquivo deve seguir o padrão convencional.</p>
  <p><strong>Exemplo de estrutura de diretório:</strong></p>
</details>

<details>
  <summary><strong>Exemplo 01</strong></summary>
  <p><strong>Formatos Suportados</strong></p>
  <p>O código utiliza arquivos no formato <code>POSCAR</code> (usado pelo VASP) ou <code>.xyz</code> para ler as coordenadas atômicas iniciais. A estrutura do arquivo deve seguir o padrão convencional.</p>
  <p><strong>Exemplo de estrutura de diretório:</strong></p>
</details>

<details>
  <summary><strong>Exemplo 02</strong></summary>
  <p><strong>Formatos Suportados</strong></p>
  <p>O código utiliza arquivos no formato <code>POSCAR</code> (usado pelo VASP) ou <code>.xyz</code> para ler as coordenadas atômicas iniciais. A estrutura do arquivo deve seguir o padrão convencional.</p>
  <p><strong>Exemplo de estrutura de diretório:</strong></p>
</details>
