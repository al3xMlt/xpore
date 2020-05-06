"""Setup for the xpore package."""

from setuptools import setup,find_packages

__pkg_name__ = 'xpore'


with open('README.md') as f:
    README = f.read()

setup(
    author="Ploy N. Pratanwanich",
    maintainer_email="naruemon.p@chula.ac.th",
    name=__pkg_name__,
    license="MIT",
    description='xpore is a python package for Nanopore data analysis.',
    version='v0.1.2',
    long_description=README,
    url='https://github.com/GoekeLab/xpore',
    packages=find_packages(),
    install_requires=[
            'numpy>=1.18.0',
            'pandas>=0.25.3',
            'scipy>=1.4.1',
            'PyYAML>=5.3.1',
            'h5py>=2.10.0',
            'pysam>=0.15.4',
            'pyensembl>=1.8.5'
            ],
    python_requires=">=3.5",
    entry_points={'console_scripts': ["xpore-dataprep={}.scripts.dataprep:main".format(__pkg_name__),
                                      "xpore-diffmod={}.scripts.diffmod:main".format(__pkg_name__)]},
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
    ],
)
