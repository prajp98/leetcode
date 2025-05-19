def validIPAddress(self, queryIP: str) -> str:
    def ipv4(ip):
        nums = ip.split(".")
        for num in nums:
            if not num.isdigit() or not 0 <= int(num) <= 255:
                return False
            if num[0] == "0" and len(num) > 1:
                return False
        return True

    def ipv6(ip):
        nums = ip.split(":")
        s = "0123456789abcdefABCDEF"
        for num in nums:
            if not 1 <= len(num) <= 4:
                return False
            for ch in num:
                if ch not in hexdigits:
                    return False
        return True

    if queryIP.count(".") == 3 and ipv4(queryIP):
        return "IPv4"
    elif queryIP.count(":") == 7 and ipv6(queryIP):
        return "IPv6"
    else:
        return "Neither"