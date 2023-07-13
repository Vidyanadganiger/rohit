#python program to create an output tuple that  converts the words to uppercase from the input tuple of words
x=input('enter the number of words you want to convert into tuple')
n=int(x)
words=[]
for i in range(0,n):
    w=input('enter the word: ')
    words.append(w)
tplwords=tuple(words)
lst=[w.upper() for w in tplwords]
outputtpl=tuple(lst)
print('original words in tuple: ')
print(tplwords)
print('after converting to upper case new tuple: ')
print(outputtpl)
