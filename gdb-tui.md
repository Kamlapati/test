####Starting and Quitting
```
gdb [-tui] [-c core] [exename]	(Unix Command) Start gdb on an executable or standalone; specify "-tui" to start the TUI GUI; specify "-c" with a corefile name to see where a crash occurred
run [arg1] [arg2] [...]	Run the currently loaded program with the given command line arguments
quit	Exit the debugger
file exename	Load an executable file by name
```

####Breakpoints and Watchpoints
```
break location	Set a breakpoint at a location, line number, or file (e.g. "main", "5", or "hello.c:23")
watch expression	Break when a variable is written to
rwatch expression	Break when a variable is read from
awatch expression	Break when a variable is written to or read from
info break	Display breakpoint and watchpoint information and numbers
info watch	Same as info break
clear location	Clear a breakpoint from a location
delete num	Delete a breakpoint or watchpoint by number
```
####Stepping and Running
```
next	Run to the next line of this function
step	Step into the function on this line, if possible
stepi	Step a single assembly instruction
continue	Keep running from here
CTRL-C	Stop running, wherever you are
finish	Run until the end of the current function
advance location	Advance to a location, line number, or file (e.g. "somefunction", "5", or "hello.c:23")
jump location	Just like continue, except jump to a particular location first.
```

####Examining and Modifying Variables
```
display expression	Display the value of a variable or expression every step of the program—the expression must make sense in the current scope
info display	Show a list of expressions currently being displayed and their numbers
undisplay num	Stop showing an expression identified by its number (see info display)
print expression	Print the value of a variable or expression
printf formatstr expressionlist	Do some formatted output with printf() e.g. printf "i = %d, p = %s\n", i, p
set variable expression	Set a variable to value, e.g. set variable x=20
set (expression)	Works like set variable
```
####Window Commands
```
info win	Shows current window info
focus winname	Set focus to a particular window bby name ("SRC", "CMD", "ASM", or "REG") or by position ("next" or "prev")
fs	Alias for focus
layout type	Set the window layout ("src", "asm", "split", or "reg")
tui reg type	Set the register window layout ("general", "float", "system", or "next")
winheight val	Set the window height (either an absolute value, or a relative value prefaced with "+" or "-")
wh	Alias for winheight
set disassembly-flavor flavor	Set the look-and-feel of the disassembly. On Intel machines, valid flavors are intel and att
```

####Misc Commands
```
RETURN	Hit RETURN to repeat the last command
backtrace	Show the current stack
bt	Alias for backtrace
attach pid	Attach to an already-running process by its PID
info registers	Dump integer registers to screen
info all-registers	Dump all registers to screen
```


