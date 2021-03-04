import jwt


key = "-v568i9,;jbomns54rbn80yt7tug"

def cript(key1,code):
    encoded = jwt.encode({
        "msg":code
        
    
    }, key, algorithm="HS256")
    print(encoded)
    return encoded

