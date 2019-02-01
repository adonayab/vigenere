def alphabet_position(letter):

    alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in alphas:
        if letter == i:
            pos = alphas.find(i)
            if pos > 25:
                pos = pos % 26

    return pos


def rotate_character(char, rot):

    if char.isalpha():
        alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_pos = alphabet_position(char)
        for i in alphas:
            if i == char:
                rep_pos = char_pos + rot
                replacement_char = alphas[rep_pos]
                if rep_pos > 25:
                    rep_pos = rep_pos % 26
                    replacement_char = alphas[rep_pos]
    else:
        replacement_char = char

    if char.isupper():
        replacement_char = replacement_char.upper()

    return replacement_char
