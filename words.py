def countWordsFromFile():
    file = input("Enter The File name")
    f = open(file,"r")
    numberOfWords = 0
    for line in f:
        words = line.split()
        numberOfWords = numberOfWords+len(words)
    print("Number of words: " + str(numberOfWords))


countWordsFromFile()