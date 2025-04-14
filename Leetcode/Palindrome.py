# A palindrome is a word, number, phrase, or sequence that reads the same
# forward and backward, ignoring spaces, punctuation, and capitalization.
# Examples:
# - "madam" -> Palindrome
# - "racecar" -> Palindrome
# - "12321" -> Palindrome
# - "hello" -> Not a Palindrome


def palindrome(x):
    for i in range(len(x) // 2): ## checking left half with the right half
        if x[i] != x[len(x) - i - 1]: ## reversing [(-0-1 = -1),(-1-1 = -2)]
            return False

    return True


def recur_palindrome(x):
    if len(x) <= 1: ## Last Index remains
        return True
    else:
        if x[0] == x[-1]:
            return recur_palindrome(x[1:-1]) ## Chopping off FIRST and LAST index
        else:
            return False
