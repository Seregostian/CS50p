import re

def main():
  print(validate(input("IPv4 Address: ")))


def validate(ip_address):

  matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip_address)
  if matches:
    for number in matches.groups():
      if int(number) > 255:
        return False
    return True
  else:
    return False

if __name__ == '__main__':
    main()