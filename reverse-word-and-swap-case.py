def swap_case(word):
    return ''.join([character.lower() if character.isupper() else character.upper() for character in word])


def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')[::-1]
    return ' '.join([swap_case(word) for word in words])


print(swap_case('hello'))
