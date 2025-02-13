# //DICTIONARIES IN PYTHON 
#  Dictionaries are used to store data values in key value pairs. 
#  A dictionary is a collection which is unordered, changeable or mutable and do not allow duplicates.
#  Dictionary items are unordered, changeable, and does not allow duplicates. 
#  Dictionary items are presented in key value pairs, and can be referred to by using the key name. 
#  Dictionaries cannot have two items with the same key. 
#  A dictionary can nested and can contain another dictionary.
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

d1={}
print(d1)
print(type(d1))
thisdict = {
  "brand": "Toyota",
  "model": "Mustang",
  "year": 1966
}
print(thisdict)
myintro={
  "name": "safwan",
  "age" : 22,
}
print(myintro)
print(myintro.keys())
print(myintro.values())