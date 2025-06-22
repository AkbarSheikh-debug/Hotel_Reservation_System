from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Reservation_System",
    version="0.1",
    author="Akbar_Arif",
    packages=find_packages(),
    install_requires = requirements,
)