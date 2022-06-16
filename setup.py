from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sendwecom',
    version='0.0.3',
    packages=setuptools.find_packages(),
    url='https://github.com/hukongyi/SendWecom',
    license='MIT',
    author='Hu Kongyi',
    author_email='hukongyi@ihep.ac.cn',
    description='A small example package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
