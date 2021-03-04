import jwt
import json


def cript():
    encoded = jwt.encode(
        {
            "Code": "eTc1aXRnaDg5NTd0Z2g4ZXd2OTU3dGdtOXc4NzVoZjg3NWZ0Z2h5NzU4eQ=="
        }, "3645487365783465789346", algorithm="HS256")
        
    print(encoded)
    return encoded

def decript(code):
    decoded = jwt.decode(code, "3645487365783465789346", algorithms=["HS256"])
    print(decoded)
    return decoded

crippt = cript()

dados = decript(crippt)
    
with open( 'daos.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)