words = [i for i in input().split()]

def isPalindrome(words):
    if list(words) == list(reversed(words)):
        print('%s is a palindrome'% words)
    else:
        print("%s is not a palindrome!" %words)

for i in words:
	isPalindrome(i)
