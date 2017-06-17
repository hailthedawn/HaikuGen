import markovify
#This file tests out basic functions that markovify can do
with open ("tests/Macbeth-Shakespeare.txt") as file:
    text=file.read(); #file read

text_model=markovify.NewlineText(text)  #model built
#NOTE: here, NewlineText is a nested class (inside Text). So, its instances can access Text's functions


#1 file=1 text model. for multiple files, create multiple models.

for i in range(5):
    print(text_model.make_sentence())