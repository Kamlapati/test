IDA 

1) File-> Load FILE -> FLIRT  (stripped statically linked executables)

2) Shortcuts
Shift+F2 (For IDC Console)



3) Functions:
------------------------------------------------------------------
Functions                    Return Value
------------------------------------------------------------------
idc.ScreenEA()          address of the focused location from "IDA VIEW" in decimal.
idc.SegName(address)    Find the segment name in which "address" is present.
idc.SegStart(address)   Find the Segment start address. "address" can be nay address within the segment.
idc.SegEnd(address)     Find the Segment end address. "address" can be nay address within the segment.
idc.NextSeg(address)    "address" can be nay address within the segment. Find the next segment address.
idc.SegByName(segname)  Find the address of the segment by th segment name (segname).
idautils.Segments()     Array containing address of all the segments present in the file


-----------------------------------------------------------------------
Functions                          Return Value
------------------------------------------------------------------------
idautils.Functions()                      Array containing start addresses of each function present in the code.
idautils.Functions(start_addr, end_addr)  Array containing start addresses of each function present in the given range.
idautils.FuncItems(address)               Get a iterator type (convert to list) of all addresses in a function.
idautils.CodeRefsTo(addr, flow)           return an iterator that can be looped through. addr is the address that we would like to have cross-ref erenced to
                                          The argument flow is a bool . It is used to specify to follow normal code flow or not.
idautils.DataRefsTo(addr)                 return an iterator of cross references address to data 
idautils.DataRefsFrom(addr)               return an iterator of cross references address from data
idautils.XrefsTo(addr,1)                  return an iterator of cross references address to the strings. 
                                          xref.type, idautils.XrefTypeName(xref.type),hex(xref.frm), hex(xref.to), xref.iscode
idc.GetFunctionName(address)              Returns function at "address". "address" can be anywhere within the function boundaries.
idc.NextFucntion(address)                 Returns th next function address
idc.PrevFunction(address)                 Returns the previous function address
idc.GetFunctionAttr(address, attr)        Get the attribute (atr=[FUNCATTR_START, FUNCATTR_END])
idc.GetFunctionFlags(address)             returns flag .(flag=[FUNC_NORET,FUNC_FAR,FUNC_LIB,FUNC_STATIC,FUNC_FRAME,
                                                         FUNC_USERFAR, FUNC_HIDDEN, FUNC_THUNK, FUNC_BOTTOMBP])
idc.NextHead(address)                     get the start of the next instruction
idc.PrevHead(ea)                          get the previous instruction address.
idc.NextAddr(ea)                          get the next address.
idc.PrevAddr(ea)                          get the previous address
idc.GetOpType(addr, n)                    get optype of operand n (starts with 0)
idc.GetOperandValue(addr,n)               get the value of operand n
idc.OpOff(addr, n, base)                  to convertthe operand to an offset. The first argument ea is the address, n is the operand index
                                          and base is the base address.
 idc.LocByName(func_name)		  get the address of the API "func_name"
idaapi.get_func(address)                  Class of the function.


----------------------------------------------------------
Functions                    Return Value
----------------------------------------------------------
idc.GetDisasm(address)  Get the diassmbled code at "address"
idc.GetMnem(address)    Get Mnemonic at "address"
idc.GetOpnd(address,n)  Get "n" operand at "address"



4) Tips

[find attributes and function name of the class]
python>dir(objecName)
dir(idaapi.cmd)


?????????       Finction Flags        ????????????????????????????????????????????
FUNC_NORET: This flag is used to identify a function that does not execute a return instruction. It’s
            internally represented as equal to 1.
FUNC_FAR: This flag is rarely seen unless reversing software that uses segmented memory. It is internally 
          represented as an integer of 2.
FUNC_USERFAR: This f lag is rarely seen and has very little documentation. HexRays describes the flag as
            "user has specified far-ness of the function”. It has an internal value of 32.
FUNC_LIB: This flag is used to find library code. It’ internally represented as an integer value of 4.
FUNC_STATIC: This flag is used to identify functions that were compiled as a static function.
FUNC_FRAME: This flag indicates the function uses a frame pointer ebp .
FUNC_BOTTOMBP: Similar to FUNC_FRAME this flag is used to track the frame pointer. It will identify functions
            that frame pointers is equal to the stack pointer.
FUNC_HIDDEN: Functions with the FUNC_HIDDEN flag means they are hidden and will need to be expanded
             to view.
FUNC_THUNK: This flag identifies functions that are thunk functions. They are simple functions that jump
            to another function.

????????????????????????????????????????????????????????????????????

???????????????       Operands       ????????????????????????????????????????????
o_void:  an instruction does not have any operands it will return 0.
o_reg:   If an operand is a general register it will return this type. This value is internally represented
         as 1.
o_mem:   If an operand is direct memory ref erence it will return this type. This value is internally
         represented as 2. e.g., ds:dword_A152B8
o_phrase: operand is returned if the operand consists of a base register and/or a index register.
          This value is internally represented as 3. eg, [edi+ecx]
