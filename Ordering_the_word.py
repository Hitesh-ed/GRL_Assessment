n = int(input())
words = [] # to store input words
word_dict = {} # to store distinct words 

# this loop stores all the input words in the list 'words'
for i in range(n):
    words.append(input())

# this loop does the main job
for word in words:
    if word not in word_dict.keys():
        word_dict[word] = 1
    else: 
        word_dict[word] += 1

# prints the number of distinct words
print(len(word_dict.keys()))

# prints the number of distinct words in order
for i in word_dict.values():
	print(i,end=" ")
