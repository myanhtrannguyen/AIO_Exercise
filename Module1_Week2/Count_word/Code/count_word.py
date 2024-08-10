def count_word (file_path) :
    counter = {}
    words = file_path.split()
    for word in words :
        if word in counter :
            counter[word] += 1
        else :
            counter[word] = 1
    return counter
file_path = open('P1_data.txt','r')
file_path = file_path.read()
result = count_word ( file_path )
print(result)
