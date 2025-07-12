# SAMBA

SAMBA (Simulation and Automated Methods for Bilayer Analysis) is an open-source Python 3 code capable of:
- Automating the generation of twisted homo- and heterobilayers using the coincidence lattice method, ensuring low lattice mismatch and a wide variety of twist angles.
- Automating DFT calculations via the VASP code in a high-throughput approach, including the creation of input files for different types of DFT calculations, along with a customized execution job.
- Analyzing and extracting results, producing high-quality plots (via the VASProcar code) of various structural and electronic properties, as well as storing the data in JSON files.

## Tutorial
Click on the topics below to expand and see the details for each section.

<details>
<summary><strong>Prerequisites</strong></summary>

Make sure you have the following prerequisites:
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
- vasprocar
- pymatgen
- scipy
- numpy
- matplotlib
- plotly

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
