from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pdf-restaurant-extractor",
    version="1.0.0",
    author="Yasir Salman",
    author_email="yasirsmayet496@example.com",
    description="Extract restaurant information from PDF files using text extraction and OCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yasir-Salman/pdf-restaurant-extractor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pdf-restaurant-extractor=pdf_restaurant_extractor:main",
        ],
    },
    keywords="pdf, ocr, restaurant, text extraction, receipt processing",
    project_urls={
        "Bug Reports": "https://github.com/Yasir-Salman/pdf-restaurant-extractor/issues",
        "Source": "https://github.com/Yasir-Salman/pdf-restaurant-extractor",
    },
)
