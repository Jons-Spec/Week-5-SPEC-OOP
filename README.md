# Week 5 SPEC singleton and factory design patterens

## How to run the program

To run the program you need the following:

- Clone this repository

- A version of Python installed, I used version 3.9.0

- A version of Pip installed, I used version 20.4
- A MySQL database

Create a python virtual enviroment in the cloned repository using the following command in Windows PowerShell:

```
Windows: python -m venv venv
```

If you haven't configured a python path run:

```
Windows: C:\Users\Name\AppData\Local\Programs\Python\Python310\python -m venv venv
```

To run the virtual enviroment run:

```
Windows: venv\Scripts\activate
```

install all the required libaries run:

```
Windows: pip install -r requirements.txt
```

To run the program run:

```
python main.py
```

## How it works

The programs creates a connection to a MySQL database and
then ask the use for inputs on the clothes you want to be created.

Inputs such as:

- type pants or tshirt
- size
- color
- style
- design
