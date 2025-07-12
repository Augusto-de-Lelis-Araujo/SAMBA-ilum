# SAMBA (Simulation and Automated Methods for Bilayer Analysis) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
## Article available in ?????: in soon

SAMBA is an open-source Python 3 code capable of:
- Automating the generation of twisted homo- and heterobilayers using the coincidence lattice method, ensuring low lattice mismatch and a wide variety of twist angles.
- Automating DFT calculations via the VASP code in a high-throughput approach, including the creation of input files for different types of DFT calculations, along with a customized execution job.
- Analyzing and extracting results, producing high-quality plots (via the VASProcar code) of various structural and electronic properties, as well as storing the data in JSON files.


<details>
<summary><strong>Authors</strong></summary>
  
- Augusto de Lelis Araújo ([ORCID](https://orcid.org/0000-0002-6835-6113))
- Adalberto Fazzio ([ORCID](https://orcid.org/0000-0001-5384-7676))
- Felipe Castro de Lima ([ORCID](https://orcid.org/0000-0002-2937-2620))
- Pedro Henrique Sophia ([ORCID](https://orcid.org/0009-0007-5428-0596))

</details>


## Tutorial
Click on the topics below to expand and see the details for each section.

<details>
<summary><strong>Requirements</strong></summary>

Make sure you have the following requirements:
- Linux or Windows environment for bilayer generation
- Linux environment for high-throughput DFT (requires VASPkit installed)
- Python 3.8+
- Python virtual environment is recommended (`venv` or `conda`)

</details>

<details>
<summary><strong>Instalação</strong></summary>
  
The latest version of the SAMBA code can be installed using the Python Package Index via the command:
```bash
pip install samba_ilum
```
During the installation, SAMBA checks the existence of the following Python modules:
- [vasprocar](https://pypi.org/project/vasprocar/)
- [pymatgen](https://pypi.org/project/pymatgen/)
- [scipy](https://pypi.org/project/scipy/)
- [numpy](https://pypi.org/project/numpy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [plotly](https://pypi.org/project/plotly/)

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


------------------------------------------------------------------------

<img src="etc/figures/logo.png">
