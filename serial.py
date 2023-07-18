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

    def __init__(self, start_num=0):
        """Initialize with a start number and create a current Num to hold start"""
        self.start_num = start_num
        self.current_num = start_num

    def generate(self):
        """Create a variable to hold current Num, increment CurrentNum,
            return num
        """
        num = self.current_num
        self.current_num += 1
        return num

    def reset(self):
        """Reassign current_num to the start_num number"""
        self.currentNum = self.start_num
