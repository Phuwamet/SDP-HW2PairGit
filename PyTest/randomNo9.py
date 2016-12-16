from random import randint
a=""
for x in range(1, 2):
    while 1:
        b=randint(0,9);
        if b==0 :
            a+=str(0);
        else:
            a+=str(b);
        if b==9 :
            break
    print "Lotto",x,a[:];
    a=""
