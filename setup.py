from setuptools import setup, find_packages

setup(
    name="randomness-validator",
    version="0.1.0",
    author="Davor Radic",
    author_email="info@emolio.nl",
    description="A library for validating randomness in numeric streams.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/emolionl/randomness-validator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["numpy"],  # Add other dependencies here
)
