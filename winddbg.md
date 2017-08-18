


##### To read location
```
dx addressToRead
```

| da  | Reads from memory and displays it as ASCII text   |
| du  | Reads from memory and displays it as Unicode text  |
| dd  | Reads from memory and displays it as 32-bit double words   |

#####  *e* command is used in the same way to change memory values. 
```
ex addressToWrite dataToWrite
```
##### *dwo* command is used to dereference a 32-bit pointer and see the value at that location.

```
du dwo (esp+4)
```

##### *ln* command, which will list the closest symbol for a given memory address. This can be used to determine to which function a pointer is directed.
```
ln address
```


##### find the driver object with the *!drvobj* command.
```
ModLoad: f7b0d000 f7b0e780   FileWriter.sys
> !drvobj FileWriter
```
Sometimes the driver object will have a different name or !drvobj will fail. As an alternative, you can browse the driver objects with the !object \Driver command. This command lists all the objects in the \Driver namespace, 

##### *u* command to check the instructrions
```
> u address
```

##### print data

bu address “.echo random_var_NAME;dc poi(esp+0c);gc”


#### Kernel Debugging net setting
```
bcdedit /dbgsettings net hostip:1.1.1.1 port:50000 key:1.12.3.1
bcedit /set busparams num.num.num
```

##### To find structure of heap, if page heap is enable 
```
dt _DPH_BLOCK_INFORMATION  
```

