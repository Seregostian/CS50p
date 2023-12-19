from numb3rs import validate

def main():

    test_ip_formats()
    test_ip_ranges()


def test_ip_formats():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False


def test_ip_ranges():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("33.44.55.66") == True
    assert validate("191.919.282.828") == False
    assert validate("249.249.249.249") == True
    assert validate("david") == False
    assert validate("malan") == False
    assert validate("1.2.3.4") == True

if __name__ == '__main__':
    main()