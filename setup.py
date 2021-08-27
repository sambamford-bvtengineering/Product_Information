from setuptools import setup, find_packages

setup(
    name="Product_Information",
    version="0.3dev",
    packages=find_packages(include=["Product_Information"]),
    package_data={"": ["*.csv"]},
    include_package_data=True,
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
)
