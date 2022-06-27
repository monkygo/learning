

def getAllSubstrings(s):
    subs = {}
    for i in range(len(s) - 1):
        for j in range(len(s) - i):
            sub = "".join(sorted(s[j:j + i + 1]))
            subs[sub] = subs.get(sub, 0) + 1
    return subs

def pairAnagramCount(list):
    cnt = 0
    for n in list.values():
        calc = (n * (n - 1)) // 2
        cnt += calc
    return cnt

a = "mom" #2
b = "abba" #4
c = "abcd" #0
d = "ifailuhkqq" #3
e = "kkkk" #10
f = "cdcd" #5

subAs = getAllSubstrings(a)
subBs = getAllSubstrings(b)
subCs = getAllSubstrings(c)
subDs = getAllSubstrings(d)
subEs = getAllSubstrings(e)
subFs = getAllSubstrings(f)

cntA = pairAnagramCount(subAs)
cntB = pairAnagramCount(subBs)
cntC = pairAnagramCount(subCs)
cntD = pairAnagramCount(subDs)
cntE = pairAnagramCount(subEs)
cntF = pairAnagramCount(subFs)

print(cntA)
print(cntB)
print(cntC)
print(cntD)
print(cntE)
print(cntF)