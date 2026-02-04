from setuptools import find_packages, setup

setup(
    name="clinicalrag",
    version="0.1.0",
    author="Nitesh Raghuwanshi",
    author_email="niteshraghuwanshi68@gmail.com",
    description="Evidence-grounded clinical RAG system for medical QA",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[],
)
