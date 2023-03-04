from setuptools import setup, find_packages

VERSION = "0.0.2" 
DESCRIPTION = "c"

setup(
        name="binscript", 
        version=VERSION,
        author="ngn13",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=["rich"], 
        entry_points={"console_scripts": ["binscript=binscript.__init__:main"]}
)