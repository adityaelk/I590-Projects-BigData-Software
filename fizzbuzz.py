def fizzbuzz(n):
    i = 1
    while(i <= n):
        if((i % 2 == 0) and (i % 3 == 0)):
            print "fizzbuzz"
            i += 1
        if(i % 2 == 0):
            print "fizz"
            i += 1
        if(i % 3 == 0):
            print "buzz"
            i += 1
        else:
            print i
            i +=1 
fizzbuzz(int(raw_input("Enter a number:")))
