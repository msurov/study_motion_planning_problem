from setuptools import setup, find_packages

setup(
    version = '0.0.1',
    name = 'cart-double-pendulum',
    author = 'Maksim Surov',
    author_email = 'surov.m.o@gmail.com',
    install_requires = [
        'sympy',
        'numpy',
        'matplotlib',
        'scipy',
        'ipython',
        'PyQT6',
        'ipykernel'
    ],
    package_dir = {
        '': 'src'
    },
    packages = find_packages(where='src')
)
