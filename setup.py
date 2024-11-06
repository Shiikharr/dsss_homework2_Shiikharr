from setuptools import setup, find_packages

setup(
    name="math-quiz",
    version="0.1",  # Version number
    description="A simple math quiz game in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Shikhar Srivastava",
    author_email="shikhar.sri111@gmail.com",
    url="https://github.com/Shiikharr/dsss_homework2_Shiikharr.git",
    packages=find_packages(),  # Automatically find all packages in the directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
    test_suite='tests', 
)
