import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nilslib',
    version='1.0',
    author='Nils',
    description='Collection of small tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nils865/nilsLib.py',
    license='MIT',
    packages=['nilslib'],
    install_requires=[],
)
