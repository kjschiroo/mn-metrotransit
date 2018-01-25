from setuptools import setup

setup(
    name='mn-metrotransit',
    version='0.1',
    description='A thin client for querying the Twin Cities Metro Transit API',

    author='Kevin Schiroo',
    author_email='kjschiroo@gmail.com',
    license='MIT',

    packages=['mn_metrotransit'],
    install_requires=['requests'],

    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
