from setuptools import setup, find_packages
from cpc2project import __version__ as version

VERSION = version
DESCRIPTION = 'Create RetrovirtualMachine html cpc'

setup(
    name='cpc2project',
    version=VERSION,
    author="Destroyer",
    author_email="<destroyer.dcf@gmail.com>",
    description=DESCRIPTION,
    license="GPL",
    packages=find_packages(),
    install_requires=[
        'click',
        'jinja2'
    ],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',   
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'cpc2project= cpc2project.__main__:main',
        ]
    }
)