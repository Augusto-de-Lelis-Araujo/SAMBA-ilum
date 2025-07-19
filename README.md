<img src="etc/figures/code_logo.png" alt="SAMBA logo">
<h1>SAMBA (Simulation and Automated Methods for Bilayer Analysis)
  <a href="https://www.gnu.org/licenses/gpl-3.0">
    <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License: GPL v3">
  </a>
</h1>

<h2>Article available in soon</h2>




<h2>Tutorial</h2>



<details>
  <summary><strong>Description</strong></summary>

-----------------------------------
   
◉ SAMBA is an open-source Python 3 code capable of:

- Automating the generation of twisted homo- and heterobilayers using the coincidence lattice method, ensuring low lattice mismatch and a wide variety of twist angles.
- Automating DFT calculations via the VASP code in a high-throughput approach, including the creation of input files for different types of DFT calculations, along with a customized execution job.
- Analyzing and extracting results, producing high-quality plots (via the VASProcar code) of various structural and electronic properties, as well as storing the data in JSON files.

------------------------------------

◉ **Authors**
  
- Augusto de Lelis Araújo (**<a href="https://orcid.org/0000-0002-6835-6113">ORCID</a>**)
- Adalberto Fazzio (**<a href="https://orcid.org/0000-0001-5384-7676">ORCID</a>**)
- Felipe Castro de Lima (**<a href="https://orcid.org/0000-0002-2937-2620">ORCID</a>**)
- Pedro Henrique Sophia (**<a href="https://orcid.org/0009-0007-5428-0596">ORCID</a>**)

<img src="etc/figures/Authors.png" alt="SAMBA logo">

------------------------------------

◉ **Meet Institutional and Research Network**
  
- Ilum - School of Science **<a href="https://ilum.cnpem.br/en/">link</a>**
- CNPEM - The Brazilian Center for Research in Energy and Materials **<a href="https://cnpem.br/en/">link</a>**
- INCT - Materials Informatics **<a href="https://inct-mi.pesquisa.ufabc.edu.br/">link</a>**
- midb.cloud database **<a href="https://midb.cloud/">link</a>**

<img src="etc/figures/institucional.png" alt="Institutional Network">

------------------------------------
  
</details>




