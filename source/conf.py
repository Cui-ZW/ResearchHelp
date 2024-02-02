# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '科研手册'
copyright = '2024, Zhiwen Cui'
author = 'Zhiwen Cui'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 'myst_parser',  #support markdown
              'sphinx_markdown_tables' #support tables
              ]
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = []
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
]

templates_path = ['_templates']
exclude_patterns = []

# language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
