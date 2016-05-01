import urllib2
import hashlib
import itertools
import socket
import numpy as np

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.19.127.222",41000))
    s.settimeout(600)

    #s.sendall("0")

    data = s.recv(9999)
    for num in range(0,8):
        calc = s.recv(9999)
        print calc
        calc = calc.split(":")
        calc = calc[1].replace('\n','')
        print calc
        print eval(calc)
        rep = str(eval(calc))
        s.sendall(rep)

    step2 = s.recv(9999)
    print "Step 2"

    for num in range(0,8):
        print "Tour num " + str(num)

        data = s.recv(9999)

        print data
        if num >= 2:
            data = s.recv(9999)

        data = data.split(':')

        print data

        if num == 0:
            eq = data[2].split("\n")
        else:
            eq = data[0].split("\n")

        if num == 0:
            eq1 = eq[1]
            eq2 = eq[2]
        else:
            eq1 = eq[0]
            eq2 = eq[1]


        print "eq1: " + eq1
        print "eq2: " + eq2

        x1 = eq1.split('x')
        x1 = int(x1[0])

        y1 = eq1.split('y')
        y1 = y1[0].split(' ')
        y1 = int(y1[2])

        s1 = eq1.split('=')
        s1 = int(s1[1])

        x2 = eq2.split('x')
        x2 = int(x2[0])

        y2 = eq2.split('y')
        y2 = y2[0].split(' ')
        y2 = int(y2[2])

        s2 = eq2.split('=')
        s2 = int(s2[1])

        print 'x1 ' + str(x1)
        print 'y1 ' + str(y1)
        print 'x2 ' + str(x2)
        print 'y2 ' + str(y2)

        print str(s1)
        print str(s2)

        a = np.array([[x1,y1], [x2,y2]])
        b = np.array([s1,s2])
        sol = np.linalg.solve(a, b)

        x = sol[0]
        x = str(x)
        x = x.split(".")[0]
        s.sendall(x)


        data = s.recv(9999)
        print data
        y = sol[1]
        y = str(y)
        y = y.split(".")[0]
        s.sendall(y)

        if num == 0:
            data = s.recv(9999)
            print data

    data = s.recv(9999)
    print data

    for num in range(0,9):
        print 'Derivees tour ' + str(num)
        data = s.recv(9999)
        print data
        data = data.split(":");
        val = data[0]
        val = val.split("=")
        val = val[1]
        val = int(val)
        print "val : " + str(val)

        q=int(0)
        m=int(0)
        d=int(0)
        f=int(0)
        g=int(0)
        h=int(0)
        j=int(0)
        k=int(0)
        l=int(0)
        r=int(0)

        if num == 0:
            eq = data[1].split("\n")
            eq = str(eq[1])
            eq = eq.split("=")
            eq = str(eq[1])
            eq = eq[1:]
            print "Equation :" + eq

            n = eq[0]

            try:
              eq[3]
            except NameError:
              pwr = 0
            else:
              pwr = int(eq[3])



            if pwr == 1:
                l=n
                print n+"^1"
            elif pwr == 2:
                k=n
                print n+"^2"
            elif pwr == 3:
                j=n
                print n+"^3"
            elif pwr == 4:
                h=n
                print n+"^4"
            elif pwr == 5:
                g=n
                print n+"^5"
            elif pwr == 6:
                f=n
                print n+"^6"
            elif pwr == 7:
                d=n
                print n+"^7"
            elif pwr == 8:
                m=n
                print n+"^8"
            elif pwr == 9:
                q=n
                print n+"^9"
            elif pwr == 0:
                q=r
                print n

            p = np.poly1d([int(q),int(m),int(d),int(f),int(g),int(h),int(j),int(k),int(l), int(r)])

            print p
            q = p.deriv()
            print q

            fin = str(q(val))

            s.sendall(fin)
        else:
            data = s.recv(9999)
            print data
            data = data.split("=")
            data = data[1].split("\n")
            data = data[0]
            print data

            mbrs = data.split(" ")
            for nomnul in mbrs:
                if '+' in mbrs:
                    mbrs.remove('+')
            mbrs.remove('')
            for oklm in mbrs:
                n = oklm[0]
                try:
                  oklm[3]
                except IndexError:
                  pwr = 0
                else:
                  pwr = int(oklm[3])


                if pwr == 1:
                    if l != 0:
                        l = int(l) +int(n)
                    else:
                        l=n
                    print n+"^1"
                elif pwr == 2:
                    if k != 0:
                        k= int(k) + int(n)
                    else:
                        k=n
                    print n+"^2"
                elif pwr == 3:
                    if j != 0:
                        j = int(j) + int(n)
                    else:
                        j=n
                    print n+"^3"
                elif pwr == 4:
                    if h != 0:
                        h = int(h) + int(n)
                    else:
                        h=n
                    print n+"^4"
                elif pwr == 5:
                    if g != 0:
                        g = int(g) + int(n)
                    else:
                        g=n
                    print n+"^5"
                elif pwr == 6:
                    if f != 0:
                        f = int(f) + int(n)
                    else:
                        f=n
                    print n+"^6"
                elif pwr == 7:
                    if d != 0:
                        d = int(d) + int(n)
                    else:
                        d=n
                    print n+"^7"
                elif pwr == 8:
                    if m != 0:
                        m = int(m) + int(n)
                    else:
                        m=n
                    print n+"^8"
                elif pwr == 9:
                    if q != 0:
                        q = int(q) + int(n)
                    else:
                        q=n
                    print n+"^9"
                elif pwr == 0:
                    if r != 0:
                        r = int(r) + int(n)
                    else:
                        r=n
                    print n

            p = np.poly1d([int(q),int(m),int(d),int(f),int(g),int(h),int(j),int(k),int(l), int(r)])

            print p

            q = p.deriv()
            print q

            fin = str(q(val))

            s.sendall(fin)
