from complex import Complex

def test_complex():
    """
    Test function
    Tests addition, subtraction and multiplication between 
    type Complex-Complex, type Complex-Int, modulus method
    and conjugate method
    """
    number = Complex(2, 4)
    number2 = Complex(0, 1)
    number3 = Complex(0, 0)
    number4 = Complex(3, 4)
    assert (number + 1) == Complex(3, 4)
    assert (number - 1) == Complex(1, 4)
    assert (number * 2) == Complex(4, 8)
    assert (number + number2) == Complex(2, 5)
    assert (number - number2) == Complex(2, 3)
    assert (number * number2) == Complex(-4, 2)
    assert (number * number3) == Complex(0, 0)
    assert (number4.modulus()) == 5.0
    assert (number.conjugate()) == Complex(2, -4)

def test_complex_floats():
    """
    Test function
    Tests addition, subtraction and multiplication between 
    type Complex-Complex with floats, type Complex-float, modulus method with floats
    and conjugate method with floats
    """
    tol = 1e-10
    number = Complex(2.5, 4.5)
    number2 = Complex(0, 0.5)
    number3 = Complex(0, 0)
    assert (number + 1) == Complex(3.5, 4.5)
    assert (number - 1) == Complex(1.5, 4.5)
    assert (number + number2) == Complex(2.5, 5)
    assert (number - number2) == Complex(2.5, 4)
    assert (number * number2) == Complex(-2.25, 1.25)
    assert (number * number3) == Complex(0, 0)
    assert abs(number.modulus() - 5.1478150704935) < tol
    assert (number.conjugate()) == Complex(2.5, -4.5)

def test_complex_complex():
    """
    Test function
    Tests addition, multiplication and subtraction between
    type Complex-complex
    Tests __eq__ method, __neg__ method and __complex__ method
    """
    tol = 1e-10
    number = Complex(2, 5)
    number2 = complex(1, 2)
    number3 = complex(2, 5)
    assert (number + number2) == Complex(3, 7)
    assert (number * number2) == Complex(-8, 9)
    assert number == number3
    assert Complex(1,0) == 1
    assert type(complex(number)) == type(number2)

def test_right_operation():
    """
    Test function
    Tests right operation for addition, multiplication and subtraction
    """
    number = Complex(2, 4)
    number2 = Complex(0, 1)
    number3 = Complex(0, 0)
    number4 = Complex(3, 4)
    assert (1 + number) == Complex(3, 4)
    assert (1 - number) == Complex(1, 4)
    assert (2 * number) == Complex(4, 8)
    assert (number2 + number) == Complex(2, 5)
    assert (number2 - number) == Complex(-2, -3)
    assert (number2 * number) == Complex(-4, 2)