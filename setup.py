from setuptools import setup, find_packages

setup(
    name='tscvki_montecarlo',
    version='1.1.0',
    description='Python package for doing science.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='lorenzoschena',
    python_requires='>=3.8',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    license='BSD-3-Clause',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
    ],
)