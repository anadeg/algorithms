def huffman_decode(line, dictionary):
    helping_str = ''
    result = ''
    for i in range(len(line)):
        helping_str += line[i]
        if helping_str in dictionary:
            result += dictionary.get(helping_str)
            helping_str = ''

    return result


def main():
    unique_chars, amount_of_bites = map(int, input().split())
    huffman = dict()
    for i in range(unique_chars):
        char, code = input().split(sep=': ')
        huffman[code] = char
    line = input()

    decoded_str = huffman_decode(line, huffman)
    print(decoded_str)


if __name__ == "__main__":
    main()
