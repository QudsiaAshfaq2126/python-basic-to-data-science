word_state={}
with open("poem.txt","r") as q:
    for line in q:
        words=line.split(" ")
        for word in words:
            if word in word_state:
                word_state[word]+=1
            else:
               word_state[word]=1
print(word_state)
word_occurances = list(word_state.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_state.items():
    if count==max_count:
        print(word)


