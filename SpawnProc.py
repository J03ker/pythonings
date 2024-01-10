import ctypes
from ctypes.wintypes import DWORD,LPWSTR,WORD,HANDLE,LPBYTE

k_handle = ctypes.WinDLL("Kernel32.dll")

#structure for process info
#https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information
class PROCESS_INFORMATION(ctypes.Structure):
	_fields_ = [
		("hProcess", HANDLE),
		("hThread",HANDLE),
		("dwProcessId",DWORD),
		("dwThreadId",DWORD)
		]

#structure for startup creation
#https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfow
class STARTUPINFO(ctypes.Structure):
	_fields_ = [
	("cb", DWORD),
	("lpReserved", LPWSTR),
	("lpDesktop", LPWSTR),
	("lpTitle", LPWSTR),
	("dwX", DWORD),
	("dwY", DWORD),
	("dwXSize", DWORD),
	("dwYSize", DWORD),
	("dwXCountChars", DWORD),
	("dwYCountChars", DWORD),
	("dwFillAttribute", DWORD),
	("dwFlags", DWORD),
	("wShowWindow", WORD),
	("cbReserved2", WORD),
	("lpReserved2", LPBYTE),
	("hStdInput", HANDLE),
	("hStdOutput", HANDLE),
	("hStdError", HANDLE)
	]

#CreateProcessW Funtion 
#https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
lpApplicationName = "C:\\Windows\\System32\\cmd.exe"
lpCommandLine = None
lpProcessAttributes = None
lpThreadAttributes = None
lpEnvironment = None
lpCurrentDirectory = None

dwCreationFlags = 0x00000010

bInheritHandle = False
lpProcessInformation = PROCESS_INFORMATION()

lpStartupInfo = STARTUPINFO()

lpStartupInfo.wShowWindow = 0x1
lpStartupInfo.dwFlags = 0x1

response = k_handle.CreateProcessW(
	lpApplicationName,
	lpCommandLine,
	lpProcessAttributes,
	lpThreadAttributes,
	bInheritHandle,
	dwCreationFlags,
	lpEnvironment,
	lpCurrentDirectory,
	ctypes.byref(lpStartupInfo),
	ctypes.byref(lpProcessInformation))

#feedback for user and error handling
if response > 0:
	print("Process is running")
else:
	print("Process Failed. Error Code: {0}".format(k_handle.GetLastError()))

	






