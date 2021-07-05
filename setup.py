from setuptools import setup, find_packages

setup(
    name="pottersay",
    version="0.1.4",
    description="Generate a random Harry Potter quote in ASCII art.",
    url="http://github.com/defcon-007/pottersay",
    author="Ayush Goyal",
    author_email="ayushgoyal.iitkgp@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points=dict(console_scripts=["pottersay=src.main:generate_quote"]),
)
