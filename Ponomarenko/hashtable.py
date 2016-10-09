import numpy

import ctypes
m = ctypes.c_wchar_p * (ctypes.c_uint(2).value+1)
class hashtable1(object):
	def __init__(self):
		self.List = m(1)
		print(self.List.contents)
		pass
	def __HashFunction(self,key):
		return self.__Ly(key)

	def AddObject(self,key,value):
		GeneratedKey = self.__HashFunction(key)
		self.__Add(GeneratedKey,value)
	def __Add(self,key,value):
		self.List[key] = value

	def Get(self,key):
		IntKey = __HashFunction(key)
		return self.List[IntKey]
	# different hash functions
	def __Ly(self,key):
		Hash = ctypes.c_uint(0)
		for i in key:
			Hash = ctypes.c_uint(Hash.value * 1664525 + ord(i) + 1013904223)
		print(Hash)
		return Hash.value
h = hashtable1()
# h.AddObject("petr",1997)
# print(h.Get("petr"))