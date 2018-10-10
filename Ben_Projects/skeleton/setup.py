try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Benjamin Liu',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'bliu7@foxmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
