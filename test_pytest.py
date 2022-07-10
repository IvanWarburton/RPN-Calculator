import RPN

def test_Addition():
    assert RPN.Calculate("1", "1", "+") == 2

def test_Subtraction():
    assert RPN.Calculate("2", "1", "-") == 1

def test_Multiplication():
    assert RPN.Calculate("2", "2", "*") == 4

def test_Division():
    assert RPN.Calculate("4", "2", "*") == 2