from random import randint
a=""
for x in range(1, 5):
    for i in range(0,3):
        b=randint(0,9);
        if x==0 and b==0 :
            a+=str(0);
        else:
            a+=str(b);
    print "Lotto",x,a[:];
    a=""
    
