#sentence panlindrome without using any built-in functions
def is_palindrome(sentence):
    cleaned_sentence = ''
    for char in sentence:
        if char.isalnum():
            cleaned_sentence += char.lower()
    # Check if the cleaned sentence is equal to its reverse
    for i in range(len(cleaned_sentence) // 2):
        if cleaned_sentence[i] != cleaned_sentence[len(cleaned_sentence) - 1 - i]:
            return False
    return True


#longest palindrome longest substring
def longest_palindrome_substring(s):
    def is_palindrome(sub):
        for i in range(len(sub) // 2):
            if sub[i] != sub[len(sub) - 1 - i]:
                return False
        return True

    max_length = 0
    longest_palindrome = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]) and (j - i) > max_length:
                max_length = j - i
                longest_palindrome = s[i:j]
    return longest_palindrome
