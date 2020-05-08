#Assigning elements to different lists

l1=[]
l2=[]
l1.append(1)
l1.append(2)
l1.append("mango")
print(l1)

l2.append("John")
print(l2)
l2.extend(["Ron",6,7])
print("l2=",l2)

l1.extend([10,11,12,"apple"])
print("l1=",l1)


#Accessing Elements from a tuple

tup1=(1,2,3,"hello","python")
print(tup1[1])
print(tup1[4])
print(tup1[0:])#accessing all the elements of a tuple


#Deleting different dictionary elements

dict1={1:"a",2:"b",3:"c",4:"d"}
print(dict1.items())
print(dict1.values())

print(dict1.pop(4))

print(dict1)
dict1.popitem()
print(dict1)
