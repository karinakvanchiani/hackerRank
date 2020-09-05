if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    new = set(arr)
    max_value = max(arr)
    new.remove(max_value)

    
    print(max(new))
