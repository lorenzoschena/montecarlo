# -- Path setup --------------------------------------------------------------

import os
import sys

# Add project root so autodoc can find the package
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

project = 'montecarlo'
author = 'VKI'

# Extract version from the package
import montecarlo
version = montecarlo.__version__
release = version

language = 'en'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
]

autosummary_generate = True
autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = []

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Optional sidebar (RTD theme supports this nicely)
html_sidebars = {
    '**': [
        'relations.html',
        'searchbox.html',
    ]
}

# -- Intersphinx mapping -----------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
}