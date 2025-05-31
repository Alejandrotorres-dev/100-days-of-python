extensions = input("File name: ")


if extensions == ("cat.gif"): 
    print("image/gif")

elif extensions == ("cat.jpg"): 
    print("image/jpeg")

elif extensions == ("cat.jpeg"): 
    print("image/jpeg")

elif extensions == ("cat.png"): 
    print("image/png")

elif extensions == ("cat.zip"): 
    print("application/zip")

else:
    print("application/octet-stream")