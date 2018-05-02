from setuptools import setup

setup(
    author='Adrian Sadłocha',
    description='Shrug emoticon printer',
    entry_points={'console_scripts': ['shrug = shrug.cli:main']},
    long_description='Shrug emoticon printer',
    name='shrug',
    packages=['shrug'],
    tests_require=['pytest', 'pytest-runner'],
    url='https://github.com/Necior/shrug',
    version='0.1.1',
)
