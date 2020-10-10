# find needle in haystack
#Question 2
haystack = input("Input the haystack having the needles: ").lower()
needle = input("Which needle do you want to find in the haystack?").lower()


def findneedle():
    while len(needle) > len(haystack):
        return "Invalid input-Needle bigger than haystack"
    letter_index = 0
    for letter in haystack:
        if not (needle in haystack):
            return -1
        if letter == needle[0]:
            if needle in haystack[letter_index:letter_index + len(needle)]:
                return letter_index
        letter_index += 1


position = findneedle()
print("The needle is in the position", position)



# Question 1
# Finding the index

numbers = [3, 5, 6, 9, 15, 7, 3, 34]
key = int(input("enter the number you want to find: "))


def index_search():
    length = len(numbers)
    for x in range(0, length):
        if numbers[x] == key:
            return x
    return -1


index = index_search()
print("the key is at the position", index)
