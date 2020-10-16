#program to find the second largest item in a list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(set(arr))
    arr.sort()
    print(arr[-2])