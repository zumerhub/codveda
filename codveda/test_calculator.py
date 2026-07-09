# Test cases for the calculator
import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_multiply():
    assert calculator.multiply(4, 2) == 8

def test_divide():
    assert calculator.divide(8, 2) == 4
    assert calculator.divide(8, 0) == "Error! Division by zero is not allowed."

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All test cases passed!")