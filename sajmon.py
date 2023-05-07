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

    def inorder_tree_walk(self,node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.data)
            self.inorder_tree_walk(node.right)

    def letter_value(self,node,letter):
        if node.letter == letter:
            return node.data
        if node.left is not None:
            left=self.letter_value(node.left,letter)
            if left is not None:
                return left
        if node.right is not None:
            right=self.letter_value(node.right,letter)
            if right is not None:
                return right

    def search_tree(self,letter):
        if(letter==" "):
            return "/"
        value = self.letter_value(self.root,letter)
        out=""
        src_node=tree.root

        while src_node.data!=value:
            if src_node.data > value:
                src_node=src_node.left
                out+="."
            elif src_node.data < value:
                src_node=src_node.right
                out+="-"
        return out
    def find_character(self,niz):
        src_node=self.root
        for simbol in niz:
            if simbol ==".":
                src_node=src_node.left
            elif simbol=="-":
                src_node=src_node.right
            elif simbol=="/":
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

tree=Tree()
elements = [('start', 100),
            ('E', 50), ('T', 150),
            ('I', 25), ('A', 75), ('N', 125), ('M', 175),
            ('S', 12), ('U', 37), ('R', 62), ('W', 87), ('D', 112), ('K', 137), ('G', 167), ('O', 187),
            ('H', 6), ('V', 18), ('F', 31), (' ', 40), ('L', 55), (' ', 70), ('P', 80), ('J', 90), ('B', 110), ('X', 120), ('C', 130), ('Y', 140), ('Z', 155), ('Q', 170), (' ', 180), (' ', 190),
            ('5', 5), ('4', 7), (' ', 17), ('3', 19), (' ', 30), (' ', 32), (' ', 39), ('2', 41), (' ', 54), (' ', 56), ('+', 69), (' ', 71), (' ', 79),  (' ', 81), (' ', 89), ('1', 91), ('6', 104), ('=', 111), ('/', 119), (' ', 121), (' ', 129), (' ', 131), (' ', 139), (' ', 141), ('7', 154), (' ', 169), (' ', 165), (' ', 171), ('8', 179), (' ', 181), ('9', 189), ('0', 191)]


for i in range(len(elements)):
    tree.insert(Node(data=elements[i][1],letter=elements[i][0]))

while(1):
    tree.print_tree()
    ulaz=input("Ulaz: ")
    izlaz=""
    if ulaz[0] in ('-','.','/'):
        sifre=ulaz.split()
        for sifra in sifre:
            izlaz+=tree.find_character(sifra)

    else:
        for slovo in ulaz:
            izlaz+=" "+tree.search_tree(slovo)
    tree.print_tree()
    print("Izlaz: "+izlaz)



