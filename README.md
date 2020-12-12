# Easy I.S.A 
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/python/black)

## Introduction

This library is an implementation of the International Standard Atmoshphere equations.
The main purpose of this library is to be simple, and to be based only on in-python modules.

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

The usage is simple. For example, I want to know the preasuer at 9.8km altitude:

´´´python

from easyISA import equations as eq  

p = eq.presure.meter(9.8e3)

print(p)

´´´

asdasd
## References
[The International Standard Atmoshphere (ISA)](http://fisicaatmo.at.fcen.uba.ar/practicas/ISAweb.pdf)