from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-plotly-events2",
    version="0.0.7",
    author="Chiyun Lee",
    author_email="chiyun.alberto.lee@gmail.com",
    description="Reviving the Streamlit community package, streamlit-plotly-events",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malariagen/streamlit-plotly-events2",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.10",
    install_requires=[
        "streamlit >= 1.36",
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",
            "playwright==1.39.0",
            "requests==2.31.0",
            "pytest-playwright-snapshot==1.0",
            "pytest-rerunfailures==12.0",
        ]
    }
)
