import os
from setuptools import setup, find_packages

src_dir = os.path.dirname(__file__)

install_requires = [
    'stacker_blueprints>=1.0.7',
    'stacker',
]


if __name__ == '__main__':
    setup(
        name='wantit_org',
        version='0.0.1',
        author='Michael Barrett',
        author_email='loki77@gmail.com',
        url="https://github.com/phobologic/wantit.org",
        description='stacker config for wantit.org domain',
        install_requires=install_requires,
        packages=find_packages(),
    )
