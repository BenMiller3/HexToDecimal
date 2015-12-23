def ex(num):
    result = 0
    num = str(num)
    ans = [0]*len(num)
    for i in range(len(num)):
        if(num[i]==('0')):
            ans[i] = 0
        elif(num[i]==('1')):
            x = 2 ** (4*(len(num)-i-1))
            ans[i] = x
        elif(num[i]==('2')):
            x = 2 ** (4*(len(num)-i-1) + 1)
            ans[i] = x
        elif(num[i]==('3')):
            x = (2 ** (4*(len(num)-i-1) + 1) + 2 ** (4*(len(num)-i-1)))
            ans[i] = x
        elif(num[i]==('4')):
            x = 2 ** (4*(len(num)-i-1) + 2)
            ans[i] = x
        elif(num[i]==('5')):
            x = 2 ** (4*(len(num)-i-1) + 2) + 2 ** (4*(len(num)-i-1))
            ans[i] = x
        elif(num[i]==('6')):
            x = 2 ** (4*(len(num)-i-1) + 2) + 2 ** (4*(len(num)-i-1) + 1)
            ans[i] = x
        elif(num[i]==('7')):
            x = 2 ** (4*(len(num)-i-1) + 2) + 2 ** (4*(len(num)-i-1) + 1) + 2 ** (4*(len(num)-i-1))
            ans[i] = x
        elif(num[i]==('8')):
            x = 2 ** (4*(len(num)-i-1) + 3)
            ans[i] = x
        elif(num[i]==('9')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1))
            ans[i] = x
        elif(num[i]==('a')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1) + 1)
            ans[i] = x
        elif(num[i]==('b')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1) + 1) + 2 ** (4*(len(num)-i-1))
            ans[i] = x
        elif(num[i]==('c')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1) + 2)
            ans[i] = x
        elif(num[i]==('d')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1) + 2) + 2 ** (4*(len(num)-i-1))
            ans[i] = x
        elif(num[i]==('e')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1) + 2) + 2 ** (4*(len(num)-i-1) + 1)
            ans[i] = x
        elif(num[i]==('f')):
            x = 2 ** (4*(len(num)-i-1) + 3) + 2 ** (4*(len(num)-i-1) + 2) + 2 ** (4*(len(num)-i-1) + 1) + 2 ** (4*(len(num)-i-1)) 
            ans[i] = x

    for i in range(len(num)):
        result = ans[i] + result
    return result

def main():
    run = True
    print(" --- Hex to Decimal Converter ---\nType * at any time to quit")
    while(run==True):
        num = input("\nPlease enter a hex number to be changed to decimal (lowercase): ")
        if(num=="*"):
            run = False
        else:
            ans = ex(num)
            print("\n",num, "as a decimal is: ",ans)
        

main()
