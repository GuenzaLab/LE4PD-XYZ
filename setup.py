from setuptools import setup

setup(
    name = 'LE4PD',
    version = '0.3',
    author = 'Pablo Romano and Eric Beyerle',
    description = 'Python API for Protein Dynamics using the Langevin Formalism (LE4PD)',
    url = 'https://github.com/erb24/LE4PD',

    packages = ['LE4PD'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'mdtraj',
        'openmm',
	'physt'
    ],
    zip_safe = False
)