o_displ:  This operand is returned if the operand consists of registers and a displacement value.  
          Internally it is represented as a value of 4. e.g., [edi+18h]
 o_imm:   Operands that are a value such as an integer of 0xC are of this type. Internally it is
          represented as 5.        
 o_far:   This operand is not very common when reversing x86 or x86_64 . It is used to f ind operands
          that are accessing immediate f ar addresses. It is represented internally as 6.
 o_near:  This operand is not very common when reversing x86 or x86_64 . It is used to f ind operands
          that are accessing immediate near addresses. It is represented internally as 7.         
????????????????????????????????????????????????????????????????????


????????????????   xref.type   ????????????????????????????
0 = 'Data_Unknown'
1 = 'Data_Offset'
2 = 'Data_Write'
3 = 'Data_Read'
4 = 'Data_Text'
5 = 'Data_Informational'
16 = 'Code_Far_Call'
17 = 'Code_Near_Call'
18 = 'Code_Far_Jump'
19 = 'Code_Near_Jump'
20 = 'Code_User'
21 = 'Ordinary_Flow'
???????????????????????????????????????????????????????



5) Example cods:
...........................................................
[Code to Find all the Segment:]
```
for seg in idautils.Segments():
    #print(seg)
    print (idc.SegName(seg), idc.SegStart(seg), idc.SegEnd(seg))
```
............................................................
[Find all the functions in the code]
```
for func in idautils.Functions():
    print(hex(func), idc.GetFunctionName(func))
```    
...............................................................    
[Code to disassemble of a function]
[Example-1]
```
dism_addr = list(idautils.FuncItems(here()))
for line in dism_addr:
    print hex(line), idc.GetDisasm(line)
```

[Example-2]
```
ea = here()     # return address at the focused location
start = idc.GetFunctionAttr(ea,FUNCATTR_START)     # find the start address
end = idc.GetFunctionAttr(ea,FUNCATTR_END)         # find the end address
cur_addr = start
while cur_addr <=end:
    print hex(cur_addr), idc.GetDisasm(cur_addr)  # print instrunction
    cur_addr = idc.NextHead(cur_addr,end)         # jump to next instruction
```    
...............................................................................    
[code to find properties of all the function]
```
for func in idautils.Functions():
   flags=idc.GetFunctionFlags(func)
   print (idc.GetFunctionName(func))
   if flags & FUNC_NORET:
      print "FUNC_NORET"
   if flags & FUNC_FAR:
      print "FUNC_FAR"
   if flags & FUNC_LIB:
      print "FUNC_LIB"
   if flags & FUNC_STATIC:
      print "FUNC_STATIC"
   if flags & FUNC_FRAME:
      print "FUNC_FRAME"
   if flags & FUNC_USERFAR:
      print "FUNC_USERFAR"
   if flags & FUNC_HIDDEN:
      print "FUNC_HIDDEN"
   if flags & FUNC_THUNK:
      print "FUNC_THUNK"
   if flags & FUNC_BOTTOMBP:
      print "FUNC_BOTTOMBP"
```

[Find dynamic calls addresses]
```
import idautils
for func in idautils.Functions():
    flags = idc.GetFunctionFlags(func)
    if flags & FUNC_LIB or flags & FUNC_THUNK:
        continue
    dism_addr = list(idautils.FuncItems(func))
    for line in dism_addr:
        m = idc.GetMnem(line)
        if m == 'call' or m == 'jmp':
            op = idc.GetOpType(line,0)
            if op == o_reg:
                print "0x%x %s"%(line, idc.GetDisasm(line)) 
 ```   
[Change offset addresst to string]
```
min = MinEA()
max = MaxEA()
def change_offset_addr_to_name():
	for func in idautils.Functions():
		flags = idc.GetFunctionFlags(func)
		if flags & FUNC_LIB or flags & FUNC_THUNK:
			continue
		dism_addr = list(idautils.FuncItems(func))
		for cur_addr in dism_addr:
			if idc.GetOpType(cur_addr,0) == 5 and (min < idc.GetOperandValue(cur_addr,0)< max):  # o_imm=5
				idc.OpOff(cur_addr,0,0)
			if idc.GetOpType(cur_addr,1) == 5 and (min < idc.GetOperandValue(cur_addr,1)< max):  # o_imm=5
				idc.OpOff(cur_addr,1,0)
```				
[write bytes]
```
f = open('c:\\users\\filPath', 'wb').write(GetManyBytes(0x6529B0, 0x1f8))
```
[finde Xref of Functions]
```
from idaapi import *

dng_func = ["strcpy","fun_404050_theMainEvent","strncpy"]

for f in dng_func:
   addr = LocByName(f)
   if addr != BADADDR:
      c_refs = CodeRefsTo(addr,0)
      print "Cross_Refs"
      print "----------"
      for x in c_refs:
         print ("%08x" %x)
         SetColor(x,CIC_ITEM,0xf52fff)
```

