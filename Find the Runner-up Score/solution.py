if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    newarr = set(list(arr))
    newarr.remove(max(newarr))
    
    print(max(newarr))
