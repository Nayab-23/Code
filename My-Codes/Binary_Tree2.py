def InsertNode(self, new_node):
        if self.NumberNodes == 0:
            self.Tree[0] = new_node
            self.FirstNode = 0
            self.NumberNodes += 1
            return
        
        current = self.FirstNode
        while True:
            if new_node.GetData() < self.Tree[current].GetData():
                if self.Tree[current].GetLeft() == -1:
                    self.Tree[self.NumberNodes] = new_node
                    self.Tree[current].SetLeft(self.NumberNodes)
                    self.NumberNodes += 1
                    return
                else:
                    current = self.Tree[current].GetLeft()
            else:
                if self.Tree[current].GetRight() == -1:
                    self.Tree[self.NumberNodes] = new_node
                    self.Tree[current].SetRight(self.NumberNodes)
                    self.NumberNodes += 1
                    return
                else:
                    current = self.Tree[current].GetRight()# your code goes here
