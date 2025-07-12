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

This option generates the following input files for the SAMBA code:
```text
SAMBA_HeteroStructure.input
SAMBA_WorkFlow.input
```
-----------------------------------

   <details>
   <summary><strong>SAMBA_HeteroStructure.input</strong></summary>

      <details>
      <summary><strong>Sample file</strong></summary>

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
      # What do you want to run? ? =========================================
      # ====================================================================
      # [0] Generate SAMBA execution inputs
      # --------------------------------------------------------------------
      # [1] Heterostructure Generator
      # [2] WorkFlow: High Throughput DFT (inputs + job)
      # --------------------------------------------------------------------
      # [3] Customize internal WorkFlow inputs (INPUTS folder)
      ######################################################################
      ```

      </details>
     
   </details>
    
-----------------------------------

   <details>
   <summary><strong>SAMBA_WorkFlow.input</strong></summary>
     
   </details>
   
-----------------------------------

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
