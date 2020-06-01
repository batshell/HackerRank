import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    a = {}
    for i in ar:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    for i in a:
        while a[i] > 1:
            count += 1
            a[i] -= 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
