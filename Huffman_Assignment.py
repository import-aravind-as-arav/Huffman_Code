# Huffman Coding in python
from prettytable import PrettyTable #For creating tables in Python
import operator

file = open("for_encoding.txt",encoding='UTF-8') #Text file that contains the Biography of James C Maxwell
string = file.read().replace("\n", "") #replace Newline character with space.
file.close()

# To create tree nodes for Huffman Coding
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculating frequency of each symbol
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) 

nodes = freq
w=dict(nodes)
w.update((x, y/(len(string))) for x, y in w.items()) #Finding the symbol probabilities

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

#Creating a table of symbols and probabilities
t = PrettyTable(['Symbol', 'Probability'])
for key, val in w.items():
   t.add_row([key, val])
print (t)
print("\n\n")

#Creating a table with symbols and its Huffman Coding
coded={}
t1=PrettyTable(['Symbol','Huffman Code'])
for (char, frequency) in freq:
    coded[char]=huffmanCode[char]
    t1.add_row([char,huffmanCode[char]])
print(t1)

#Encoding the name and Roll no.
name="Aravind A"
roll="CB.EN.U4ECE18009"

roll_code="" #To store the encoded roll no. using Huffman Code 
name_code="" #To store the encoded name using Huffman Code

for i in name:
    name_code+=coded[i]  #Encoding name using the Huffman code stored in coded dictionary

for j in roll:
    roll_code+=coded[j]  #Encoding roll no. using the Huffman code stored in coded dictionary


print("Encoded roll no. is : ",roll_code)
print("")
print("Encoded name is : ",name_code)