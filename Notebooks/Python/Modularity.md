# Modules

#### Modules are single python file that can be imported and used inside another file.

### import
We use `import` statement to import a python file into another python file, when the module will be imported, he will be ran. 
Inside the other python file, all the functions and classes of the module can be accessed by `module_name.function_name`.

For example, to import a file called `my_program.py`, write `import my_program` in your code.  

Convention says you should write all your import statements on the top of the page.

### from
We can import specific functions from a module with the from statement.

When using from, there is no need to call them with module_name.function_name syntax, they are directly imported and we can call them with function_name only.

Example:  
`from mymodule import myfunction`

### as

We can use aliases to change the name of the module inside the program.
Example:  
`import mymodule as mod`


### pip
Pip is a python packages manager, it can download and install packages alone, it take them automatically from pypi.org, but can also install a downloaded package. You can use it from the terminal.

### Package
A package is made up of multiple python files, and can even include librairies in C or C++, it's an entier folder.

### \_\_init__.py
A lot of time when looking at the structure of the packages, you'll see a file called `__init__.py`, this is the old syntax to create python packages, it's not necessary today but most of the packages are built like this. This file is executed when the package is loaded.  
Every module in the package can be loaded alone by using `from my_package import my_module`
