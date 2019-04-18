
if __name__ == '__main__':
    filt = pow(10,10)
    a = pow(2,7830457,filt)
    b = 28433 * a + 1
    c = b % filt
    print(c)