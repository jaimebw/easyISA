# Easy I.S.A 
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/python/black)

## Introduction

This library is an implementation of the International Standard Atmoshphere equations.
The main purpose of this library is to be simple, and to be based only on in-python modules. And for myself on learning how to deploy working libraries.

## TO-DO List

* [X] Create library
* [X] Create tests
* [X] Upload to [Pypi](https://packaging.python.org/tutorials/packaging-projects/)
* [ ]Create examples of use
* [ ] Maybe implement getting data as .csv or .txt?
# Installation and how to use
To install you just need to write: 

```
pip install easyISA 
```  

The usage is simple. For example, if I wanted to know the preasure at an altitude of 9.8km, I'd type:

```python
from easyISA.equations import pressure 
p = pressure.meter(9.8e3)
print(p)
```
More examples inside the example directory:
* [Representation of the atmosphere from the troposhphere to statosphere]()

asdasd
## References
[The International Standard Atmoshphere (ISA)](http://fisicaatmo.at.fcen.uba.ar/practicas/ISAweb.pdf)