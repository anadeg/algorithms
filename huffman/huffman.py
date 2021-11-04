"""
huffman code
input --- line for coding
output ---
    the first line --- amount of unique chars, amount of bites after coding line
    the next lines --- char and its code
    the last line --- encoded line
"""


# class for tree implementation
class HuffmanNode:
    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right
        self.code = ''  # 0 or 1


def code_dictionary(huffman_node, code_dict, value=''):
    update_code = value + str(huffman_node.code)  # make code of current node

    # visit all tree list while it is possible
    if huffman_node.left:
        code_dictionary(huffman_node.left, code_dict, update_code)
    if huffman_node.right:
        code_dictionary(huffman_node.right, code_dict, update_code)

    # if we are in list (no way to go further), add char and its code in dictionary
    if not (huffman_node.left or huffman_node.right):
        code_dict.update({huffman_node.symbol: update_code})


def count_bites(line, code_diction):
    n = 0
    res_str = ''
    # go through line
    # find value(code) by key(current char) in dictionary
    # add length of char code to n
    # add char code to res_str
    for i in range(len(line)):
        n += len(code_diction.get(line[i]))
        res_str += code_diction.get(line[i])
    return n, res_str


code_dict = dict()  # char: code

for_coding = input("input string for coding --- ")
not_repeated_elements = list(set(for_coding))   # make set from line (to throw away repeating chars)
frequency_char = []  # char -- frequency

if len(not_repeated_elements) == 1:  # if the line consist of only one char
    new_node = HuffmanNode(not_repeated_elements[0], 1)  # make huffman node. frequency doesn't matter in this case
    new_node.code = 0  # code of this char is 0
    frequency_char.append(new_node)
else:
    for char in not_repeated_elements:
        frequency_char.append(HuffmanNode(char, for_coding.count(char)))  # add nodes with char and its frequency

    while len(frequency_char) > 1:
        # sorting by frequency because we will take two elements with the smallest frequencies to combine they
        frequency_char = sorted(frequency_char, key=lambda x: x.frequency)

        left = frequency_char[0]
        right = frequency_char[1]

        left.code = 0  # code of the smallest one of smallest is 0
        right.code = 1  # code of the biggest one of smallest is 1

        # combine nodes. char of combined nodes doesn't matter
        new_node = HuffmanNode('', left.frequency + right.frequency, left, right)

        frequency_char.remove(left)  # delete the smallest nodes
        frequency_char.remove(right)
        frequency_char.append(new_node)  # adding combined node


code_dictionary(frequency_char[0], code_dict)  # filling dictionary with char and its code

amount_of_chars = len(not_repeated_elements)
amount_of_bites, res_line = count_bites(for_coding, code_dict)

print(amount_of_chars, amount_of_bites)

for key, value in code_dict.items():
    print(f"{key}: {value}")

print(res_line)
