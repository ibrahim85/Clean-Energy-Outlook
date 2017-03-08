import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

ver_file = os.path.join('Clean-Energy-Outlook', 'version.py')
with open(ver_file) as f:
    exec(f.read())

opts = dict(name=NAME,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            install_requires=REQUIRES,
            requires=REQUIRES
            keywords=KEYWORDS)

if __name__ == '__main__':
    setup(**opts)
