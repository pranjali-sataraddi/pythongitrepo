'''
Datastructure 
1.Built-in DS
2.User-Defined DS

'''
#list:
l = [10,20,30,20.344,"alen",[1,2,3]]
print(type(l))

#length of the list
print("The length of the list is ",len(l))

#to access the element of the list
l1 = [10,20,30,[100,200]]
print(l1[2])

print(l1[3][1])

#concatination of two lists
l1 = [10,20,30]
l2 = [40,50,60]
print(l1 + l2)

#Repitation in the list
print(l1 * 3)


#Sclicing in list
l3 =  [10,20,30,40,50,60,66,70]
#30-50
#l2[start:stop:step]
print(l3)
print(l3[2:5])
print(l3[-2])

#How to reverse list in python using sclicing
print(l3[::-1])
l3 =  [10,20,30,40,50,60,66,70]
print(l3[2:])



