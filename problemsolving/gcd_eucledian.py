def gcd_eucledian(x,y):
    while x>0 and y>0:
        if x>=y : 
            x = x % y
        else:
            y = y % x
    print (max(x,y))
    return max(x,y)

if __name__ == "__main__":
    gcd_eucledian(20,50)
    gcd_eucledian(99929,30)