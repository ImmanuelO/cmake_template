# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os


project = 'CPP Template'
copyright = '2025, John Smith'
author = 'John Smith'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "breathe",
]

breathe_projects = {
    "cpp_template": os.path.abspath("../../../build/docs/doxygen/xml"),
}

breathe_default_project = "cpp_template"

breathe_domain_by_extension = {
    "h": "cpp",
    "hpp": "cpp",
    "cpp": "cpp",
}


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['']
