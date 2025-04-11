from setuptools import setup, find_packages

setup(
    name="tagon",
    version="0.1.0",
    description="O framework web reativo 100% em Python",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    url="https://github.com/seu-usuario/tagon",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "tagon=tagon.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="web, framework, python, reactive",
    python_requires=">=3.7",
)