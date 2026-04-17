def new_list(list_b):
   chunked_list = list()
   chunked_size = 3
   for i in range(0,len(list_b),chunked_size):
      chunked_list.append (list_b[i:i+chunked_size])
   return chunked_list


list_a = [1,2,3,4,5,6,7,8,9,10]
print("The new list is:",new_list(list_a))
