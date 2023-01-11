import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

with open("requirements.txt") as f:
    requireds = f.read().splitlines()

setup(
    name="docscan",
    version="1.0.5",
    description="This is a document scanner",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielgatis/docscan",
    author="Daniel Gatis",
    author_email="danielgatis@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="document, scanner, opencv",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.5, <4",
    install_requires=requireds,
    entry_points={
        "console_scripts": [
            "docscan=docscan.cmd.cli:main",
            "docscan-server=docscan.cmd.server:main",
        ],
    },
)
