# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys, os
sys.path.insert(0,os.path.abspath("../.."))

project = 'mandelbrot_julia'
copyright = '2024, Leonard Nader et Camille Revol'
author = 'Leonard Nader et Camille Revol'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'sphinx.ext.viewcode', 'myst_parser', 'sphinx.ext.mathjax']
myst_enable_extensions = [
    "amsmath",  # Pour les blocs d’équations en Markdown
    "dollarmath"  # Pour le support des symboles $...$ en inline
]



templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

source_suffix=[".rst", ".md"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']