<details>
  <summary><strong>Installation / Source code</strong></summary>

  ------------------------------------
  
  The latest version of SAMBA code can be **installed** using the Python Package Index via the <strong>command below</strong>, while the **source code** is available for **download** via the **<a href="https://pypi.org/project/SAMBA-ilum/">link</a>**.
  <pre><code>pip install samba_ilum</code></pre>

  ------------------------------------

  **Requirements**: Make sure you have the following requirements:
  
  - Linux or Windows environment for bilayer generation;
  - Linux environment for high-throughput DFT (requires VASPKIT installed **<a href="https://vaspkit.com/installation.html" target="_blank">link</a>**);
  - Python 3.8+;
  - Python virtual environment (venv) is recommended;
  - Pseudopotential files for high-throughput DFT (The VASP terms of use do not allow redistributing, publishing, or sharing the POTCAR files).

  ------------------------------------

  During the installation, SAMBA checks the existence of the following Python modules:
  
  - VASProcar **<a href="https://pypi.org/project/vasprocar/">link</a>**
    
    **VASProcar** <img src="etc/figures/VASProcar_logo.png" alt="Descrição" style="vertical-align:middle; width: 20px;"> is one of **SAMBA**'s <img src="etc/figures/SAMBA_logo.png" alt="Descrição" style="vertical-align:middle; width: 20px;"> main packages, which handles the post-processing and plotting of results from **VASP** output files.
  - pymatgen **<a href="https://pypi.org/project/pymatgen/">link</a>**
  - SciPy **<a href="https://pypi.org/project/scipy/">link</a>**
  - NumPy **<a href="https://pypi.org/project/numpy/">link</a>**
  - Matplotlib **<a href="https://pypi.org/project/matplotlib/">link</a>**
  - Plotly **<a href="https://pypi.org/project/plotly/">link</a>**


  <img src="etc/figures/python_packages_logos.png" alt="python_packages"> 

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
SAMBA_ilum v1.0.0.513 Copyright (C) 2025 --------------------
Adalberto Fazzio's research group (Ilum|CNPEM)
Author: Augusto de Lelis Araujo -----------------------------
=============================================================
   _____ ___    __  _______  ___       _ __
  / ___//   |  /  |/  / __ )/   |     (_) /_  ______ ___
  \__ \/ /| | / /|_/ / __  / /| |    / / / / / / __ `___\
 ___/ / ___ |/ /  / / /_/ / ___ |   / / / /_/ / / / / / /
/____/_/  |_/_/  /_/_____/_/  |_|  /_/_/\__,_/_/ /_/ /_/
Simulation and Automated Methods for Bilayer Analysis v1.0.0.513
&#8203;
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
A tutorial on how to use the SAMBA is available on GitHub at the link:
https://github.com/Augusto-de-Lelis-Araujo/SAMBA/blob/main/README.md
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
<summary><strong>Generating Twisted Bilayers</strong></summary>

------------------------------------

<details>
  <summary><strong>1st Step) Create a working directory and, inside it, create a folder where you will place the POSCAR files of the monolayers to be used for bilayer generation</strong></summary>

  ------------------------------------

  **Note:** Both the name of the folder containing the POSCAR files and the labels of these files are freely chosen by the user.

  **Note:** The POSCAR files for bilayer generation must follow the following **criteria** (compare the criteria with the model in **POSCAR file - example**):

<details>
  <summary><strong>POSCAR file - example</strong></summary>
  <pre><code>SAMBA Pt4Se6Hg2_75eb2b2b9759445a
1.0
 7.419406617232910   0.00000000000000   0.0
-3.709703308616455   6.42539461153006   0.0
 0.000000000000000   0.00000000000000   18.526402379698077
Pt Se Hg
4 6 2
Direct
0.0000000000000000  0.5000000000000000  0.5000000000000000
0.0000000000000000  0.0000000000000000  0.5000000000000000
0.5000000000000000  0.5000000000000000  0.5000000000000000
0.5000000000000000  0.0000000000000000  0.5000000000000000
0.3363234295508661  0.1681617147754295  0.5707808825560079
0.8318382852245705  0.6636765704491339  0.5707808825560079
0.8318382852245705  0.1681617147754295  0.5707808825560079
0.1681617147754295  0.8318382852245705  0.4292191174439921
0.1681617147754295  0.3363234295508661  0.4292191174439921
0.6636765704491339  0.8318382852245705  0.4292191174439921
0.3333333333333357  0.6666666666666643  0.5951699375852613
0.6666666666666643  0.3333333333333357  0.4048300624147387</code></pre>
</details>

<details>
  <summary><strong>Criteria for the POSCAR file</strong></summary>

  ------------------------------------
  
  - They must be inserted within the folder defined by **dir_poscar**;
  - They must correspond to 2D lattices whose vectors (A1,A2) are in the KxKy plane, while vector A3 must be on the z-axis;
  - They must be written in direct coordinates;

  - **Optional:** The user can enter an identifier (**ID**) to associate each generated bilayer with its respective source monolayer. To do this, simply include the ID in the first line of the POSCAR file, immediately after the word SAMBA. The code interprets the last string present in this initial line as the ID;

  - **Optional:** It is recommended to use **unit cells**, as using **supercells** can hide possible configurations and slow down code execution. During execution, SAMBA checks whether the cells in the folder defined by **dir_poscar** are unit cells or not, and will ask the user if they want to continue the calculation anyway;

  - **Note:** To ensure that the different twisted angles are correctly obtained, the cell must be constructed so that the **axis of smallest rotation around the z-axis** is positioned at the **cell origin**. If the code identifies that this axis is outside the origin, it will automatically translate the ions to correct this position. The original cell will be preserved in the "**POSCAR_original** directory.

</details>

------------------------------------

</details>


◉ **2nd Step)** In the working directory, run the SAMBA code (**python -m samba_ilum**) and choose **option [0]** to create the input file **SAMBA_HeteroStructure.input**.


<details>
  <summary><strong>3rd Step) Edit the input file SAMBA_HeteroStructure.input, specifying the details of the bilayers to be generated using the tags described below:</strong></summary>

------------------------------------

<details>
  <summary><strong>SAMBA_HeteroStructure.input (description and adjustments)</strong></summary>

  ------------------------------------

  Through this input file, the user controls the details regarding the generation of bilayers for different Twisted angles, where:

  - **dir_poscar** defines the name of the directory containing the POSCAR files of the monolayers to be used in the generation of the bilayers;
  - **dir_o** defines the name of the directory to be created by the code, and where the structural files of the generated bilayers will be stored;
  - **loop_ht** defines how POSCAR files will be used to generate bilayers, where:

    For **loop_ht=0**, the user must enter in **Lattice1** and **Lattice2** the name of the POSCAR files of the bottom and top layers of the stack, respectively. In this case, only the bilayer between these two selected materials is created;

    For **loop_ht=1**, the code will operate in a loop, creating bilayers, referring to the pairwise combination of all structural files contained in the directory defined by **dir_poscar**;

  - **separation_1** defines the vertical separation distance (in Å) between monolayers in the stack;
  - **vacuum** defines the vertical separation (in Å) between periodic images of the cell along the z-axis (due to the periodic boundary condition of the DFT calculation), values above 10Å are usually used;
  - **cell_fator** defines the multiplication factor of vectors A1 and A2 of the cells present in **dir_poscar**, to create the respective supercells;
  - **crit_mod_vector** defines the percentage tolerance (%) in the comparison of the modulus of the lattice vectors A and B between two different lattices (**A1 with A2** and **B1 with B2**). It is used to check if the two lattices have similar vector sizes;
  - **crit_distorc_lattice** defines the percentage tolerance (%) for the difference between vectors A and B of the same lattice (**A1 with B1** and **A2 with B2**). This value measures how much the lattice is distorted (how much it deviates from an ideal square or hexagonal lattice, for example);
  - **crit_angle_perc** defines the percentage tolerance (%) in the variation of the angle formed between the lattice vectors, between the two lattices;
  - **crit_angle_diff** defines the absolute tolerance (in degrees º) of the angular difference between the two lattices. It is a complementary criterion to **crit_angle_perc**;
  - **crit_area** defines the percentage tolerance (%) in the area difference between the two lattices;
  - **ions_crit_i and ions_crit_f** define the lower and upper limits for the number of atoms in the generated structures. These criteria allow the construction of heterostructures with desired dimensions, in addition to avoiding computational problems;
  - **angle_min and angle_max** define the lower and upper limits for the opening angle of the generated structures. These criteria avoid cases where the lattices align nearly parallel (0° or 180°), leading to overly elongated cells, generating physically uninteresting systems, or potentially leading to numerical errors;
  - **mismatch_type** defines how the lattice mismatch will be resolved: which material will be deformed, and which will remain undeformed, where:

    **mismatch_type=0** evenly distributes structural distortion among stack materials;

    **mismatch_type=1** applies structural distortion to the bottom monolayer of the stack;

    **mismatch_type=2** applies structural distortion to the top monolayer of the stack;

  - **rot_angle_calc** defines the geometric reference used to measure the rotation angle between layers, where:

    **rot_angle_calc='center_cell'** defines the angle needed to align the central vector (connecting the origin to the cell center) of both cells;

    **rot_angle_calc='A1'** defines the angle needed to align the A1 vector of both cells;

    **rot_angle_calc='A2'** defines the angle needed to align the A2 vector of both cells;

    ------------------------------------

</details>


<details>
  <summary><strong>SAMBA_HeteroStructure.input (Sample file)</strong></summary>

  <pre><code># SAMBA Copyright (C) 2025

#=========================================================================================================================
# Important notes !!! ====================================================================================================
#=========================================================================================================================
# Use only 2D lattices whose vectors (A1,A2) lie in the KxKy plane, and whose vector A3 lies in the z-axis direction -----
# A1 = (A1x, A1y, 0.0)   |   A2 = (A2x, A2y, 0.0)   |   A3 = (0.0, 0.0, A3z)
#-------------------------------------------------------------------------------------------------------------------------
# Use a 2D unit cell for each material, non-unit cells limit the number of of structures generated, in addition to introducing
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
                                       #                                     POSCAR files contained in the "dir_poscar" directory
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
                                       # Note: Very high values can lead to excessive code slowness.
#----------------------------------
crit_mod_vector  = 3                   # Percentage variation % of the module between the vectors (A and B) of the lattices: A1_with_A2 and B1_with_B2
crit_distorc_lattice = 3               # Percentage variation % of the module between the vectors (A and B) of the same lattice: A1_with_B1 and A2_with_B2
crit_angle_perc = 2                    # Percentage variation % of the angle formed between the vectors (A and B) of the lattices: Theta1_with_Theta2
crit_angle_diff = 2                    # Variation (in module) of the angle in degrees (º) formed between the vectors (A and B) of the lattices: Theta1_with_Theta2
crit_area = 5                          # Percentage variation % of the area of the lattices that will make up the Heterostructure: Area1_with_Area2
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


------------------------------------

</details>

<details>
  <summary><strong>4th Step) Run the SAMBA code</strong></summary>

  ------------------------------------

  - Execute the SAMBA code within the working directory (**python -m samba_ilum**), and subsequently select **option [1]** to initiate the generation of bilayers;
  - **Alternatively:** You may create the **run.input file** in the working directory, write **"task = 1"** in its **first** line, and simply execute the SAMBA code (**python -m samba_ilum**). This is useful for the execution of the SAMBA code on job schedulers, such as **OpenPBS** and **Slurm**, utilized in high-performance computing (**HPC**) environments;
  - Finally, the structural files for the generated bilayers are saved in the **Structures** directory. If the code runs in a **loop**, the structural files for each material combination will be stored in separate folders within the **Structures** directory.

  ------------------------------------

</details>


<details>
  <summary><strong>5th Step) Terminal Messages</strong></summary>

  ------------------------------------

  Below we show an example of the messages printed to the terminal during the execution of the script. These messages indicate the progress of the different steps, such as input loading, calculations, and results generation. This can help the user follow the workflow and identify any issues if they occur.

  <details>
  <summary><strong>Terminal Message - example</strong></summary>
  <pre><code>=============================================================
SAMBA_ilum v1.0.0.513 Copyright (C) 2025 --------------------
Closed source: Adalberto Fazzio's research group (Ilum|CNPEM)
Author: Augusto de Lelis Araujo -----------------------------
=============================================================
    _____ ___    __  _______  ___       _ __              
  / ___//   |  /  |/  / __ )/   |     (_) /_  ______ ___ 
  \__ \/ /| | / /|_/ / __  / /| |    / / / / / / __ `___\ 
 ___/ / ___ |/ /  / / /_/ / ___ |   / / / /_/ / / / / / /
