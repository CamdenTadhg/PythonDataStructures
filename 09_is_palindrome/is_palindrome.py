def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower()
    phrase = phrase.replace(' ', '', -1)
    forward_list = list(phrase)
    backward_list = list(phrase)
    backward_list.reverse()
    if forward_list == backward_list:
        return True
    return False
