# __init__ should initialize a jar with the capacity unless the capacity is negative then it should raise a ValueError.

# __str__ should return a str with the amount of cookies in the jar

# deposit should add n cookies to the cookie jar unless it exceeds the capacity 12 then it should raise a ValueError

# withdraw should take n cookies out of the cookie jar unless that amount is more than the amount in the jar, then it should raise a ValueError

# capacity should return the cookie jars capacity

# size should return the actual quantity of cookies in the jar, initially 0


class Jar:
    def __init__(self, size=0, capacity=12):
        self.size = size
        self.capacity = capacity

    def __str__(self):
        return f"there are {self.size} cookies in the jar the capacity of the jar is {self.capacity}"

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("the capacity of the cookie jar is 12 bro, your gonna bust it")
        self.size = self.size + n
        return self.size 

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("there arnt that many cookies in the jar fatty")
        self.size = self.size - n
        return self.size 

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("capacity must be a a positive integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size



def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(3)
    print(jar)


if __name__ == "__main__":
    main()


