/____/_/  |_/_/  /_/_____/_/  |_|  /_/_/\__,_/_/ /_/ /_/ 
Simulation and Automated Methods for Bilayer Analysis v1.0.0.513
&#8203;
==================================
Wait a moment ====================
==================================
&#8203;
=====================================================================================================
Step 1: Analyzing all possible cells of the 1 Material (Linear combinations of vectors A1 and A2) ===
=====================================================================================================
Progress    1%
...
Progress   100%
&#8203;
=====================================================================================================
Step 2: Analyzing all possible cells of the 2 Material (Linear combinations of vectors A1 and A2) ===
=====================================================================================================
Progress    1%
...
Progress   100%
&#8203;
==============================================================
Step 3: Analyzing lattices matches (1st and 2nd materials) ===
==============================================================
Progress 1/51
...
Progress 51/51
&#8203;
================================================================
Step 4: Writing the POSCAR files for the 2 material lattices ===
================================================================
Progress 1/51
...
Progress 51/51
&#8203;
=============================================================
Step 5: Writing the Heterostructures POSCAR files ===========
=============================================================
Progress 1/51
...
Progress 51/51
--------------------------------
32420 cells were identified
&#8203;
====================================
Step 6: Excluding non-unit cells ===
====================================
Progress 1/51
...
Progress 51/51
--------------------------------------
30452 cells were filtered/excluded
1.968 remaining cells
&#8203;
======================================
Step 7: Deleting Similar Lattices ====
======================================
Progress 1/17
...
Progress 17/17
--------------------------------------
1948 cells were filtered/excluded
20 remaining cells
&#8203;
======================================
Step 8: Deleting Similar Lattices ====
======================================
Progress 1/20
...
Progress 20/20
============================================
12 cells were filtered/excluded
--------------------------------------------
8 cells were found
============================================
&#8203;
========================================
Step 9: Adjusting direct coordinates ===
========================================
Progress 1/8
...
Progress 8/8
&#8203;
============================================
Completed ==================================
============================================</code></pre>
</details>

