class MyLinkedList:

    def __init__(self):
        self.p = []
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: return -1
        else: return self.p[index]

    def addAtHead(self, val: int) -> None:
        self.p.insert(0, val)
        self.length += 1

    def addAtTail(self, val: int) -> None:
        self.p.append(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < self.length:
            self.p.insert(index, val)
            self.length += 1
        elif index == self.length: self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length: return
        else:
            self.p.pop(index)
            self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
