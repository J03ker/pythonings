import ctypes
from ctypes.wintypes import DWORD,LPWSTR,WORD,HANDLE,LPBYTE

u_handler = ctypes.WinDLL("User32.dll")
k_handler = ctypes.WinDLL("Kernel32.dll")

class PROCESS_INFORMATION(ctypes.Structure):
	_fields_ = [
		("hProcess", HANDLE),
		("hThread",HANDLE),
		("dwProcessId",DWORD),
		("dwThreadId",DWORD)
		]

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


lpApplicationName = "C:\\Windows\\System32\\notepad.exe"
lpCommandLine = None
lpProcessAttributes = None
lpThreadAttributes = None
bInheritHandles = False
dwCreationFlags = 0x00000010
lpEnvironment = None
lpCurrentDirectory = None
lpStartupInfo = STARTUPINFO()
lpProcessInformation = PROCESS_INFORMATION()


response = k_handler.CreateProcessW(lpApplicationName,lpCommandLine,lpProcessAttributes,lpThreadAttributes,bInheritHandles,dwCreationFlags,lpEnvironment,lpCurrentDirectory,lpStartupInfo,lpProcessInformation)


error = k_handler.GetLastError()