</details>


<details>
  <summary><strong>Structure of the POSCAR file for the generated bilayers</strong></summary>

  ------------------------------------

  The generated bilayers are labeled as the following structure "**009atoms_-1.352_1.38_60.0_Bi2Se3+Ga2Te2_801626ab7da7c0a5+0002**", with different information separated by "**_**", where:

  - The **1st element** informs the total number of atoms in the generated structure;

  - The **2nd and 3rd elements** correspond respectively, to the percentage variation **applied** to the **Area** of the cell of **Material_A** and the percentage variation **applied** to the **Area** of the cell of **Material_B**, for the formation of the bilayer cell;

  - The **4th element** corresponds to the relative rotation angle between the layers (angle required to align the cell of material B with the cell of material A);

  - The **last element** is the **ID** that identifies the generated structure.

  Below, we present the structure of the POSCAR file of the bilayer corresponding to the label **above**.

  <pre><code>SAMBA Bi_Se+Ga_Te 5 4 | mismatch_areas_12_21 = -2.6948_2.7695 | var_areas = -1.352_1.38 | var_vectors = -0.6783_-0.6783_0.6876_0.6876 | mismatch_angles_12_21 = 0.0_0.0 | var_angles = 0.0_0.0 | rotation_angle = 60.0 | MSCell_1 = 1_1_1_1 | MSCell_2 = -1_-1_-1_-1 | MDeform_1 = 0.993216916_0.0_0.0_0.993216916 | MDeform_2 = 1.00687637_0.0_0.0_1.00687637 | MSTrain_1 = -0.006760079_0.0_0.0_-0.006760079 | MSTrain_2 = 0.006900013_0.0_0.0_0.006900012 | Shift_plane = 0.0_0.0 | Bi2Se3_7f7e8b3365f74a5d Ga2Te2_019a4ea220da4bb7 Bi2Se3+Ga2Te2_801626ab7da7c0a5+0002  
1.00000000000000     
 2.0564035366489999  3.5617954072029998  0.00000000000000000
-2.0564035373560001  3.5617954067939999  0.00000000000000000
 0.0000000000000000  0.0000000000000000  30.0941066965837827
Bi Se Ga Te
 2  3  2  2
Direct
0.6666666666666572  0.6666666666666572  0.3018215616798230
0.3333333333333286  0.3333333333333286  0.4314878698622948
0.0000000000000000  0.0000000000000000  0.3666547157710625
0.6666666666666572  0.6666666666666572  0.4840912016867946
0.3333333333333286  0.3333333333333286  0.2492182298553303
0.0000000000000000  0.0000000000000000  0.6267689929781781
0.0000000000000000  0.0000000000000000  0.7080498733779521
0.3333333333333286  0.3333333333333286  0.5840380959516907
0.3333333333333286  0.3333333333333286  0.7507817701446697</code></pre>

Various structural information regarding the generated bilayer is recorded in the **1st line** of the POSCAR file, where:

- **SAMBA** is just a TAG that allows the SAMBA code to interact with the POSCAR file, extract information and assist in creating input files for high-performance DFT calculations;

- The **2nd element** of the **1st line** of the POSCAR file, corresponds to the ions present in the layer of material A (separated by "**_**") followed by the "**+**" of the ions present in the monolayer of material B (separated by "**_**");

- The following **2 elements** before **mismatch_areas_12_21** correspond, respectively, to the total number of atoms present in the layer of material A and in the layer of material B;

- **mismatch_areas_12_21** corresponds to the percentage variation of the **Area** of the cell of **Material_A** in relation to that of Material_B followed by the percentage variation of the **Area** of the cell of **Material_B** in relation to that of Material_A (referring to pristine monolayers);

- **var_areas** corresponds to the percentage variation **applied** to the **Area** of the cell of **Material_A** followed by the percentage variation **applied** to the **Area** of the cell of **Material_B**, for the formation of the bilayer cell;

- **var_vectors** corresponds to the percentage variation of the modulus **applied** to the **lattice vectors (A1, A2)** of the **Material_A** cell followed by the percentage variation of the modulus **applied** to the **lattice vectors (A1, A2)** of the **Material_B** cell, for the formation of the bilayer cell;

- **mismatch_angles_12_21** corresponds to the percentage variation of the **Opening angle** of the **lattice vectors (A1, A2)** of the cell of **Material_A** in relation to that of Material_B followed by the percentage variation of the **Opening angle** of the **lattice vectors (A1, A2)** of the cell of **Material_B** in relation to that of Material_A (referring to pristine monolayers);

- **var_angles** corresponds to the percentage variation **applied** to the **Opening angle** of the **lattice vectors (A1, A2)** of the **Material_A** cell followed by the percentage variation **applied** to the **Opening angle** of the **lattice vectors (A1, A2)** of the **Material_B** cell, for the formation of the bilayer cell;

- **rotation_angle** corresponds to the relative rotation angle between the layers (angle required to align the cell of material B with the cell of material A);

- **MSCell_1** / **MSCell_2** correspond to the **supercell matrices** that carry the lattice vectors of the original cell provided by the user, the cell used by the code in forming the bilayer (before any deformation is applied);

- **MDeform_1** / **MDeform_2** correspond to the **deformation matrices** applied to the lattice vectors of the cells obtained through the **supercell matrices**, for the formation of the bilayer cell;

- **MSTrain_1** / **MSTrain_2** correspond to the **strain matrices** applied to the lattice vectors of the cells obtained through the **supercell matrices**, for the formation of the bilayer cell;

- **Shift_plane** = corresponds to the direct coordinates (in function of lattice vectors A1 and A2) of the displacement applied to the material B cell, during the xy-scan process;

