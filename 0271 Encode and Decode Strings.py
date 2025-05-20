class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        arr=[]
        for s in strs:
            arr.append(str(len(s))+"#"+s)
        return ''.join(arr)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        arr=[]
        i=0
        j=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            j+=1
            arr.append(s[j:j+length])
            i=j+length
        return arr