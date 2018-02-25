import sys
import setuptools

# Check for Tkinter availability
try:
    if sys.version_info[0] < 3:
        import Tkinter
    else:
        import tkinter
except ImportError:
    sys.exit("Tkinter is required to run pymenuconfig")


setuptools.setup(
    name='pymenuconfig',
    version='1.0.0',
    description='Kconfiglib frontend written in Tkinter',
    author='Roman Dobrodii',
    author_email='roman.dobrodii@gmail.com',
    url='https://github.com/RomaVis/pymenuconfig',
    license='ISC',
    python_requires='>=2.7',
    py_modules=('pymenuconfig',),
    install_requires=('kconfiglib>=2.0',),
)
