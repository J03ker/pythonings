#import cytpes to interact with Windows API
import ctypes

#create kernel handling variable
k_handle = ctypes.WinDLL("Kernel32.dll")

#creates variable for all Process Access Rights
PROCESS_ALL_ACCESS = ( 0x000F0000 | 0x00100000 | 0xFFF)

#setup parameters as per documentation - dwProcessID is Hex converted PID
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = 0x46C4

#get response, passing parameters in order as expected
response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

#Some error handling, very useful when attempting to open privileged processes
error = k_handle.GetLastError()
if error != 0:
	print("Error Code:{0}".format(error))
	exit(1)

#some user output reporting what's happened
if response <= 0:
	print("Handle was not created")
else:
	print(f"Handle was created and is", response)
