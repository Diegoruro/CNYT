# Operations of complex numbers and complex space.

This is a repository for a library that has the functions to complete basic operations with complex numbers and complex spaces, developed with python.
The following functions are:
### Complex Numbers
- Basic operations of complex numbers(Addition, subtraction, Multiplication,Division)
- Module.
- Conjugation.
- Conversion from polar to cartesian.
- Conversion from cartesian to polar.
- Return of the phase.
### Complex Vectors
- Additions between vectors.
- Additive inverse of a vector.
- Multiplication of a scalar (Complex / Real) by a vector.
- Norm of a vector.
- Distance between Vectors.
### Complex Matrix
- Addition between matrix.
- Additive inverse of a matrix.
- Multiplication of a scalar (Complex / Real) by a matrix.
- Product between matrix.
- Verify that a matrix is unitary.
- Verify that a matrix is hermitian.
### Functions for complex Matrix/Vectors
- Transpose.
- Conjugated.
- Adjoint.
- Action.
- Inner product.
- Tensor product.
## Getting Started

In order to use the following functions you´ll need to use tuples instead of the normal structure of the complex numbers the following example will guide you on how to convert normal expression into tuples.
```
3+2i->( real, imaginary )
(3,2)
```
So in order to use the function you´ll code:
### For complex Numbers
```
function_name((a,b),(c,d)) (for operations between complex numbers)
function_name((a,b))(for operations whit complex numbers)
```
Here are some examples:
```
suma((1,2),(3,4))
(4,6)
modulo((3,4))
5
```
### For complex vectors

```
function_name([[(a,b),(c,d),(ef)]],[[(a1,b1),(c1,d1),(e1,f1)]]) (for operations between complex vectors)
function_name((a,b),[[(a1,b1),(c1,d1),(e1,f1)]])(for operations whit complex vectors and scalars)
function_name([[(a1,b1),(c1,d1),(e1,f1)]])(for operations whit complex vectors)
```
Here are some examples:
```
Addition_vect([(1, 0), (2, 0)], [(1, 2), (3, 4)])
[(2, 2), (5, 4)]
norm([(4, 2), (2, 6), (6, 3), (7, 8)])
14.76
```
### For complex matrix

```
function_name([[(a,b),(c,d),(ef)]],[[(a1,b1),(c1,d1),(e1,f1)]]) (for operations between complex matrix)
function_name((a,b),[[(a1,b1),(c1,d1),(e1,f1)]])(for operations whit complex matrix and scalars)
function_name([[(a1,b1),(c1,d1),(e1,f1)]])(for operations whit complex matrix)
```
Here are some examples:
```
suma_mat([[(1, 0), (2, 0)], [(3, 4), (4, 5)]], [[(4, 5), (1, 3)], [(6, 7), (8, 9)]])
[[(5, 5), (3, 3)], [(9, 11), (12, 14)]]
herm([[(7, 0), (6, 5)], [(6, -5), (-3, 0)]])
True
```
### For functions with complex matrix/vectors

```
function_name([[(a,b),(c,d),(ef)]],[[(a1,b1),(c1,d1),(e1,f1)]]) (for operations between complex matrix and vectors)
function_name([[(a1,b1),(c1,d1),(e1,f1)]])(for operations whit complex matrix/vectors)
```
Here are some examples:
```
Action([[(1, 0), (2, 0)], [(3, 4), (4, 5)]], [[(4, 5)], [(1, 3)]])
[[(6, 11)], [(-19, 48)]]
conjugada_mat([[(1, 0), (2, 0)], [(3, 4), (4, 3)]]
[[(1, 0), (2, 0)], [(3, -4), (4, -3)]]
```
For more examples use the test file [Pruebas2.py](https://github.com/Diegoruro/ComplexCNYT/blob/master/Pruebas2.py).
## Prerequisites
- [Python](https://www.python.org/) version 3.7 or higher
- [Git](https://git-scm.com/)
- [pyCharm](https://www.jetbrains.com/es-es/pycharm/)

To use this library you need python, at least 3.7 version, if you already have python installed, to check if it is 3.7 or higher use the following command in cmd.

```
python --version
```

### Installing

These are the instructions to use the library.
follow the step by step to install the library.

copy the link of the repository with the following steps:

 - Get into the main git of the repository.
![](Images/laser.PNG)
 - Copy the URL of the repository by clicking the code button and copy button.
![](Images/Example_2.png)
 - Create a folder where you want to save the repository and open it.

![](Images/folder.PNG)
 - Right click in the folder and use the option "Git Bash Here".
![](Images/Git_bash.PNG)
 - Use the following command to copy the repository with the URL you already copy from Github.

```
git clone https://github.com/Diegoruro/ComplexCNYT.git
```
![](Images/git_clone.PNG)
 - Then the repository will be in your new folder ready to use it.
![](Images/cloned.PNG)

## Running the tests

To run the test of the library you´ll need to open the following file.
```
Pruebas2.py
```
It will show you some test of every function of the library.

The following steps will show you how to run it with [pyCharm](https://www.jetbrains.com/es-es/pycharm/)

- Open the file [pruebas.py](https://github.com/Diegoruro/ComplexCNYT/blob/master/Pruebas.py) with [pyCharm](https://www.jetbrains.com/es-es/pycharm/).

![](Images/abrir_pruebas.PNG)
- Then look for the line number 369, right click on the green play button and click on Run option
![](Images/run_2.PNG)

That´s all.
### Files
- [New_complejos.py](https://github.com/Diegoruro/ComplexCNYT/blob/master/new_complejos.py)
- [Pruebas2.py](https://github.com/Diegoruro/ComplexCNYT/blob/master/Pruebas2.py)

## Folders
- [Images](https://github.com/Diegoruro/ComplexCNYT/tree/master/Images): contains the images used in the Readme file.

## Built With

* [Python 3.8](https://www.python.org/) - As the main programming language.


## Authors

* **Diego Ruiz Rojas** - *main work* - [github](https://github.com/Diegoruro)

student at:[Escuela Colombiana de Ingeniería Julio Garavito](https://www.escuelaing.edu.co/es/)
