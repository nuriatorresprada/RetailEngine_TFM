from setuptools import setup, find_packages

setup(
    name="retail_engine",
    version="3.2.0",
    author="Nuria Torres Prada",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas", 
        "matplotlib", 
        "seaborn", 
        "openpyxl"
    ],
    python_requires=">=3.8"
)