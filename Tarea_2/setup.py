from setuptools import setup
from Cython.Build import cythonize

pyx_files = ["P1\P1.pyx", "P2\P2.pyx"]

setup(
    ext_modules=cythonize(pyx_files, language_level="3"),
)
