#import library for interacting with Windows API
import ctypes

#Create user and error handle
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

#Setup required variables for the Message Box
#https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw
hWnd = None
lpText = "Hello World"
lpCaption = "Hello Everyone"
uType = 0x00000001

#Generate the Messagebox response (with error handling)
response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)
error = k_handle.GetLastError()

#Error Reporting
if error !=0:
	print("Error Code: {0}".format(error))
	exit(1)

#User interaction status
if response == 1:
	print("User Clicked OK")

elif response == 2:
	print("User Clicked Cancel")
	
