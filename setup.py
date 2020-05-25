from setuptools import setup

setup(
    name='Piglax',
    version='1.0',
    long_description=__doc__,
    packages=['piglax'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
