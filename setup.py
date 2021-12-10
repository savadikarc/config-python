import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configpy",
    version="0.0.1",
    author="Chinmay Savadikar",
    author_email="savadikarc@gmail.com",
    description="A wrapper to access file-based config as Python class attributes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/savadikarc/config-python",
    install_requires=['pyyaml>=5.4'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)