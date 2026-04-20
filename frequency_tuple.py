test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

freq_dict = {}
for elem in test_tup:
   if elem in freq_dict:
      freq_dict[elem] += 1
   else:
      freq_dict[elem] = 1
print("Tuple elements frequency is : " + str(freq_dict))
