a = [1,2,3,4,5,6]

def reverse(a):
    left = 0
    right = len(a)-1
    while left<right:
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        left+=1
        right-=1
    return a


def reverse1(a):
    return a[::-1]

l = []
x = []
def reverse2(a):
    for i in a:
        l.insert(0,i)
    return l

print(reverse2(a))
