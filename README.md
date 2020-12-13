```
                             .___  _________   _____   
  ____ _____    _________.__.|   |/   _____/  /  _  \  
_/ __ \\__  \  /  ___<   |  ||   |\_____  \  /  /_\  \ 
\  ___/ / __ \_\___ \ \___  ||   |/        \/    |    \
 \___  >____  /____  >/ ____||___/_______  /\____|__  /
     \/     \/     \/ \/                 \/         \/ 
```
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/python/black)  
[![Build Status](https://travis-ci.org/jaimebw/easyISA.svg?branch=main)](https://travis-ci.org/jaimebw/easyISA)

## Introduction

This library is an implementation of the International Standard Atmoshphere equations.
The main purpose of this library is to be simple,to be based only on in-python modules and to help me learn how to deploy libraries.

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
* [Representation of the atmosphere from the troposhphere to statosphere](https://github.com/jaimebw/easyISA/blob/main/examples/representation_atmosphere.ipynb)

## References
[The International Standard Atmoshphere (ISA)](http://fisicaatmo.at.fcen.uba.ar/practicas/ISAweb.pdf)