- The **last 3 elements** of the **1st line** of the POSCAR file, correspond respectively to the identification ID of the monolayer of Material A, monolayer of Material B, and generated bilayer.

</details>

------------------------------------

</details>




<details>
<summary><strong>Generating the inputs for high-throughput DFT calculations</strong></summary>

------------------------------------

◉ **1st Step)** Create a working directory, and inside it, create a folder named 'Structures'. In this folder, you will place the POSCAR files for the structures on which you intend to run DFT calculations.
**Note:** In the POSCAR files, the ions must be specified in direct coordinates.

<details>
  <summary><strong>2nd Step) Pseudopotential files</strong></summary>

  ------------------------------------

  - Within the working directory, the user must place the pseudopotential files (for every ion present in the POSCAR files) into a folder called **POTCAR**";
  - The pseudopotential files must be named according to the pattern below:

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


◉ **3rd Step)** In the working directory, run the SAMBA code (**python -m samba_ilum**) and choose **option [0]** to create the input file **SAMBA_WorkFlow.input**.


<details>
  <summary><strong>4th Step) Edit the SAMBA_WorkFlow.input input file, specifying the details of the DFT calculations to be performed, using the tags described below:</strong></summary>

------------------------------------

<details>
<summary><strong>SAMBA_WorkFlow.input (description and adjustments)</strong></summary>

------------------------------------

Through this input file, the user controls the details of the DFT calculations to be performed in a high-throughput approach, where:

- **dir_virtual_python** defines the **path** where the **python virtual environment** is located;
- **dir_o** defines the name of the output directory (to be created by the code), where the input files for the high-throughput DFT calculation will be generated;
- **replace_type_pseudo** and **replace_type_XC** are information from the DFT calculation to be inserted into the .json files;
- **type_lattice** defines the type of lattice to be analyzed, where:
  
  **type_lattice=1** defines that the analyzed structures are 1D lattices (periodic in X);
  
  **type_lattice=2** defines that the analyzed structures are 2D lattices (periodic in XY);
  
  **type_lattice=3** defines that the analyzed structures are 3D lattices (bulk materials);
- **tasks** defines all the different DFT calculations to be performed in the high-throughput approach, for all structures present in the "Structures" directory;
- **type** defines whether calculations in **tasks** will include spin-orbit coupling (SOC), where:

  **type=['sem_SO']** defines that all calculations are performed disregarding the SOC;
  
  **type=['com_SO']** defines that the SOC is included in the calculations;
  
  **type=['sem_SO','com_SO']** defines that all calculations are performed, both "with" and "without" SOC;
- **ispin** defines the spin polarization for calculations **without SOC**, where:

  **ispin=1**: non-spin-polarized calculations are performed;
  
  **ispin=2**: spin-polarized calculations (collinear) are performed;
- **dipole** defines whether or not dipole correction is included in the calculations, where:
  
  **dipol='none'** disables dipole correction;
  
  **dipol='center_cell'** enables dipole correction; defining the center of the cell as the region relative to which the total dipole moment in the cell is calculated;
  
  **dipol='center_mass'** enables dipole correction; defining the center of mass of the cell as the region relative to which the total dipole moment in the cell is calculated;
- **magnet_mode** defines how magnetization is calculated for non-collinear calculations or with spin polarization enabled, where:
  
  **magnet_mode='default'** sets the VASP default where the MAGMOM tag is set to number_of_ions&#42;1.0 for ISPIN=2 "calculation with spin polarization", or 3&#42;number_of_ions&#42;1.0 for calculation with SOC;
  
  **magnet_mode='MAGMOM=0'** sets the initial magnetic moments of the lattice ions to zero, where the MAGMOM tag is set to number_of_ions**x**0 for ISPIN=2 "calculation with spin polarization", or 3**x**number_of_ions**x**0 for calculation with SOC;
  
  **magnet_mode='NUPDOWN=0'** sets the difference between the number of electrons between the up and down spin components to be zero;
- **U_correction**: Enables or disables Hubbard correction, for transition metals with 3d/4d/5d electrons or Lanthanides/actinides with 4f/5f electrons, where:

  **U_correction=0** (no correction);
  
  **U_correction=1** activates the correction, applied to the following ions (Cr, Mn, Fe, Co, Ni, Cu, La, Ce, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, U). **See ??? if you want to adjust the U correction values applied to each ion**.
  
- **vdW** specifies a vdW dispersion term of the atom-pairwise or many-body type, where:

  **vdW=0** (no correction);
  
  **vdW=integer>0** defines the method used for the dispersion correction added to the total energy, atomic forces, and stress tensor. To see the different methods implemented in VASP, see the **<a href="https://www.vasp.at/wiki/index.php/IVDW" target="_blank">link</a>**;
- **vdWDF** defines the semilocal exchange-correlation functional for vdW correction, where:

  **vdWDF='none'** (no correction);
  
  To activate the correction, choose one of the following semilocal exchange-correlation functionals ('DF', 'DF2', 'optPBE', 'optB88', 'optB86b', 'rev-DF2', 'DF-cx', 'DF3-opt1', 'DF3-opt2'), for more details about each functional see the **<a href="https://www.vasp.at/wiki/index.php/Nonlocal_vdW-DF_functionals" target="_blank">link</a>**;
