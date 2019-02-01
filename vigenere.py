from helpers import alphabet_position, rotate_character


def encrypt(text, word_rot):

    encrypted = ''

    rot_word_text = ''
    word_rot_length = len(word_rot)
    k = 0
    for i in text:
        if i.isalpha():
            rot_word_text += word_rot[k % word_rot_length]
            k += 1
        else:
            rot_word_text += i

    for idx in range(len(text)):
        if text[idx].isalpha():
            encrypted += rotate_character(text[idx],
                                          alphabet_position(rot_word_text[idx]))
        else:
            encrypted += text[idx]

    return encrypted


def main():

    message = input('Type a message:\n')
    rot = input('Rotate by:\n')

    print(encrypt(message, rot))


if __name__ == "__main__":
    main()
