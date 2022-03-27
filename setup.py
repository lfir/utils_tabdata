from setuptools import find_packages, setup


def readme():
    file_name = "README.rst"
    with open(file_name, "r") as f:
        return f.read()


setup(
    name="utils_tabdata",
    version="1.0.5",
    description="Module with tools to organize and work with tabular data (from CSV files or Pandas Data Frames).",
    long_description=readme(),
    url="https://github.com/Asta1986/utils_tabdata",
    author="Asta1986",
    author_email="psljp@protonmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires="~=3.10",
    install_requires=[
        "click~=8.0",
        "matplotlib~=3.3",
        "openpyxl~=3.0",
        "pandas~=1.2",
        "xlsxwriter~=3.0",
        "pytest"
    ],
    entry_points="""
                [console_scripts]
                utils_tabdata=utils_tabdata.scripts:cli
                """,
    include_package_data=True,
    zip_safe=False,
)
