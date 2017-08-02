
##### To read location
```
dx addressToRead
```

| da  | Reads from memory and displays it as ASCII text   |
| du  | Reads from memory and displays it as Unicode text  |
| dd  | Reads from memory and displays it as 32-bit double words   |

#####  e command is used in the same way to change memory values. 
```
ex addressToWrite dataToWrite
```
##### dwo command is used to dereference a 32-bit pointer and see the value at that location.

```
du dwo (esp+4)
```

##### *ln* command, which will list the closest symbol for a given memory address. This can be used to determine to which function a pointer is directed.
```
ln address
```

##### print data

bu address “.echo random_var_NAME;dc poi(esp+0c);gc”
