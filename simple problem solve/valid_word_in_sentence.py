sentence = "ooo are mine& and I am your9"

sentence_list = sentence.split(" ")
output = 0
for word in sentence_list:
    if word.isalnum() and len(word) >2 and ("a" in list(word.lower()) 
                                            or "e" in list(word.lower())
                                            or "i" in list(word.lower()) 
                                            or "o" in list(word.lower())  
                                            or "u" in list(word.lower()) ) and ("a" not in list(word.lower()) 
                                            or "e" not in list(word.lower())
                                            or "i" not in list(word.lower()) 
                                            or "o" not in list(word.lower())  
                                            or "u" not in list(word.lower()) ) :


        output += 1
print(output)