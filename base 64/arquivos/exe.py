import base64
data = open("putty.txt", "r").read()
encoded = base64.b64encode(data)
print(data)

        