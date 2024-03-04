# coding: utf-8

"""
    ProductSearch Api

    ProductSearch Api  # noqa: E501

    OpenAPI spec version: v4
    Contact: dl_Agile_Team_B2B_API@digikey.com
    Generated by: https://github.com/dk_api-api/dk_api-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dk_api-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="ProductSearch Api",
    author_email="dl_Agile_Team_B2B_API@digikey.com",
    url="",
    keywords=["dk_api", "ProductSearch Api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ProductSearch Api  # noqa: E501
    """
)
