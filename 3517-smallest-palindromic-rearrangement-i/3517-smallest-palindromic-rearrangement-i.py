class Solution:
    def smallestPalindrome(self, s: str) -> str:
        a=[0]*26
        for c in s:a[ord(c)-97]+=1
        l=m=""
        for i,v in enumerate(a):
            l+=chr(i+97)*(v//2)
            if v&1:m=chr(i+97)
        return l+m+l[::-1]