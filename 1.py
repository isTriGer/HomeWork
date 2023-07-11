def palindrome(word):
    word_list = list(word.lower())
    for i in range(int(len(word) / 2)):
        if word_list[i] != word_list[-i - 1]:
            return False
    return True


print(palindrome('лепсспел'))
print(palindrome('Hello Word'))