import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mnist-analysis",
    version="0.0.1",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="A simple analysis of mnist digit dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marskar/mnist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)