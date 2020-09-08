from Crypto import  Signature
import  base64
from Crypto.PublicKey import RSA

def sign(str):
    with open(file='./data',mode='r')as f :
        s=f.read()
    key = RSA.import_key(s)
    sortdata = oprint(str,True)
    hSigVal = Signature.PKCS1_v1_5.new(key).sign(sortdata)
    return base64.b64decode(hSigVal)




def parseobj(v, ini):
    # console.log(v, "not array");

    ir = []
    for  j in v:
        if j == "sign":
            continue
        if v[j] is 'object':
          #   console.log(v, j, "is object");
            if ini:
                ir.append(j + "=" + oprint(v[j], False))
            else:
                ir.append(j + ":" + oprint(v[j], False))

        else:
          #   console.log(v, j, "not object");
            if ini:
                ir.append(j + "=" + v[j])
            else:
                ir.append(j + ":" + v[j])



    ir.sort()
    if ini:
        vv = ir.join("&")
    else:
        vv = "map[" + ir.join(" ") + "]"

    return vv


def parsearr(v):
    ir = []
    for  i in v:
        if v[i] is 'object':
            ir.append(oprint(v[i], False))
        elif type(v[i])=='list' :
            ir.append(parsearr(v[i]))
        else:
            ir.append(v[i])


    vv = "[" + ir.join(" ") + "]"
    return vv
def oprint(v, ini):

    if  v is 'object':
        if type(v)=='list':
            vv = parsearr(v)
        else:
            vv = parseobj(v, ini)

    else:
        vv = v

    # console.log(vv);
    return vv
