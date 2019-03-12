def count1(string, searched_letter):
    count =  0
    for letter in string:
        if letter == searched_letter:
            count = count +1
    return count


hest = count1("banana","a")
print(hest)
