# SAMBA

Breve descrição do que seu código faz. Por exemplo: "Uma coleção de scripts em Python para automatizar a criação de estruturas de materiais 2D e a execução de cálculos de alto rendimento com DFT."


## Tutorial
Clique nos tópicos abaixo para expandir e ver os detalhes de cada seção.



<details>
<summary><strong>Instalação</strong></summary>

### Pré-requisitos
Certifique-se de que você possui os seguintes softwares instalados:
- Python 3.8+
- Um ambiente virtual (recomendado, ex: `venv` ou `conda`)
- Git

The latest version of the SAMBA code can be installed using the Python Package Index via the command:
### pip install samba_ilum

During the installation, SAMBA checks the existence of the following Python modules:
- vasprocar
- pymatgen
- scipy
- numpy
- matplotlib
- plotly

For run the code, the user must use the command below in the work directory.
### python -m samba_ilum
or
### python3 -m samba_ilum
 
### Passos para Instalação

1.  **Clone o repositório:**
    Certifique-se de que você possui os seguintes softwares instalados:
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    O projeto depende de bibliotecas como NumPy, SciPy e Matplotlib. Instale todas com o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Verifique a instalação:**
    Execute o script de teste para garantir que tudo está funcionando corretamente.
    ```bash
    python run_tests.py
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
