import sys

#Open word bank text
dictionary = open("enable1.txt")

#Copy text into string variable
word_bank = dictionary.read()

#Create list of word lengths
word_bank_length = [len(x) for x in word_bank.split()]

#Combine into dictionary keys = Words. values = word length
word_bank_dictionary = dict(zip(word_bank.split(), word_bank_length))

print("Please input valid word: ")

start_word = sys.stdin.readline()

#Remove newline charater
start_word = start_word.strip('\n')

#Ensure word is 2 letters long and in in dictionary
while ((len(start_word) < 2) or (start_word not in word_bank_dictionary)):
   print("Please input valid word: ")
   start_word = sys.stdin.readline()
   start_word = start_word.strip('\n')

#Extra line for formating
print()

#Initialize index
i = len(start_word) + 1

while True:
    valid_i_letter_word = []

    #Compile list of all words with length of interest
    all_i_letter_words = [k for k,v in word_bank_dictionary.items() if v == i] 
    
    #Search for matching words in all words of length of interest
    valid_i_letter_word = [s for s in all_i_letter_words if start_word in s] 
    
    #Break if no matching words are found
    if not valid_i_letter_word: 
        break

    #Print if matching words were found
    print("Valid {} letter words: ".format(i))
    print(", ".join(valid_i_letter_word))
    print()
    
    i = i + 1
    