# Installing python

Download python from the official site, and run the Wizard until the end.

    For windows users: be sure to check "Add python to PATH"


# The python interactive shell (IDLE)

Python is an interpreted language, it means he can run code line by line. Python interactive shell allows you to run python code, line by line. 

To open it, open a terminal, and type "python" (for windows users) | "python3" (for mac/linux users).

You should see `>>>` at the beginning of the line, it means you entered the python shell.

> Developers use the python shell to test pieces of code they aren't sure about

You can try it, type some python code and hit `<Enter>`, for example:

```python
>>> 3+8
11
>>> 4*4
16
```

You can try every operator: `+`, `-`, `*`, `/` .

There are also some special operators: 

- `//` will divide and remove the floating point

  ```python
  >>> 10 / 3
  3.3333
  >>> 10 // 3
  3
  ```

- `%` (modulo) will return the rest of the division

  ```python
  >>> 10 % 3 
  1
  ```




#### Using python files

You can also store your code in a python file. 

A python file is a text file with the `.py` extension.

To run a file called `my_file.py`, enter the terminal, navigate to the file's directory and run:

```bash
$python3 my_file.py
```

#### Comments
Python ignore all the lines that start with `#`, it's called a comment, use it to document your code.
