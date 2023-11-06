import setuptools
with open("README.md",'r',encoding="utf-8") as f:
    long_description = f.read()
__version__ = "0.0.0"
REPO_NAME = "CementStrengthPrediction"
AUTHOR_NAME = "Tilakakasapu"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "tilak57233@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for ml app",
    long_description = long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    )