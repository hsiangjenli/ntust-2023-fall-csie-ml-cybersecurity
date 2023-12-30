import datetime
import os.path as osp
import os
pkg_path = os.path.abspath(os.path.join(__file__, "..", "..", ".."))

import sys;sys.path.append(pkg_path)
import pyg_sphinx_theme as my_sphinx_theme
import script

author = 'Hsiang-Jen Li'

copyright = f'{datetime.datetime.now().year}, {author}'

if datetime.datetime.now().year != 2023:
    copyright = "2023 ~ " + copyright


sys.path.append(osp.join(osp.dirname(my_sphinx_theme.__file__), 'extension'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'nbsphinx',
]

html_theme = 'pyg_sphinx_theme'
html_logo = ('https://hsiangjenli.github.io/hsiangjenli/static/image/ntust.png')
html_favicon = ('https://hsiangjenli.github.io/hsiangjenli/static/image/ntust.png')


add_module_names = False
autodoc_member_order = 'bysource'

suppress_warnings = ['autodoc.import_object']

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/dev', None),
    'torch': ('https://pytorch.org/docs/master', None),
}


def setup(app):
    def rst_jinja_render(app, _, source):
        rst_context = {'script': script}
        source[0] = app.builder.templates.render_string(source[0], rst_context)

    app.connect('source-read', rst_jinja_render)
    app.add_js_file('js/version_alert.js')