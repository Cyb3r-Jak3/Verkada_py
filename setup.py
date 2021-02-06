from setuptools import setup
from verkada_py import __version__


install_reqs = open("requirements.txt").readlines()

readme = open("README.md").read()

setup(
        name="verkada_py",
        version=__version__,
        description="Unofficial Verkada API Python Library",
        long_description=readme,
        author="Cyber_Jake",
        author_email="jake@jwhite.network",
        url="https://github.com/Cyb3r-Jak3/Verkada_py",
        project_urls={
            "Changelog": "https://github.com/Cyb3r-Jak3/Verkada_py/blob/main/CHANGELOG.md",
            "Issues": "https://github.com/Cyb3r-Jak3/Verkada_py/issues"
        },
        download_url="https://github.com/Cyb3r-Jak3/Verkada_py/releases/latest",
        packages=[
            "src"
        ],
        package_dir={"src": "src"},
        tests_require=[
            "bandit>=1.6.2",
            "black>=20.8b1",
            "coverage>=5.3",
            "flake8>=3.8.4",
            "pylint>=2.6.0",
            "pytest>=6.1.2",
            "pytest-cov>=2.10.1"
        ],
        install_requires=install_reqs,
        license="MPL 2.0",
        zip_safe=False,
        keywords="template, github",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
)
