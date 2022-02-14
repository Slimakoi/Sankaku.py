from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name = "Sankaku.py",
    version = "1.0.0",
    url = "https://github.com/Slimakoi/Sankaku.py",
    download_url = "https://github.com/Slimakoi/Sankaku.py/tarball/master",
    license = "MIT",
    author = "Slimakoi",
    author_email = "slimeytoficial@gmail.com",
    description = "A library to create Sankaku Complex bots.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [
        "sankaku",
        "sankaku-complex",
        "sankaku-py",
        "sankaku-bot",
        "api",
        "python",
        "python3",
        "python3.x",
        "slimakoi",
        "official"
    ],
    install_requires = [
        "setuptools",
        "requests",
        "six"
    ],
    setup_requires = [
        "wheel"
    ],
    packages = find_packages()
)
