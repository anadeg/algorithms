"""
decoding line with huffman code
input ---
    the first line --- amount of unique char and amount of bites in line
    the next lines --- char and its code (example --- a: 10)
    the last line --- encoded line
output --- decoded line
"""


def huffman_decode(line, dictionary):
    helping_str = ''
    result = ''
    # take symbol  from line
    # if line == some key in dictionary
    # take value and add it to result. nullify helping
    # else take next symbol from line and comparing again
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
