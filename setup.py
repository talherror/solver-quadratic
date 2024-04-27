from setuptools import setup, find_packages

setup(
    name='quadratic_solver',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'quadratic_solver = quadratic_solver.__main__:main'
        ]
    },
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.21.0',
    ],
  
)
