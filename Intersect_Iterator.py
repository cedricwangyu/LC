
class Intersect_Iterator():
    def __init__(self, iterator_1, iterator_2):
        self.iterator_1 = iterator_1
        self.iterator_2 = iterator_2
        self.next_item = None

    def has_next(self):
        if self.next_item is not None: return True
        if not self.iterator_1.has_next() or not self.iterator_2.has_next(): 
            return False

        item_1, item_2 = self.iterator_1.next(), self.iterator_2.next()
        if item_1 == item_2:
            self.next_item = item_1
            return True

        while self.iterator_1.has_next() and self.iterator_2.has_next():
            if item_1 < item_2: 
                item_1 = self.iterator_1.next()
            elif item_1 > item_2:
                item_2 = self.iterator_2.next()
            else:
                self.next_item = item_1
                return True

        return False
    
    def next(self):
        if self.next_item or self.has_next():
            self.next_item, res = None, self.next_item
            return res
        
        else:
            raise ValueError("next element does not exists")

        
        
            



            