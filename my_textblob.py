from textblob import TextBlob

def convert(string):
    li=list(string.split())
    return li
str1=input("Enter your word : ")
words=convert(str1)
corrected_words=[]
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("corrected words are:")
for i in corrected_words:
    print(i.correct(), end='')