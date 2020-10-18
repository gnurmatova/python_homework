from midterm import converter

def test_currencyConverter():
    assert converter( "USD", "USD", "30") == "30 in USD = 30 in USD"
    assert converter( "INR", "INR", "30") == "30 in INR = 30 in INR"
    assert converter( "ert", "USD", "30") == "ERROR: Invalid API endpoint"
    assert converter( "USD", "ert", "30") == "Country code(s) doesn't exist"
    assert converter( "USD", "TTT", "30") == "Country code(s) doesn't exist"
    assert converter( "TTT", "USD", "30") == "ERROR: Invalid API endpoint"

test_currencyConverter()
