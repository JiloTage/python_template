from src.sample import fizzbuzz


def test_fizzbuzz():
    """test fizzbuzz function."""
    fizzbuzz(15)

def test_fizzbuzz1(capfd):
    """test fizzbuzz(1)."""
    fizzbuzz(1)
    out, _ = capfd.readouterr()
    assert out == "1\n"

def test_fizzbuzz15(capfd):
    """test fizzbuzz(15)."""
    fizzbuzz(15)
    out, _ = capfd.readouterr()
    assert out == "1\n2\nFizz!\n4\nBuzz!\nFizz!\n7\n8\nFizz!\nBuzz!\n11\nFizz!\n13\n14\nFizz Buzz!\n"
