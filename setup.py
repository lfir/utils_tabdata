from setuptools import find_packages, setup


def readme():
    file_name = 'README.rst'
    with open(file_name, 'r') as f:
        return f.read()

setup(name='utils_tabdata',
    version='0.2',
    description='Module with tools to organize and work with tabular data (from CSV files or Pandas Data Frames).',
    long_description=readme(),
    url='https://github.com/Asta1986/utils_tabdata',
    author='Asta1986',
    author_email='psljp@protonmail.com',
    license='GPL-3',
    packages=find_packages(),
    python_requires='~=3.9',
    install_requires=[
        'click~=7.1',
        'matplotlib~=3.3',
        'pandas~=1.2',
        'xlrd~=1.2',
        'xlsxwriter~=1.3'
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points='''
                [console_scripts]
                utils_tabdata=utils_tabdata.scripts:cli
                ''',
    include_package_data=True,
    zip_safe=False
)