- **ENCUT_min** Minimum value for the cutoff energy (in eV) used for the plane wave expansion of the wave function;
- **encut_factor** Multiplication factor applied to cutting energy;
  
  **Note:** If (ENCUT_min < ENCUT&#42;encut_factor), then ENCUT_min = ENCUT&#42;encut_factor, where ENCUT refers to the highest cutting energy value present in the POTCAR file;
- **type_k_dens** defines the method used for the Bloch vectors (k-points) used to sample the Brillouin zone in self-consistent calculations (scf), choose between (for more details see the **<a href="https://www.vasp.at/wiki/index.php/KPOINTS" target="_blank">link</a>**):

  **type_k_dens=1** to use Monkhorst-Pack;
  
  **type_k_dens=1** to use Gamma;
  
  **type_k_dens=1** to use KSPACING Monkhorst-Pack;
  
  **type_k_dens=1** to use KSPACING Gamma;
  
- **k_dens_relax** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1 and A2), to sample the Brillouin zone in the structural relaxation calculation;
- **k_dens_scf** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1 and A2), to sample the Brillouin zone in the calculation of the charge density;
- **k_dens_dos** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1 and A2), to sample the Brillouin zone in the calculation of the density of states (DOS);
- **k_dens_bader** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1 and A2), to sample the Brillouin zone in charge density calculations to obtain the Bader's charge;
- **n_kpoints** defines the number of k-points for each high-symmetry line (k-point interval) in the band structure calculation;
- **nions_split** defines the minimum number of atoms in the structure, so that the band structure calculation is segmented/split into different calculations, each referring to a specific high-symmetry line (k-points interval) defined in the KPOINTS file;

  **Note:** This method is useful for calculating the band structure in very large systems (large number of ions) where the available computational power is limited.
- **vacuum** defines the vertical separation (in Å) between periodic images of the cell along the z-axis (due to the periodic boundary condition of the DFT calculation), values above 10 Å are usually used;
- **NCORE** defines the number of "cores" per "node", used by VASP to process the bands in parallel.
- **k_dens_a_scan** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1, A2 and A3), to sample the Brillouin zone in the a-scan calculation (a-scan is a scan by the ideal lattice parameter "a", suitable for bulk 3D systems);
- **factor_var** defines the maximum percentage (%) variation in relation to the initial lattice parameter **a**, as calculated by a-scan;
- **k_dens_z_scan** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1, A2), to sample the Brillouin zone in the z-scan calculation;
- **k_dens_xy_scan** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1, A2), to sample the Brillouin zone in the xy-scan calculation;
- **r_displacement_A1** defines the component of the lateral displacement (relative to the lattice vector A1) performed on the top layer of the stack, in the xy-scan calculation;
- **r_displacement_A2** defines the component of the lateral displacement (relative to the lattice vector A2) performed on the top layer of the stack, in the xy-scan calculation;
- **k_dens_xyz_scan** defines the number of k-points per $Å^{-1}$ (relative to the direction defined by vectors A1 and A2), to sample the Brillouin zone in the xyz-scan calculation (xyz-scan is a combination of the z_scan and xy_scan calculations in a single process);
- **displacement_Z** defines the initial vertical separation values between the layers of the stack, in the xyz-scan calculation;
- **displacement_xyz_A1** defines the component of the lateral displacement (relative to the lattice vector A1) performed on the top layer of the stack, in the xyz-scan calculation;
- **displacement_xyz_A2** defines the component of the lateral displacement (relative to the lattice vector A2) performed on the top layer of the stack, in the xyz-scan calculation.

------------------------------------
  
</details>


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
                      # Note:  If (ENCUT_min < ENCUT&#42;encut_factor), then ENCUT_min = ENCUT&#42;encut_factor
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
k_dens_a_scan = 6       # a-scan calculation: number of k-points per Å^-1
factor_var    = 5       # % variation of the lattice parameter (modulo the smallest lattice vector)

#============================
# z-scan parameters =========
#============================
k_dens_z_scan = 6        # z-scan calculation: number of k-points per Å^-1

#============================
# xy-scan parameters ========
#============================
k_dens_xy_scan = 6                                                                    # xy-scan calculation: number of k-points per Å^-1
r_displacement_A1 = [0.0, (1/8), (1/6), (1/4), (1/3), (1/2), (2/3), (3/4), (5/6)]     # Displacements in the direction of vector A1 (2nd material)
r_displacement_A2 = [0.0, (1/8), (1/6), (1/4), (1/3), (1/2), (2/3), (3/4), (5/6)]     # Displacements in the direction of vector A2 (2nd material)

#============================
# xyz-scan parameters =======
#============================
k_dens_xyz_scan = 6                                       # xyz-scan calculation: number of k-points Å^-1
displacement_Z = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]      # Vertical separation (z-axis) between layers
displacement_xyz_A1 = [0.0, 0.2, 0.4, 0.6, 0.8]           # Displacements in the direction of vector A1 (2nd material)
displacement_xyz_A2 = [0.0, 0.2, 0.4, 0.6, 0.8]           # Displacements in the direction of vector A2 (2nd material)</code></pre>

------------------------------------
</details>


------------------------------------

</details>


<details>
  <summary><strong>5th Step) Run the SAMBA code </strong></summary>

  ------------------------------------

  - Execute the SAMBA code within the working directory (**python -m samba_ilum**), and subsequently select **option [2]** to initiate the generation of inputs for the selected DFT calculations for all structures within the Structures folder;
  - **Alternatively:** You may create the **run.input file** in the working directory, write **"task = 2"** in its **first** line, and simply execute the SAMBA code (**python -m samba_ilum**). This is useful for the execution of the SAMBA code on job schedulers, such as **OpenPBS** and **Slurm**, utilized in high-performance computing (**HPC**) environments;
  - Finally, the input files for the selected DFT calculations for all structures within the Structures folder are saved to the directory defined by the **dir_o** tag in **SAMBA_WorkFlow.input**. The input files for each structure will be stored in separate folders, named after the corresponding structural file.

------------------------------------

</details>


