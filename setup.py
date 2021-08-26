from distutils.core import setup

setup(
    name="Product_Information",
    version="0.2dev",
    packages=["Product_Information"],
    package_dir=["Product_Informartion"],
    package_data={"": ["Autex Frontier Acoustic Fins.csv"]},
    include_package_data=True,
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
)
