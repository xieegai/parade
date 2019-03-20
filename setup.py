#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python :: 3
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: Unix
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX
"""

setup(
    name='parade',
    # auto generate version
    # use_scm_version=True,
    version='0.1.22.4',
    author='He Bai',
    author_email='bailaohe@gmail.com',

    description='A ETL engine for dataframe based data task',

    keywords=["parade", "ETL", "dataframe", "schedule", "database"],
    url='https://github.com/bailaohe/parade',
    platforms=["any"],
    classifiers=filter(None, classifiers.split("\n")),

    install_requires=['pandas', 'sqlalchemy', 'requests', 'pyyaml',
                      'psycopg2', 'mysqlclient', 'xlsxwriter',
                      'flask', 'flask_cors', 'flask_restful', 'Flask-SocketIO',
                      'PyGithub', 'pymongo', 'redis', 'jupyter', 'nbformat'],

    packages=find_packages('src'),
    package_dir=({'parade': 'src/parade'}),
    zip_safe=False,

    include_package_data=True,
    package_data={'': ['*.json', '*.xml', '*.yml', '*.tpl']},

    entry_points={
        'console_scripts': [
            'parade = parade.cmdline:execute',
        ],
    },

    # extras_require={
    #     "solr": ["solr-doc-manager"],
    #     "elastic": ["elastic-doc-manager"],
    #     "elastic-aws": ["elastic-doc-manager[aws]"],
    #     "elastic2": ["elastic2-doc-manager[elastic2]"],
    #     "elastic5": ["elastic2-doc-manager[elastic5]"],
    #     "elastic2-aws": ["elastic2-doc-manager[elastic2,aws]"],
    # },
    # setup_requires=[
    #     "setuptools_scm>=1.5",
    # ],
    python_requires=">=3.4",
    # download_url='https://github.com/bailaohe/parade/tarball/0.1',
)
