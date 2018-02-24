from setuptools import setup, find_packages
import faker_cloud


def read_file(name):
    with open(name) as fd:
        return fd.read()


setup(
    name="faker-cloud",
    version=faker_cloud.__version__,
    author=faker_cloud.__author__,
    author_email=faker_cloud.__email__,
    description=faker_cloud.__doc__,
    url=faker_cloud.__url__,
    keywords=faker_cloud.__keywords__,
    license=faker_cloud.__license__,
    py_modules=['faker_cloud'],
    packages=find_packages(),
    install_requires=read_file('requirements.txt').splitlines(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=read_file('README.rst'),
)
