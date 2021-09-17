import os
from setuptools import setup, find_packages


version = "0.1"


install_requires = [
    'fanstatic',
    'reiter.application',
    'uvcreha',
]

test_requires = [
    'pytest',
]


setup(
    name='reha.siguv_theme',
    version=version,
    author='Souheil CHELFOUH',
    author_email='trollfot@gmail.com',
    description='SIGUV theme for UVCReha',
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.rst")).read()
    ),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python:: 3 :: Only',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['reha',],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
    entry_points={
        "fanstatic.libraries": [
            "reha.siguv_theme = reha.siguv_theme.resources:library",
        ],
    }
)
