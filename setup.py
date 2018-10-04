import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skippy",
    version="0.1.0",
    author="Martin Skarzynski",
    author_email="marskar@gmail.com",
    description="Simplified analysis of sklearn datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marskar/skippy",
    packages=['skippy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'skippy = skippy.__main__:main'
        ]
    },
    install_requires=[
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ]
)
