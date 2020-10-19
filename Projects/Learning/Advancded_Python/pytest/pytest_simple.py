#using pytest is simplar then unittest you dont have to remember different assert functions and can do it all in one file
def rectangle_perimeter(length, height)
    return 2*(length + height)

def test_perimeter():
    assert rectangle_perimeter(5, 7) == 24