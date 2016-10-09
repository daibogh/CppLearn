import numpy
class hashtable1(object):
	def __init__(self):
		self.List = numpy.zeros(10**20)
		print(self.List)
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
		Hash = 0
		for i in key:
			Hash = (Hash * 1664525) + ord(i) + 1013904223
		print(Hash)
		return Hash
h = hashtable1()
h.AddObject("petr",1997)
print(h.Get("petr"))