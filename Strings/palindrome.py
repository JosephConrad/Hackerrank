def isPalindrome(l):
    return l==l[::-1]

def lin(s):
    i=0; j=len(s)-1
    while i<j and s[i]==s[j]:
        i+=1
        j-=1
    if i>=j: return -1
    if isPalindrome(s[i+1:j+1]): return i
    if isPalindrome(s[i:j]): return j

def main():
    for i in range(int(raw_input())):
        string = str(raw_input())
        print lin(list(string))

main()
