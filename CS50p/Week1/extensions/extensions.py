file_name = input("File name: ").lower().strip()
check = file_name[-4:]

if check == ".gif" in file_name:
    print("image/gif")

#placing jpg and jpeg together seems like a great idea, since they're practically the same. I just hope the reviewer doesn't make a fuzz about it

elif check == ".jpg" in file_name or file_name[-5:] == ".jpeg" in file_name:
    print("image/jpeg")

elif check == ".png" in file_name:
    print("image/png")
elif check == ".pdf" in file_name:
    print("application/pdf")
elif check == ".txt" in file_name:
    print("text/plain")
elif check == ".zip" in file_name:
    print("application/zip")

else:
    print("application/octet-stream")