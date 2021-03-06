"""Setup for Crowdsource Hinter XBlock."""

from __future__ import absolute_import
import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='crowdsourcehinter-xblock',
    version='0.5',
    description='crowdsourcehinter XBlock',   # TODO: write a better description.
    packages=[
        'crowdsourcehinter',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'crowdsourcehinter = crowdsourcehinter:CrowdsourceHinter',
        ]
    },
    package_data=package_data("crowdsourcehinter", ["static", "public"]),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
