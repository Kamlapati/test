 
#### Linked Librariers

 1. runtime linking is commonly used in malware
 2. LoadLibrary, GetProcAddress, LdrGetProcAddress, and LdrLoadDll Microsoft Windows functions allow programmers to import linked functions not listed in a program’s file header.
 
 
 ### Tools
 
| Tools                      | Descriptions                                     | 
| -------------------------- |:------------------------------------------------:| 
|Dependency Walker           | Dynamically linked functions                                  | 
|ApateDNS                    | Faking Network                                   |
|INetSim                     | To simulating common Internet services (Linux)   |
|

 ##### Run DLL
 
 ```
 rundll32.exe DLLname, Export arguments
 ```
 The Export value must be a function name or ordinal selected from the exported function table in the DLL. 
 ```
 rundll32.exe rip.dll, Install
 rundll32.exe xyzzy.dll, #5
 ```
 
###### net start command is used to start a service on a Windows system.
 ```
 net start ServiceName
 ```
#### OPcode
    * pusha * pushes the 16-bit registers on the stack in the following order: AX, CX, DX, BX, SP, BP, SI, DI.
    * pushad * pushes the 32-bit registers on the stack in the following order: EAX, ECX, EDX, EBX, ESP, EBP, ESI, EDI.
    
 ```
 jz loc : Jump to specified location if ZF = 1.

jnz loc : Jump to specified location if ZF = 0.

je loc : Same as jz, but commonly used after a cmp instruction. Jump will occur if the destination operand equals the source operand.

jne loc : Same as jnz, but commonly used after a cmp. Jump will occur if the destination operand is not equal to the source operand.

jg loc : Performs signed comparison jump after a cmp if the destination operand is greater than the source operand.

jge loc  : Performs signed comparison jump after a cmp if the destination operand is greater than or equal to the source operand.

ja loc : Same as jg, but an unsigned comparison is performed.

jae loc :Same as jge, but an unsigned comparison is performed.

jl loc : Performs signed comparison jump after a cmp if the destination operand is less than the source operand.

jle loc : Performs signed comparison jump after a cmp if the destination operand is less than or equal to the source operand.

jb loc : Same as jl, but an unsigned comparison is performed.

jbe loc : Same as jle, but an unsigned comparison is performed.

jo loc :Jump if the previous instruction set the overflow flag (OF = 1).

js loc : Jump if the sign flag is set (SF = 1).

jecxz loc : Jump to location if ECX = 0.
 
 ```
 
 
 
 
 #### Process Hollowing
 
 NtUnmapViewOfSection and ZwUnmapViewOfSection are two versions of the same Windows Native System Services routine. 
The ZwUnmapViewOfSection routine unmaps a view of a section from the virtual address space of a subject process.

```
HMODULE handle = GetModuleHandle("ntdll.dll");
funcptr = GetProcAddress(handle, "NtUnmapViewOfSection")); 
or
funcptr = GetProcAddress(handle, "ZwUnmapViewOfSection"));
```

##### VirtualAllocEx function
```
LPVOID WINAPI VirtualAllocEx(
  _In_     HANDLE hProcess,
  _In_opt_ LPVOID lpAddress,
  _In_     SIZE_T dwSize,
  _In_     DWORD  flAllocationType,
  _In_     DWORD  flProtect
);
```
If the function succeeds, the return value is the base address of the allocated region of pages.
If the function fails, the return value is NULL


##### WriteProcessMemory function
Writes data to an area of memory in a specified process. 
```
BOOL WINAPI WriteProcessMemory(
  _In_  HANDLE  hProcess,
  _In_  LPVOID  lpBaseAddress,
  _In_  LPCVOID lpBuffer,
  _In_  SIZE_T  nSize,
  _Out_ SIZE_T  *lpNumberOfBytesWritten
);
```
If the function succeeds, the return value is nonzero.

* SetWindowsHookEx * - way that keyloggers receive keyboard inputs

