# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='utils_tabdata',
      version='0.1',
      description='Module with tools to organize and work with tabular data (from CSV files or Pandas Data Frames).',
      url='https://github.com/Asta1986/utils_tabdata',
      author='Asta1986',
      author_email='psljp@protonmail.com',
      license='GPL-3',
      packages=find_packages(),
      install_requires=['pandas>=0.22.0', 'xlsxwriter>=1.0.2'],
      test_suite='nose.collector',
      tests_require=['nose>=1.3.7'],
      include_package_data=True,
      zip_safe=False)
