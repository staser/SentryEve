import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sentry-eve',
    version='0.0.0.1c1',
    author="Standart AG, LLC",
    author_email="it@standart.lv",
    description="Eve Sentry support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/staser/SentryEve",
    packages=setuptools.find_packages(),
    install_requires=[
        'eve', 'raven[flask]'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
