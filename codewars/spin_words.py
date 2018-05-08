def spin_words(sentence):
    sentence_new=[]
    for i in sentence.split(" "):
        if len(i)>=5:
            i=i[::-1]
        sentence_new.append(i)
    return " ".join(sentence_new)


print(spin_words("Welcome"))
