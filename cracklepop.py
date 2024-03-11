# cracklepop.py

class namedint:
    def __init__(self, value: int, name: str = ''):
        self.value = value
        self.name = name
    def __iadd__(self,n):
        self.value += n
        return self
    def __lt__(self, other):
        assert isinstance(other, namedint)
        return self.value < other.value
    def __gt__(self, other):
        assert isinstance(other, namedint)
        return self.value > other.value
    def __str__(self):
        if self.name:
            return self.name
        return str(self.value)
    def __repr__(self):
        return self.__str__()

def multiples_of(n: int, name: str = ''):
    '''
    Generates a stream of namedints of multiples of 'n'.
    '''
    m = namedint(n, name)
    while True:
        yield m
        m += n

def merge(gen1, gen2):
    '''
    Merges 2 generators/streams of namedints in ascending order.
    '''
    e1 = next(gen1)
    e2 = next(gen2)
    while True:
        if e1 > e2:
            yield e2
            e2 = next(gen2)
        elif e2 > e1:
            yield e1
            e1 = next(gen1)
        else:
            yield namedint(e1.value, e1.name + e2.name)
            e1 = next(gen1)
            e2 = next(gen2)

def print_n_elements(gen, n):
    '''
    Prints 'n' elements of a generator/stream.
    '''
    while n > 0:
        e = next(gen)
        print(e)
        n -= 1


if __name__ == '__main__':
    threes = multiples_of(3, 'Crackle')
    fives = multiples_of(5, 'Pop')
    integers = multiples_of(1)
    print_n_elements(merge(integers, merge(threes,fives)), 100)
