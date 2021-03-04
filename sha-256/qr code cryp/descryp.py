import jwt


key = "-v568i9,;jbomns54rbn80yt7tug"

def decript(code):
    decoded = jwt.decode(code,key, algorithms=["HS256"])
    print(decoded)
    return decoded

