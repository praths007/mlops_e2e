from setuptools import find_packages, setup


def find_packages(file_path):
    return list(open(file_path, 'r'))


setup(
    name='mlops_e2e',
    version='0.01',
    requires=find_packages('requirements.txt'),
    author='praths'
)
