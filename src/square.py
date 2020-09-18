def isSqaure(p, q):
    delta = abs(p[0] - q[0])
    return p[0] == q[0] or p[1] == q[1] or delta == abs(p[1] - q[1])


class Node(object):
    def __init__(self, p):
        self.p = p
        self.left, self.right = None, None

    def addi(self, p, level):
        if not self:
            self = Node(p)
            if level == 3:
                return (True, self)
            else:
                return (False, self)
        else:
            if isSqaure(self.p, p):
                if self.left:
                    return self.left.addi(p, level + 1)
                else:
                    self.left = Node(p)
                    if level == 3:
                        return (True, self)
                    else:
                        return (False, self)
            else:
                if self.right:
                    return self.addi(self.right, p)
                else:
                    self.right = Node(p)
                    if level == 3:
                        return (True, self)
                    else:
                        return (False, self)



class Square(object):
    def __init__(self):
        self.bst = None

    def add(self, p):
        if not self.bst:
            self.bst = Node(p)
            return False
        (v, _) = self.bst.addi(p, 0)
        return v


s = Square()
print(s.add([1,2]))
print(s.add([1,5]))
print(s.add([4,5]))
print(s.add([4,2]))
print(s.add([4,5]))

exit(0)
print(isSqaure([1,2], [1,5]))
print(isSqaure([1,3], [6,3]))
print(isSqaure([1,2], [4,5]))
print(isSqaure([1,2], [4,7]))