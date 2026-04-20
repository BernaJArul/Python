# Python program to convert list of sentences to list of wordcounts

# Function
def sen_word(sentence):
   wordList = sentence.split(" ")
   wordList1 = [ x for x in sentence if x!=" "] #using list comprehension
   return wordList,wordList1

# Main Routine
ori_sentence = input("Enter a sentence:")
print("Result:",sen_word(ori_sentence))
