# Python program to merge two dictionaries and print the combined result

def merge():

   dict_1 = {1: 'a', 2: 'b'}
   dict_2 = {2: 'c', 4: 'd'}
   dict_3 = dict_2.copy()
   dict_3.update(dict_1)

   dict_4 = {'Name':'Berna','Class':'ECE_A'}
   dict_5 = {'Roll.No':'24BEC004','College':'MSEC'}
   dict_6 = dict_4.copy()
   dict_6.update(dict_5)

   return  dict_3,dict_6

# Main Routine
x = merge()
print("The merged list is:")
print(x[0])
print(x[1])
