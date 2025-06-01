from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="raycaster-engine",
    version="0.1.0",
    description="A modular, developer-friendly Python raycasting engine template for retro-style shooters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Elemental Publishing",
    author_email="houser2388@gmail.com",
    url="https://github.com/ElementalPublishing/Raycaster",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    entry_points={
        "console_scripts": [
            "raycaster=raycaster.main:main"
        ]
    },
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Games/Entertainment",
    ],
    project_urls={
        "Source": "https://github.com/ElementalPublishing/Raycaster",
        "Tracker": "https://github.com/ElementalPublishing/Raycaster/issues",
    },
)