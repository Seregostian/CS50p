from plates import is_valid

#error messages:
#test_plates catches plates.py without beginning alphabetical checks
#test_plates catches plates.py without length checks
#test_plates catches plates.py without checks for number placement
#test_plates catches plates.py without checks for zero placement
#test_plates catches plates.py without checks for alphanumeric characters
#tl:dr gotta test : alphabetical & alphanumeric, lenght, number placement, zero placement

def test_bounds():
  assert not is_valid("LenghtOverSixCharacters")
  assert not is_valid("X")
  assert is_valid("XD") #haha XD

def test_special_chars():
  assert not is_valid("???")
  assert not is_valid(" CS50 ")
  assert not is_valid("PI3.14")

def test_zero_placement():
  assert is_valid("CS50")
  assert not is_valid("CS05")

def test_numbers_placement():
  assert not is_valid("50CS")
  assert not is_valid("123456")
  assert is_valid("AAA222")
  assert not is_valid("AAA22A")