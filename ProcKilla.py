import ctypes

#FindWindowA
#GetWindowThreadProcessId
#OpenProcess
#TerminateProcess
#Every stage should have error handling

# HWND FindWindowA(
#   [in, optional] LPCSTR lpClassName,
#   [in, optional] LPCSTR lpWindowName
# );


#setup handlers
k_handle = ctypes.WinDLL("Kernel32.dll")
u_handle = ctypes.WinDLL("User32.dll")

#creates variable for all Process Access Rights
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF)

#setup parameters for FindWindowA (Because its an A it's ANSI encoded)
#since its a pointer (LP), we'll use ctypes.c_char_p
#since its ANSI not ASCII we need to encode it

# lpClassName = NULL
lpWindowName =  ctypes.c_char_p(input("Enter Windows Name to Kill: ").encode('utf-8'))

hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
	print("Error Code: {0} - Could not determine handle".format(k_handle.GetLastError()))
else:
	print(f"Got the handle, and it is {hWnd}")


lpdwProcessId = ctypes.c_ulong()
response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))

if response == 0:
	print("Error Code: {0} - Could not determine PID".format(k_handle.GetLastError()))
	exit(1)
else:
	print("PID attained")

#setup parameters as per documentation - dwProcessID is Hex converted PID
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpdwProcessId

hprocess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
if hprocess <= 0:
	print("Error Code: {0} - Could not grab priv handle".format(k_handle.GetLastError()))
else:
	print("Got the handle")


#Time to terminate the process:
# BOOL TerminateProcess(
#   [in] HANDLE hProcess,
#   [in] UINT   uExitCode
# );

uExitCode = 0x1

response = k_handle.TerminateProcess(hprocess,uExitCode)

if response == 0:
	print("Error Code: {0} - Could not terminate process".format(k_handle.GetLastError()))
else:
	print("Process Terminated")
