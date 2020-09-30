from homework5_bunnies import bunnyEars

def test_bunnyEars():
    assert bunnyEars(0) == 0
    assert bunnyEars(1) == 2
    assert bunnyEars(2) == 5
    assert bunnyEars(3) == 7

test_bunnyEars()