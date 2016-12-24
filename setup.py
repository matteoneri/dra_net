try:
    from setuptools import setup
except ImportError:
    from distutils.core import import setup

config = {
        'name': 'projectname'
        'version': '0.1',
        'description': 'My Project',
        'author': 'Matteo Neri',
        'author_email': 'nremtt@gmail.com',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
}

setup(**config)

