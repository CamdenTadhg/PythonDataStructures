def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    vowel_list = []
    for char in s:
        if char in vowels:
            vowel_list.append(char)
    vowel_list.reverse()
    index = 0
    new_list = []
    for char in s:
        if char in vowels:
            new_list.append(vowel_list[index])
            index += 1
        else:
            new_list.append(char)
    return ''.join(new_list)