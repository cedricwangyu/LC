def validIP4(IP):
    IP4 = IP.split('.')
    if (len(IP4) == 4) and (all([item.isdigit() for item in IP4])):
        for item in IP4:
            if(item[0] == '0') and (len(item) > 1):
                return False
            else:
                num = int(item)
                if (num < 0) or (num > 255):
                    return False
        return True
    return False

def validIP6(IP):
    IP6 = IP.split(':')
    if (len(IP6) == 8) and (all([len(item) >= 1 for item in IP6])) and (all([len(item) <= 4 for item in IP6])):
        A = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
        for item in list("".join(IP6).lower()):
            if item not in A:
                return False
        return True
    
    return False

class Solution:
    
    def validIPAddress(self, IP: str) -> str:
        if validIP4(IP):
            return "IPv4"
        elif validIP6(IP):
            return "IPv6"
        else:
            return "Neither"
        