# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Wild Raccoons Documentation'
copyright = '2024, Wild Raccoons'
author = 'Wild Raccoons'

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

    # Set you GA account ID to enable tracking
    #'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://wildraccoons8891.readthedocs.io/en/latest/',

    # Set the color and the accent color
    'color_primary': 'purple',
    'color_accent': 'light-purple',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/wildraccoons/Documentation',
    'repo_name': 'Documentation',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': False,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
