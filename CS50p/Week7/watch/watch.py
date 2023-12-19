import re

def main():

  print(parse(input("HTML: ")))


def parse(html_string):

  matches = re.search(r"src=\"http(?:s)?://(?:www.)?youtube\.com/embed/(\w+)\"", html_string)
  if matches:
    return f"https://youtu.be/{matches.group(1)}"
  else:
    return None

if __name__ == "__main__":
    main()