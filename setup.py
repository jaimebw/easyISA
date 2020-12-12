from setuptools import find_packages, setup

setup(
    name = 'easyISA-jaimebw',
    packages=find_packages(include=['easyISA']),
    version= '0.1.0',
    description='Easy implementation of ISA equations',
    author='Jaime Bowen',
    author_email="jaimebwv@gmail.com",
    install_requires = [],
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    url="https://github.com/jaimebw/easyISA",
    python_requires='>=3.6'
)
"""
setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    
  
    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
"""