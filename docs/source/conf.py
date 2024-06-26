# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '8891 Wild Raccoons'
copyright = '2024, Wild Raccoons'
author = '8891 Wild Raccoons'

release = '0.1'
version = '0.1.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_material'

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Wild Raccoons’s FRC Documentation',

    'theme_color': '9240ad',

    'color_primary': '9240ad',

    'color_accent': 'green'

}

# -- Options for EPUB output
epub_show_urls = 'footnote'
