import numpy as np

class Complex:
    """
    Class creates a complex number.
    Class takes in two real numbers a and b, 
    where a is the real part and b is the imaginary part
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    @staticmethod
    def classmethods():
        print("modulus, conjugate, __add__, __sub__, __mul__, __eq__, ")
        print("__radd__, __rsub__, __rmul__, __neg__, __complex__, __str__")

    def __str__(self):
        """Return a string of the complex number on the form a + bi"""
        return f"{self.a} + {self.b}i"

    def modulus(self):
        """
        Calculates the modulus of the complex number.
        Return a number of type float.
        """
        a = self.a
        b = self.b
        modulus = np.sqrt(a**2 + b**2)
        return float(modulus)
    
    def conjugate(self):
        """
        Return the conjugate of the complex number.
        a + bi becomes a - bi
        """
        b = -self.b
        a = self.a
        return Complex(a, b)

    def __add__(self, other):
        """
        Add function for the complex number.
        Takes in two objects, first is self and another object.
        Checks whether the other object is of type int, float, complex
        or Complex (which is this class) and return a new complex number object
        of the Complex class.
        """
        if isinstance(other, (int, float)):
            return Complex(self.a + other, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        elif isinstance(other, complex):
            return Complex(self.a + other.real, self.b + other.imag)


    def __sub__(self, other):
        """
        Subtract function for the complex number.
        Takes in two objects, first is self and another object.
        Checks whether the other object is of type int, float, complex
        or Complex (which is this class) and return a new complex number object
        of the Complex class.
        """
        if isinstance(other, (int, float)):
            return Complex(self.a - other, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        elif isinstance(other, complex):
            return Complex(self.a - other.real, self.b - other.imag)


    def __mul__(self, other):
        """
        Multiplication function for the complex number.
        Takes in two objects, first is self and another object.
        Checks whether the other object is of type int, float, complex
        or Complex (which is this class) and return a new complex number object
        of the Complex class.
        """
        if isinstance(other, (int, float)):
            return Complex(self.a * other, self.b * other)
        elif isinstance(other, Complex):
            return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
        elif isinstance(other, complex):
            return Complex(self.a*other.real - self.b*other.imag, self.a*other.imag + self.b*other.real)

    def __eq__(self, other):
        """
        Takes in two objects, self and other
        Checks whether the value of the two objects are equal.
        Checks for int, float, Complex and complex
        """
        value = False
        if isinstance(other, (int, float)):
            if (self.a == other) and (self.b == 0):
                value = True
            return value
        if isinstance(other, Complex):
            if (self.a == other.a) and (self.b == other.b):
                value = True
            return value
        if isinstance(other, complex):
            if (self.a == other.real) and (self.b == other.imag):
                value = True
            return value

    def __radd__(self, other):
        """
        Right add function for the complex number.
        Takes in two objects, checks other + self.
        Checks whether the other object is of type int, float, complex
        or Complex (which is this class) and return a new complex number object
        of the Complex class.
        """
        if isinstance(other, (int, float)):
            return Complex(self.a + other, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        elif isinstance(other, complex):
            return Complex(self.a + other.real, self.b + other.imag)


    def __rsub__(self, other):
        """
        Right subtract function for the complex number.
        Takes in two objects, checks other - self.
        Checks whether the other object is of type int, float, complex
        or Complex (which is this class) and return a new complex number object
        of the Complex class.
        """
        if isinstance(other, (int, float)):
            return Complex(self.a - other, self.b)
        elif isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        elif isinstance(other, complex):
            return Complex(self.a - other.real, self.b - other.imag)


    def __rmul__(self, other):
        """
        Right multiplication function for the complex number.
        Takes in two objects, checks other * self.
        Checks whether the other object is of type int, float, complex
        or Complex (which is this class) and return a new complex number object
        of the Complex class.
        """
        if isinstance(other, (int, float)):
            return Complex(self.a * other, self.b * other)
        elif isinstance(other, Complex):
            return Complex(self.a*other.a - self.b*other*b, self.a*other.b + self.b*other.a)
        elif isinstance(other, complex):
            return Complex(self.a*other.real - self.b*other.imag, self.a*other.imag + self.b*other.real)

    def __neg__(self):
        """Return the negative of the number given. Returns type Complex"""
        return Complex(-self.a, -self.b)

    def __complex__(self):
        """Changes object from Complex to complex"""
        return complex(self.a, self.b)


def main():

    newObject = Complex(2.5, 4.5)
    newObject2 = Complex(2, 5)

    print(newObject + newObject2)
    print(newObject + 1)
    print(3 + newObject)
    print(3.45 * newObject)
    print(newObject2 * newObject)
    print(newObject2 * complex(1,2))
    print(newObject - newObject2)
    print(type(newObject.modulus()))

if __name__ == "__main__":

    main()