#Sample program

#####create a new repository on the command line
```
echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Kamlapati/test.git
git push -u origin master
```

##### push an existing repository from the command line
```
git remote add origin https://github.com/Kamlapati/test.git
git push -u origin master
```
### find the version of python module 
$ pip freeze | grep module_name
lxml==2.3
$ python -c "import module_name; print module_name.__version__"
