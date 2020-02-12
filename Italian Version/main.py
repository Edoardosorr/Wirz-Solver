from dictionary import words
print("If you do not want to enter the middle word enter 0 when asked")
def main(words):
    letters= {}
    start=input("starting letter\n").strip()
    mustcontain=input("must contain\n").strip()
    end=input("end letter\n").strip()
    goodwords=[]
    for word in words:
        letters=list(word)
        if letters[0] in start:
            if not mustcontain=="0":
                counter = 0
                for letter in letters:
                    if letter==mustcontain and not counter==0 and not counter==len(letters)-1:
                        if letters[-1] in end:
                            goodwords.append(word)
                    counter+=1
            else:
                if letters[-1] in end:
                    goodwords.append(word)
    string="The words you can use are:"
    counter=0
    for word in goodwords:
        counter +=1
        if counter == len(goodwords):
            string= string + f" {word}\n\n"
        else:
            string= string + f" {word},"

    print(string)
    return input("Do you wish to play another round? (y/n)")
continueyn=True
while continueyn:
    if main(words) in "y":
        pass
    else:
        exit()
