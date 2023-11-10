
def count_str(s, n):
    i = 0
    j = len(n)
    count = 0
    while j<=len(s):
        if s[i:j] == n:
            count += 1
            i = j
            j = j+len(n)
        else:
            i += 1
            j += 1
    return count

if __name__=="__main__":
    l = int(input())
    for i in range(l):
        s = input()
        n = input()
        print(count_str(s, n))
