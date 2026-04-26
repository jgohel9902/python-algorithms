def is_palindrome(s: str) -> bool:
    """
    Given a string, return True if it is a palindrome considering only
    alphanumeric characters and ignoring cases.

    Approach: Two pointers — left and right, move inward skipping
    non-alphanumeric characters.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Examples:
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome(" ")
    True
    >>> is_palindrome("Was it a car or a cat I saw?")
    True
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")