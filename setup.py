import os
import imp
from setuptools import setup, find_packages

dirname = os.path.dirname(__file__)
path_version = os.path.join(dirname, 'vaex_gql_schema/_version.py')
version = imp.load_source('version', path_version)

name        = 'vaex-gql-schema'
author      = 'Maarten A. Breddels'
author_email= 'maartenbreddels@gmail.com'
license     = 'MIT'
version     = version.__version__
url         = 'https://www.github.com/gmcbretas/vaex-graphql'
install_requires_graphql = ['vaex-core>=4.1.0,<5', 'graphene>=3.0b7,<4', 'vaex>=4.1.0,<5', 'pandas>=1.2.4,<2']

setup(
    name=name,
    version=version,
    description='GraphQL support for accessing vaex DataFrame',
    url=url,
    author=author,
    author_email=author_email,
    install_requires=install_requires_graphql,
    license=license,
    packages=find_packages(exclude=['tests*']),
    zip_safe=False,
    entry_points={
        'vaex.dataframe.accessor': ['graphql = vaex_gql_schema:DataFrameAccessorGraphQL'],
    },
)
