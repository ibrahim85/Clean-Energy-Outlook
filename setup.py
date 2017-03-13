from setuptools import setup, find_packages

CLASSIFIERS=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Topic :: Scientific/Engineering",
    ]

LONG_DESCRIPTION ="""
Clean-Energy-Outlook
====================
Clean Energy Outlook is a software that reads in energy generation data from
1960 to 2014 of various states of the United States as well as other data like
GDP, climate, oil price, and other factors and predicts the renewable energy
generation of each state for the next 5 years. Software will be useful for
investors and policy makers in renewable energy. Investors in clean energy can
use this software to identify states where clean energy has high potential.
Policy makers can also use this software to develop clean energy policies for
different states.
To get started, please go to the repository README.
.. _README: https://github.com/uwkejia/Clean-Energy-Outlook/blob/master/README.md
License
=======
``Clean-Energy-Outlook`` is licensed under the terms of the MIT license. See the
file "LICENSE" for information on the history of this software, terms &
conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.
"""
NAME = 'ceo'
MAINTAINER = "Rahul Avadhoot"
MAINTAINER_EMAIL = "rahulavd@uw.edu"
AUTHOR = "Rahul Avadhoot"
AUTHOR_EMAIL = "rahulavd@uw.edu"
DESCRIPTION = ("Prediction of the clean energy market for the next "
                            "5 years for all the states in the US"),
LICENSE = "MIT",
URL = "https://github.com/uwkejia/Clean-Energy-Outlook.git",
DOWNLOAD_URL = "https://github.com/uwkejia/Clean-Energy-Outlook.git"
PLATFORMS = "OS Independent"
REQUIRES = ["numpy","pandas","sklearn"]

setup(name=NAME,
    maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=1.0,
            packages=find_packages(),
            install_requires=REQUIRES,
            requires=REQUIRES
)
