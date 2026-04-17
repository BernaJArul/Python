from collections import Counter

def common_elements_frequency(list1, list2):
   common_elements = set(list1) & set(list2)
   freq_list1 = Counter(list1)
   freq_list2 = Counter(list2)
# Prepare the result dictionary
   result = {element: (freq_list1[element], freq_list2[element]) for element in common_elements}
					      
   return result

# Example usage
list1 = [1,2,3,4,5]
list2 = [11,2,13,14,15]
frequency = common_elements_frequency(list1, list2)
print(frequency)
