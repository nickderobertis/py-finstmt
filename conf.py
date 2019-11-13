# This is the main settings file for package setup and PyPi deployment.
# Sphinx configuration is in the docsrc folder

# Main package name
PACKAGE_NAME = 'py_qs_example'

# Package version in the format (major, minor, release)
PACKAGE_VERSION_TUPLE = (0, 1, 9)

# Short description of the package
PACKAGE_SHORT_DESCRIPTION = 'Python package PyPi Sphinx quickstart example app'

# Long description of the package
PACKAGE_DESCRIPTION = """
This is the example application for a quick start repo which was created by using pypi-sphinx-quickstart.
Fork the repo at https://github.com/whoopnip/pypi-sphinx-quickstart and edit the conf.py files to bootstrap
a Python project with PyPi deployment and Sphinx auto documentation already set up.
"""

# Author
PACKAGE_AUTHOR = "Nick DeRobertis"

# Author email
PACKAGE_AUTHOR_EMAIL = 'mail@example.com'

# Name of license for package
PACKAGE_LICENSE = 'MIT'

# Classifications for the package, see common settings below
PACKAGE_CLASSIFIERS = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

# Add any third party packages you use in requirements here
PACKAGE_INSTALL_REQUIRES = [
    # Include the names of the packages and any required versions in as strings
    # e.g.
    # 'package',
    # 'otherpackage>=1,<2'
]

# Sphinx executes all the import statements as it generates the documentation. To avoid having to install all
# the necessary packages, third-party packages can be passed to mock imports to just skip the import.
# By default, everything in PACKAGE_INSTALL_REQUIRES will be passed as mock imports, along with anything here.
# This variable is useful if a package includes multiple packages which need to be ignored.
DOCS_OTHER_MOCK_IMPORTS = [
    # Include the names of the packages as they would be imported, e.g.
    # 'package',
]

# Add any Python scripts which should be exposed to the command line in the format:
# CONSOLE_SCRIPTS = ['funniest-joke=funniest.command_line:main']
CONSOLE_SCRIPTS = [],

# Add any arbitrary scripts to be exposed to the command line in the format:
# SCRIPTS = ['bin/funniest-joke']
SCRIPTS = []

PACKAGE_URLS = {
    'Code': 'https://github.com/whoopnip/pypi-sphinx-quickstart/',
    'Documentation': 'https://whoopnip.github.io/pypi-sphinx-quickstart/'
}
