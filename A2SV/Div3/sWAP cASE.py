def swap_case(s):
    ans=''
    for i in range(len(s)):
        if s[i].islower():
            ans+=(s[i].upper())
        else:
            ans+=(s[i].lower())
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
