#PMA

Packed and obfuscated code will often include at least the functions LoadLibrary and GetProcAddress, which are used to load and gain access to additional functions.

##### push an existing repository from the command line
```
git remote add origin https://github.com/Kamlapati/test.git
git push -u origin master
```
### find the version of python module 
```
$ pip freeze | grep module_name
lxml==2.3
$ python -c "import module_name; print module_name.__version__"
```
