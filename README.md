# 2019-2020 SDP Team 32 Project
Welcome to our Senior Design Project. This repository is is the result of the joint contributions from John Gauthier, Sam Kasbawala, Mickey Mannella, and Ryan Miller. The goal of this project is to use baseball statistics to come up with a predictive model in order to predict the outcomes of games. We will first start with Machine Learning techniques, using learning models such as Support Vector Machines (SVM), Random Forest, and a couple of others. Hopefully, we will be able to extend this idea and implement something similar using neural networks and deep learning. Currently, the project is in it's developmental and initial stages.


## Table of Contents:
------
- [Installation](#installation)  
    - [Download Python](#download-python)
    - [Creating a Virtual Environment](#creating-a-virtual-environment)
    - [Using `pip`](#using-pip)


## Installation  
[Back to top](#table-of-contents)

------
In this project, we will be utilizing Jupyter Notebooks in order to visualize data and also use Scikit Learn's built in functionality. Jupyter Notebooks allows us to write supporting text that explains our thought process and will be able to provide explanation for the code. We will also be using pandas and numpy. These are all typical python libraries that used in many data science projects. Before we install the required dependencies, it's a good idea to create a new virtual environment. *DISCLAIMER: This project uses Python 3.8, but any Python version above 3.5 should work*


### Download Python
[Back to top](#table-of-contents)

------
You can download Python from [python.org](https://www.python.org/downloads/). Follow the installation for you system (Linux, Windows, Mac). `pip` should be installed when you install python. If it isn't then you should install it. It's easy to find tutorials online on how to do this. Once it's installed, make sure you have the latets version of pip installed by issuing the following command
```
$ python3 -m pip install --upgrade pip
```


### Creating a Virtual Environment
[Back to top](#table-of-contents)

------
Next, it's a good idea to make a new virtual environment. This is a good idea incase you have many projects that might have conflicting requirements. We will use pip to install `virtualenv`
```
$ python3 -m pip install virtualenv
```
Next, we have to create the virtual environment itself
```
$ python3 -m virtualenv env
```
You can name the environment whatever you would like, it does not need to be "env". Now we must activate the virtual environment. On Linux/MacOS, we can activate the environment by typing the following:
```
$ source ./env/bin/activate
```
On Windows, we issue the following command:
```
$ .\env\Scripts\activate
```


### Using `pip`
[Back to top](#table-of-contents)

------
Last step, now we have to actually install all of the dependencies. These are the items that this repository needs in order for it work and run on your system. In this repo, you will see the `requirements.txt` file. This contains all of the packages that we need and their version number.
```
$ pip3 install --upgrade -r requirements.txt
```
Now you are done! In order to open the Jupyter Notebook(s), you need to start the jupyter notebook server. You can do this by typing
```
$ jupyter notebook
```
It should open the server in your default browser. Now you can play around with the code and try things out for yourself.