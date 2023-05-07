class Node:
    def __init__(self, parent=None, left=None, right=None, data= None, letter = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data
        self.letter = letter


class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        return node
    
    def find_letter_value(self, node,letter):
        if node.letter == letter:
            return node.data
        if node.left is not None:
            left = self.find_letter_value(node.left, letter)
            if left is not None:
                return left
        if node.right is not None:
            right = self.find_letter_value(node.right, letter)
            if right is not None:
                return right
    
    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.data)
            self.inorder_tree_walk(node.right)

    def search_tree(self, letter):
        if letter == ' ':
            return '/'
        
        value = self.find_letter_value(self.root,letter)

        out = ""
        src_node = tree.root

        while src_node.data != value:
            if src_node.data > value:
                src_node = src_node.left
                out += "."
            elif src_node.data < value:
                src_node = src_node.right
                out += "-"
        return out
    
    def find_character(self, sequence):
        src_node = self.root
        for move in sequence:
            if move == '.':
                src_node = src_node.left
            elif move == '-':
                src_node = src_node.right
            elif move == '/':
                return " "
        
        return src_node.letter

    def print_tree(self):
            def display(root):
                # No child.
                if root.right is None and root.left is None:
                    line = '%s' % root.letter
                    width = len(line)
                    height = 1
                    middle = width // 2
                    return [line], width, height, middle

                # Only left child.
                if root.right is None:
                    lines, n, p, x = display(root.left)
                    s = '%s' % root.letter
                    u = len(s)
                    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                    second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                    shifted_lines = [line + u * ' ' for line in lines]
                    return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

                # Only right child.
                if root.left is None:
                    lines, n, p, x = display(root.right)
                    s = '%s' % root.letter
                    u = len(s)
                    first_line = s + x * '_' + (n - x) * ' '
                    second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                    shifted_lines = [u * ' ' + line for line in lines]
                    return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

                # Two children.
                left, n, p, x = display(root.left)
                right, m, q, y = display(root.right)
                s = '%s' % root.letter
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
                second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
                if p < q:
                    left += [n * ' '] * (q - p)
                elif q < p:
                    right += [m * ' '] * (p - q)
                zipped_lines = zip(left, right)
                lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
                return lines, n + m + u, max(p, q) + 2, n + u // 2

            lines, *_ = display(self.root)
            for line in lines:
                print(line)


tree = Tree()
elements = [('start', 200),
            ('E', 100), ('T', 300),
            ('I', 50), ('A', 150), ('N', 250), ('M', 350),
            ('S', 25), ('U', 75), ('R', 125), ('W', 175), ('D', 225), ('K', 275), ('G', 325), ('O', 375),
            ('H', 10), ('V', 30), ('F', 69), (' ', 90), ('L', 110), (' ', 130), ('P', 160), ('J', 180), ('B', 210), ('X', 240), ('C', 260), ('Y', 280), ('Z', 310), ('Q', 340), (' ', 360), (' ', 380),
            ('5', 5), ('4', 12), (' ', 27), ('3', 33), (' ', 68), (' ', 71), (' ', 88), ('2', 92), (' ', 109), (' ', 111), ('+', 129), (' ', 131), (' ', 159), (' ', 161), (' ', 179), ('1', 181), ('6', 209), ('=', 211), ('/', 239), (' ', 241), (' ', 259), (' ', 261), (' ', 279), (' ', 281), ('7', 309), (' ', 311), (' ', 339), (' ', 341), ('8', 359), (' ', 361), ('9', 379), ('0', 381)]

for i in range(len(elements)):
    tree.insert(Node(data=elements[i][1], letter=elements[i][0]))

while(1):
    inp = input("Ulaz: ")
    output = ""
    if inp[0] in ('.', '-', '/'):
        moves = inp.split(' ')
        for move in moves:
            output += tree.find_character(move)
    else:
        for letter in inp:
            output += " " + tree.search_tree(letter)
    tree.print_tree()
    print("Izlaz: " + output)