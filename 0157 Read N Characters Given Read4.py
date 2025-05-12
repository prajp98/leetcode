def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Number of characters to read (int)
    :rtype: The number of actual characters read (int)
    """
    res, k = 0, 4
    buf4 = [" "] * 4
    while res < n and k == 4:
        k = read4(buf4)
        buf[res: res + 4] = buf4
        res += k
    return min(n, res)