import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tmdb',
    version='0.1',
    packages=['tmdb'],
    include_package_data=True,
    license='BEER-WARE License',
    description='A small TMDB (themoviedatabase) API v3 wrapper for Django.',
    long_description=README,
    url='https://github.com/Merenon/django-tmdb',
    author='Dennis Detering',
    author_email='dennis@dety.eu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BEER-WARE License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)