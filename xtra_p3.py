"""
Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest


with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  



with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  

wordset1 = set(wordlist1)  
wordset2 = set(wordlist2)  

maxlen = 10  


longwordset1 = set([word for word in wordlist1 if len(word) > 10]) 
longwordset2 = set([word for word in wordlist2 if len(word) > 10])  

longwords = longwordset1 & longwordset2

print()
print(f"The number of words in Hamlet with over 10 letters: {len(longwordset1)}")
print()
print(f"The number of words in Julius Caesar with over 10 letters: {len(longwordset2)}")
print()
print(f"The number of words with over 10 letters in Hamlet & Julius Caesar: {len(longwords)}")
print()
print(f"Unique words with over 10 letters in Hamlet & Julius Caesar: {sorted(longwords) = }")
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
