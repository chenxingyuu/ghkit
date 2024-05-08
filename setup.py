from os import path

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# 读取版本号
__version__ = None

try:
    pkg_name = "ghutils"
    lib_info_py = path.join(pkg_name, "__init__.py")
    lib_info_content = open(lib_info_py, "r", encoding="utf8").readlines()
    version_line = [line.strip() for line in lib_info_content if line.startswith("__version__")][0]
    exec(version_line)  # produce __version__
except FileNotFoundError:
    __version__ = "0.0.1"

setup(
    name="ghutils",
    author="xingxing",
    author_email="chenxingyu@ndnu.edu.cn",
    version=__version__,
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "loguru~=0.6.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
