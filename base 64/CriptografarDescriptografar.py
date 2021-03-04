import base64

def crip(msg):

    message = msg
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)

def descrip(cripmsg):

    base64_message = cripmsg
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)

print("Cripitografar: 1")
print("Descripitografar: 2")
print("selecione:")
option = int(input())
print(option)

if(option==1):

    print("Insira Text:")
    inmsg = input()
    crip(inmsg)
else:
    if(option==2):

        print("Insira Cripitografia:")
        incrip = input()
        descrip(incrip)
    else:
        print("Erro")



