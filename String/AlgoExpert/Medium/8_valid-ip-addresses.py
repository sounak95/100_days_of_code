

def isValidIpAddress(string):
    if int(string)>255:
        return False
    return len(str(int(string)))==len(string)

def validIPAddresses(string):
    # Write your code here.
    ipAddressesFound=[]
    n=len(string)
    for i in range(1,min(n,4)):
        currentIpAddressParts=["","","",""]
        currentIpAddressParts[0]=string[:i]
        if not isValidIpAddress(currentIpAddressParts[0]):
            continue
        for j in range(i+1, i+min(n-i,4)):
            currentIpAddressParts[1]=string[i:j]
            if not isValidIpAddress(currentIpAddressParts[1]):
                continue
            for k in range(j+1, j+min(n-j,4)):
                currentIpAddressParts[2] = string[j:k]
                currentIpAddressParts[3] = string[k:]
                if isValidIpAddress(currentIpAddressParts[2]) and isValidIpAddress(currentIpAddressParts[3]):
                    ipAddressesFound.append(".".join(currentIpAddressParts))
    return ipAddressesFound

print(validIPAddresses("1921680"))