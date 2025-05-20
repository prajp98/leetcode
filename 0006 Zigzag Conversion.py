def convert(self, s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    i, step = 0, 1

    for char in s:
        rows[i] += char
        if i == 0:
            step = 1
        elif i == numRows - 1:
            step = -1
        i += step

    return ''.join(rows)