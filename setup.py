import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='example_flask_app',
    version="0.1.0",
    author="Karthick Prabu",
    author_email="karthikprabu.cs@gmail.com",
    description="A small example flask app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stash.mtvi.com/projects/CDCNRY/repos/vmn-python-flask-canary-app",
    packages=setuptools.find_packages(),
    include_package_data= True,
    install_requires=[
        'flask',
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)