<details>
  <summary><strong>6th Step) Terminal Messages</strong></summary>

  ------------------------------------

  Below we show an example of the messages printed to the terminal during the execution of the script. These messages indicate the progress of the different steps, such as input loading, calculations, and results generation. This can help the user follow the workflow and identify any issues if they occur.

  <details>
  <summary><strong>Terminal Message - example</strong></summary>
  <pre><code>=============================================================
SAMBA_ilum v1.0.0.513 Copyright (C) 2025 --------------------
Closed source: Adalberto Fazzio's research group (Ilum|CNPEM)
Author: Augusto de Lelis Araujo -----------------------------
=============================================================
   _____ ___    __  _______  ___       _ __
  / ___//   |  /  |/  / __ )/   |     (_) /_  ______ ___
  \__ \/ /| | / /|_/ / __  / /| |    / / / / / / __ `___\
 ___/ / ___ |/ /  / / /_/ / ___ |   / / / /_/ / / / / / /
/____/_/  |_/_/  /_/_____/_/  |_|  /_/_/\__,_/_/ /_/ /_/
Simulation and Automated Methods for Bilayer Analysis v1.0.0.513
&#8203;
==================================
Wait a moment ====================
==================================
&#8203;
---------------------------------------------------------------------
Creating directories and copying POSCAR and VASProcar input files ---
---------------------------------------------------------------------
Progress   1%
...
Progress   100%
&#8203;
-------------------------------------------------------------------------
Creating POTCAR files for each material ---------------------------------
-------------------------------------------------------------------------
Progress   1%
...
Progress   100%
&#8203;
-------------------------------------------------------------------------
Creating KPOINT file for each material ----------------------------------
-------------------------------------------------------------------------
Progress   1%
...
Progress   100%
&#8203;
-------------------------------------------------------------------------
Creating INCAR file for each material -----------------------------------
-------------------------------------------------------------------------
Progress   1%
...
Progress   100%
&#8203;
=============
Completed ===
=============</code></pre>
</details>

</details>


<details>
  <summary><strong>Optional: Customizing DFT Calculations</strong></summary>

  ------------------------------------

  To customize the DFT calculations, run the SAMBA code (**python -m samba_ilum**) in your working directory and select **option [3]**.

  This action will create the **WorkFlow_INPUTS** folder. It contains the **INCAR files** for the different VASP calculation steps and the inputs for **VASProcar**, the code responsible for post-processing the data and generating plots. As long as the WorkFlow_INPUTS folder exists in the working directory, its files will be used as the default for the high-throughput DFT calculations.

  **Note:** In the generated INCAR files, tags starting with "**replace**" or "**#**" are placeholders that SAMBA **replaces automatically**. If you wish to set a specific value for one of these parameters, you must replace the placeholder (e.g., replace_ispin) with the corresponding official VASP tag (e.g., ispin) and then set the desired value. For details on all INCAR tags, consult the official VASP documentation at the link **<a href="https://www.vasp.at/wiki/index.php/Category:INCAR_tag" target="_blank">link</a>**.

  **Note:** For the generation of inputs for high-throughput DFT, the code must be run in a **Linux environment** with the **VASPKIT** package properly installed.

</details>

------------------------------------

</details>




<details>
<summary><strong>Setting up the Linux environment for High-Throughput DFT calculations</strong></summary>

-----------------------------------

◉ **1st)** In the Linux environment where the DFT calculations will be executed, load in a python package version higher than 3.8 (or a recent version of the CONDA package), using the command: **module load** package_name.
  <pre><code>example:  module load python_3.8.11-intel-2021.3.0</code></pre>
  or
  <pre><code>example:  module load CONDA_2025.5.1</code></pre>

◉ **2nd)** Select a directory of interest and create a Python virtual environment using the command: **python -m venv** python_environment_name
   <pre><code>example:  python -m venv python_virtual</code></pre>  
     
   Save the path of the Python environment you created, as this is the **path** you should use in the **dir_virtual_python** tag of **SAMBA_WorkFlow.input**
   <pre><code>example:  dir_virtual_python = '/home/dlelis/codes/python_virtual'</code></pre>  

◉ **3rd)** Activate the Python environment using the command: **source** path_to_python_environment + **/bin/activate**
  <pre><code>example:  source /home/dlelis/codes/python_virtual/bin/activate</code></pre>

◉ **4th)** After activating the Python environment, install the following packages **SAMBA**, **VASProcar** and **pymatgen**, using the commands:
  <pre><code>pip install --upgrade samba_ilum</code></pre>
  <pre><code>pip install --upgrade vasprocar</code></pre>
  <pre><code>pip install --upgrade pymatgen</code></pre>

◉ **5th)** VASPKIT Installation:

  ------------------------------------
  
  Download VASPKIT from **<a href="https://sourceforge.net/projects/vaspkit/files/Binaries/" target="_blank">link</a>**, and if you want more information about this package, see **<a href="https://vaspkit.com/installation.html" target="_blank">link</a>**.

  To perform the installation, see the commands below, where I took as an example the downloaded file (vaspkit.1.5.1.tar.gz) to be installed in the directory (/home/dlelis/codes).
  After downloading VASPKIT, move the file to the directory of interest, and within this directory run the following commands:
  <pre><code>tar -zxvf vaspkit.1.5.1.tar.gz</code></pre>
  <pre><code>cd vaspkit.1.5.1</code></pre>
  <pre><code>cp -f how_to_set_environment_variables ~/.vaspkit</code></pre>
  <pre><code>echo 'export PATH=/home/dlelis/codes/vaspkit.1.5.1/bin/:$PATH' >> ~/.bashrc</code></pre>
  <pre><code>source ~/.bashrc</code></pre>

  To confirm that the installation was configured correctly, just type **vaspkit** in the terminal and the code should be executed.

  <img src="etc/figures/VASPKIT_logo.png" alt="Descrição" style="vertical-align:center; width: 240px;">

------------------------------------

</details>




<details>
<summary><strong>Submitting High-Throughput DFT jobs</strong></summary>

-----------------------------------

◉ When using **option [2]** of the SAMBA code, in addition to the input files required for high-performance DFT calculations, the code provides two job files for executing the calculations in a Linux environment through task schedulers, such as **Slurm**, **OpenPBS**, **Torque**, etc, commonly used in high throughput computing (**HPC**) environments, these being the files **job.sh** and **job0.sh**, where:

<details>
  <summary><strong>job.sh (Primary task scheduler file)</strong></summary>

------------------------------------

- The **job.sh** file is the main file that must be executed to submit calculations to the task scheduler, and has the following structure:

<pre><code>#!/bin/bash
#SBATCH --partition=medium
#SBATCH --job-name=WFlow
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --ntasks=32
#SBATCH --exclusive
#SBATCH -o %x.o%j
#SBATCH -e %x.e%j

#--------
dir0=`pwd`
#dir0="/mnt/bgfs/home/dlelis/WorkFlow//WorkFlow_TESTE"
#---------------------
source $dir0/./job0.sh
#---------------------</code></pre>

- The initial tags of the **job.sh** file refer to execution in the **Slurm** task scheduler, and it is necessary to edit its fields depending on the specific environment where the calculations will be executed, as well as adapting them for other task schedulers such as **OpenPBS**, **Torque**, **LoadLeveler**, etc;

- The **dir0** tag refers to the **full path** where the files for executing the DFT calculations are located, depending on the Linux environment the **pwd** command is sufficient to inform the full path, however, if this command fails, inform the full path explicitly by just removing the "**#**" in the lower field, and editing the path if the folder generated by the SAMBA code has been moved to another location;

------------------------------------

</details>

<details>
  <summary><strong>job0.sh (Auxiliary task scheduler file)</strong></summary>

------------------------------------

- The **job0.sh** file is the auxiliary file that contains information about the packages to be used and the DFT calculations to be performed. Because it is separate from the main job file **job.sh**, it can be edited as the user sees fit before the calculation is actually started in the task scheduler. The **job0.sh** file has the following structure:

<pre><code>#!/bin/bash

cd $dir0
mv python_virtual python_virtual_delete
rm -r python_virtual_delete

#-------------------------------
dir_virtual="/home/dlelis/codes/python_virtual"
#cp -r $dir_virtual $dir0/python_virtual
#dir_virtual="$dir0/python_virtual"
source $dir_virtual/bin/activate
#-------------------------------

cd $SLURM_SUBMIT_DIR
ulimit -s unlimited

module load vasp/6.2.0-intel-2021.2.0
vasp_std="mpirun -n ${SLURM_NTASKS} vasp_std"
vasp_ncl="mpirun -n ${SLURM_NTASKS} vasp_ncl"
#------------------------
#module load vasp-6.2.0-gcc-9.3.0-epqgvat
#vasp_std="srun -n ${SLURM_NTASKS} vasp_std"
#vasp_ncl="srun -n ${SLURM_NTASKS} vasp_ncl"

ttasks=( "xyz-scan" "z-scan" "xy-scan" "a-scan" "relax" "scf" "bands" "dos" "bader" "scf.SO" "bands.SO" "dos.SO" "bader.SO" )

#------------------------
if [ ! -d "$dir0/completed" ]; then
   mkdir "$dir0/completed"
fi
#------------------------
while true; do

...
...
...

done</code></pre>

- **dir_virtual** especifica o caminho do ambiente virtual Python a ser carregado para a execução de scripts ao longo da execução do job, este caminho é definido na tag **dir_virtual_python** do arquivo de input **SAMBA_WorkFlow.input**;

- **module load** loads into the Linux environment the version of the DFT package **VASP** to be used in the calculations;

- **vasp_std** and **vasp_ncl** define the commands for executing the DFT package **VASP**, for **collinear** (without SOC) and **non-collinear** (with SOC) calculations;

- **Note)** The **ttasks** tag should under no circumstances be edited.

</details>

------------------------------------

</details>




<details>
<summary><strong>Database: Twisted 2D van der Waals Homo and Hetero Bilayers (midb.cloud) </strong></summary>

-----------------------------------

The **SAMBA** code was developed with the goal of accelerating the generation of a database based on first-principles calculations grounded in Density Functional Theory (DFT), using the VASP package. It focuses on homo- and hetero-structured van der Waals bilayers with varying twist angles.

Initially, its development enabled the generation of over **18,000** distinct twisted bilayers, derived from **63** monolayers of naturally exfoliable materials or materials with previously reported synthesis, all exhibiting van der Waals interlayer interactions.

Subsequently, SAMBA also allowed for high-throughput structural relaxation and electronic property calculations for more than **800** of these bilayers, a number that continues to grow.

All data are available in the database of the **INCT – Materials Informatics project** (**midb.cloud** **<a href="https://midb.cloud/">link</a>**), under the title: "**Twisted 2D van der Waals Homo and Hetero Bilayers**" **<a href="https://www.midb.cloud/search?show_pt=no&query=(dataset=='Twisted 2D van der Waals Homo and Hetero Bilayers')">link</a>**.

-----------------------------------

</details>




<details>
<summary><strong>Support</strong></summary>

-----------------------------------

For more informations/questions or to report potential bugs, send an e-mail to: augusto-lelis@outlook.com

------------------------------------

</details>




<img src="etc/figures/institucional.png" alt="Institutional Network">
