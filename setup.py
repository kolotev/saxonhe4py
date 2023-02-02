#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.install import install
import urllib.request
import zipfile
import pathlib

import os, tempfile


def download_saxon():
    saxon_url = (
        "https://sourceforge.net/projects/saxon/files/Saxon-HE/11/Java/SaxonHE11-4J.zip/download"
    )
    saxon_file = "/tmp/saxonhe.zip"
    saxon_target = "src/saxon_he"
    if not pathlib.Path(saxon_target).exists():
        with tempfile.NamedTemporaryFile(suffix=".zip", prefix="saxonhe") as saxon_file:
            urllib.request.urlretrieve(saxon_url, saxon_file.name)
            with zipfile.ZipFile(saxon_file.name, "r") as zip:
                zip.extractall(saxon_target)


download_saxon()

setup(
    name="saxonhe4py",
    maintainer="Andrei Kolotev",
    maintainer_email="kolotev@ncbi.nlm.nih.gov",
    setup_requires=[
        "setuptools_scm[toml]>=6.2",
        "tox-setuptools",
    ],
    tests_require=["tox>=3.3,<4"],
)
# This file minimally duplicates what is defined in pyproject.toml
# to satisfy NCBI teamcity configs' requirements.
