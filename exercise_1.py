paragraph = open("text.txt", "r")
list = []
list = paragraph.read()
count = dict()
words = list.split()

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print("Total word frequency")
print(count)
paragraph.close()
