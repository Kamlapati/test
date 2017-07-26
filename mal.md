 
#### Linked Librariers

 1. runtime linking is commonly used in malware
 2. LoadLibrary, GetProcAddress, LdrGetProcAddress, and LdrLoadDll Microsoft Windows functions allow programmers to import linked functions not listed in a program’s file header.
 
 
 ### Tools
 
| Tools                      | Descriptions                                     | 
| -------------------------- |:------------------------------------------------:| 
|Dependency Walker           | Dynamically linked functions                                  | 

 
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

