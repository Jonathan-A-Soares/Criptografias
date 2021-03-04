import base64

def crip(msg):

    message = msg
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)


print("Insira Text:")
inmsg = input()
crip(inmsg)