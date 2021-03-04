import base64

def descrip(cripmsg):

    base64_message = cripmsg
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)


print("Insira Cripitografia:")
incrip = input()
descrip(incrip)
