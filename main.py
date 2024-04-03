import string
symbols = string.printable
#get's all possible words (ascii combos)
#creates our dictionary of all possible ascii words
def make_dic(length, word):
    if not length:
        yield word
    else:
        for i in symbols:
            yield from make_dic(length-1, word+i)

def make_book(size, words, curr):
    if not size:
        yield curr
    else:
        for gen in words:
            for word in gen:
                yield from make_book(size-1, words, curr + " " + word)


#using generators so it doesn't immedietley crash
#longest word in a major dictionary is 45
#but the longest publishd word is 1,909. We will limit our words to this size
#it will still be an infinite library just a smaller one
def main():
    #will be a list containing generators of generators
    words = []
    for i in range(1909):
        for s in symbols:
            words.append(make_dic(i,s))
    library = []
    count = 0
    while True:
        for gen in words:
            for word in gen:
                library.append(make_book(count, words, word))

if __name__ == '__main__':
    main()
