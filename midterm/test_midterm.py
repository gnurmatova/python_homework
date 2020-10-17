from midterm.py import converter

def test_currencyConverter():
    assert converter("30", "USD", "USD") == "30.0 in USD = 30.0 in USD"
    assert converter("30", "INR", "INR") == "30.0 in INR = 30.0 in INR"
    assert converter("30", "ert", "USD") == "ERROR: Invalid API endpoint"
    assert converter("30", "USD", "ert") == "Country code(s) doesn't exist"
    assert converter("30", "USD", "TTT") == "Country code(s) doesn't exist"
    assert converter("30", "TTT", "USD") == "ERROR: Invalid API endpoint"

test_currencyConverter()