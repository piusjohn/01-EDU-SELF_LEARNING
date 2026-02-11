def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
test_word_1 = "1Racecar1"
test_word_2 = "hello"
test_word_3 = "A man a plan a canal Panama"

print (f"{test_word_1} is a palindrome : {is_palindrome(test_word_1)}")
print (f"{test_word_2} is a palindrome : {is_palindrome(test_word_2)}")
print (f"{test_word_3} is a palindrome : {is_palindrome(test_word_3)}")