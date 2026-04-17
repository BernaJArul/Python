def merge(list_1,list_2):
   list_1.sort()
   list_2.sort()
   list4 = list_1 + list_2
   return list4

list1 = ['apple','orange','kiwi']
list2 = ['rose','lilly','lotus']
list3 = merge(list1,list2)
print("Merged list is:",list3)
