import ctypes 
from ctypes.wintypes import DWORD,HANDLE,LPWSTR

#create handlers for the DLLs
k_handle = ctypes.WinDLL("Kernel32.dll")
d_handle = ctypes.WinDLL("DNSAPI.dll")

#setup structure
class DNS_CACHE_ENTRY(ctypes.Structure):
	_fields_ = [
	("pNext",HANDLE),
	("recName",LPWSTR),
	("wType", DWORD),
	("wDataLength", DWORD),
	("dwFlags", DWORD)
	]

#instantiate the class
DNS_Entry = DNS_CACHE_ENTRY()

DNS_Entry.wDataLength = 1024

#run API call
response = d_handle.DnsGetCacheDataTable(ctypes.byref(DNS_Entry))

#add in some error reporting
if response == 0:
	print("Error Code: {0}".format(k_handle.GetLastError()))

#ignore second entry and recast
DNS_Entry = ctypes.cast(DNS_Entry.pNext, ctypes.POINTER(DNS_CACHE_ENTRY))

#print and recast the entry until end of loop
while True:
	try:
	 print("DNS Entry {0} - Type {1}".format(DNS_Entry.contents.recName, DNS_Entry.contents.wType))
	 DNS_Entry = ctypes.cast(DNS_Entry.pNext, ctypes.POINTER(DNS_CACHE_ENTRY))
	except:
		break
