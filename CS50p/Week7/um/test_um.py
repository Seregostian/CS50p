from um import count

def main():
    test_capslock()
    test_contains_um()
    test_spaces()

def test_capslock():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
    assert count('hello, um, world') == 1


def test_contains_um():
    assert count('yummi') == 0
    assert count('maximum') == 0
    assert count('chromium') == 0
    assert count('album') == 0
    assert count('lumpy') == 0
    assert count('autumn') == 0


def test_spaces():
    assert count(' um ') == 1
    assert count(' um? ') == 1
    assert count(' Um thanks for the album. ') == 1
    assert count(' Um thanks um... ') == 2
    assert count(' hello um world ') == 1




if __name__ == "__main__":
    main()