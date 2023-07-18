class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

#
    def __init__(self, start=0):
        """Initialize with a start number and create a current Num to hold start"""
        self.start = start
        self.currentNum = start

    def generate(self):
        """Create a variable to hold current Num, increment CurrentNum,
            return num
        """
        num = self.currentNum
        self.currentNum += 1
        return num

    def reset(self):
        """Reassign currentNum to the start number"""
        self.currentNum = self.start
