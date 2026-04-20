#Python program to read an element from list by index and display error if the index is out of range

def ele_index(list1, index):
   try:
      element = list1[index]
      return element
   except IndexError:
      print("Error: Index is out of range")
   finally:
      print("End of the program")

list1 = [10,20,30,40,50]

index_1 = int(input("Enter an index:"))
element = ele_index(list1, index_1)
print(f"Element at index {index_1}: {element}")
