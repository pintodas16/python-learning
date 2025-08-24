def gcd(x,y):
    gcd = 1
    for i in range(1,min(x,y)+1):
        # print(i)
        if x % i == 0 and y%i == 0:
            gcd = i 
        
    print(gcd)
    return gcd

if __name__ == "__main__":
    gcd(12,20)


# time complexity (O(min(x,y))) it's linear approach 