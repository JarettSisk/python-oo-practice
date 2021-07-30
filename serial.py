"""Python serial number generator."""

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
    def __init__(self, start):
        self.start = start
        self.serial = start
    
    def generate(self):
        """Generate new serial number"""
        print(self.serial)
        self.serial += 1

    def reset(self):
        """Reset serial number back to original start point"""
        self.serial = self.start

    def __repr__(self):
        """ Return name, start, and current serial"""
        return f"Serial generator start={self.start} serial={self.serial}"
    

serial = SerialGenerator(start=100)
serial.generate()
print(serial.__repr__())



