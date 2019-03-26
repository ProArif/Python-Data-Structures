# Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit. 
# The combined dictionary contains the key and value pairs in a specific sequence eliminating any duplicate keys. 
# The best use of ChainMap is to search through multiple dictionaries at a time and get the proper key-value pair mapping.
# We also see that these ChainMaps behave as stack data structure.

import collections

dic1 = {'name': 'arif','age':'22','color': 'white'}
dic2 = {'name':'akash','age':'12','color':'brown','choice':'bike'}

res = collections.ChainMap(dic1,dic2)
print(res)

#single dictionary
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))

#print all the elements
for key,val in res.items():
    print("Key:{}".format(key))
    print('Values= {}'.format(val))
    print()


#map reordering
res1 = collections.ChainMap(dic2,dic1)
print(res1)

#update map
dic1['name'] = 'mim'
print(res.maps,'\n')