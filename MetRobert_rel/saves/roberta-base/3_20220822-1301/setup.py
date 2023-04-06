from setuptools import setup, find_packages

setup(
    name='MetRubert',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'torch>=1.6.0',
        'transformers>=4.2.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3.0',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
