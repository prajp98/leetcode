def findComplement(self, num: int) -> int:
    b = bin(num)[2:]
    res = ""
    for i in range(len(b)):
        if b[i] == '0':
            res += '1'
        else:
            res += '0'
    return int(res, 2)

def findComplement(self, num: int) -> int:
    b=bin(num)[2:]
    res=""
    for i in range(len(b)):
        if b[i]=='0':
            res+='1'
        else:
            res+='0'
    return int(res,2)