#!/usr/bin/env python3
import os
from setuptools import find_packages, setup

VERSION = '1.0.1'

INSTALL_REQUIRES = (
    [
        'mujoco >= 2.2.0',
        'glfw >= 2.5.0',
        'imageio'
    ]
)

setup(
    name='mujoco-python-viewer',
    version=VERSION,
    author='Jack Xu',
    author_email='projectbyjx@gmail.com',
    url='https://github.com/jaku-jaku/jx-mujoco-python-viewer',
    description='Interactive renderer for MuJoCo Python',
    long_description='Interactive renderer for MuJoCo Python, inspired by mujoco-python-viewer and mujoco-py',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    zip_safe=False,
)
