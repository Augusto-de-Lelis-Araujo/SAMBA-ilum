import os
import sys
sys.path.insert(0, os.path.abspath(".."))

project = 'SAMBA'
author = 'Augusto de Lelis Araújo'

extensions = ['myst_parser']

source_suffix = {
    '.md': 'markdown',
}

html_theme = 'sphinx_rtd_theme'
