def recur_palindrome(x):
    if len(x) <= 1: ## Last Index remains
        return True
    else:
        if x[0] == x[-1]:
            return recur_palindrome(x[1:-1]) ## Chopping off FIRST and LAST index
        else:
            return False