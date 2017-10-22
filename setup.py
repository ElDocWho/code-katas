from setuptools import setup

setup(
    name='code-katas',
    author='Fortunato Maycotte',
    author_email='fortunato.maycotte@gmail.com',
    description='Codewars solutions',
    package_dir={'': 'src'},
    py_modules=['average_scores', 'convert_boolean', 'counting_sheep', 'descending_order'],
    install_requires=[],
    extras_require={
        'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox', 'Faker']
    },
)
