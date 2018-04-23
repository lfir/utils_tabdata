# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


def readme():
    file_name = 'README.rst'
    with open(file_name, 'r') as f:
        return f.read()


setup(name='utils_tabdata',
      version='0.1',
      description='Module with tools to organize and work with tabular data (from CSV files or Pandas Data Frames).',
      long_description=readme(),
      url='https://github.com/Asta1986/utils_tabdata',
      author='Asta1986',
      author_email='psljp@protonmail.com',
      license='GPL-3',
      packages=find_packages(),
      install_requires=['pandas==0.22.0', 'xlsxwriter==1.0.2', 'click==6.7'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points='''
                   [console_scripts]
                   utils_tabdata=utils_tabdata.scripts:cli
                   ''',
      include_package_data=True,
      zip_safe=False)
