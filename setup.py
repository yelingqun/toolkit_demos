import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toolkit",
    version="0.0.1",
    author="Lingqun Ye",
    author_email="yelingqun@gmail.com",
    description="Demos for bioinformatic & AI toolkits.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yelingqun/toolkit_demos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        'pandas>=1.3.1',
        'numpy>=1.19.5',
        'scipy>=1.4.1',
        'torchvision',
        'torch>=1.9.0'],
    python_requires=">=3.8",
)
