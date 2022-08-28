import sys
import unittest
from primality import * 
from sieveOfEratosthenes import *
from random import randint
class prime_test(unittest.TestCase):
    
    def test_base(self): #check if accurate up to 10^5, check against sieve
        """
        note: with 100000 calls to the function and each call taking O((log n)^3)
        time, this test is expected to take a few seconds.
        """
        n = 100000
        s = sieve(n)
        for i in range(n+1):
            assert prime(i) == s[i]
    
    def test_rspeed(self): #test speed with random values
        #only starts slows down noticably around 10**200ish
        n = 10**100
        for i in range(100):
            prime(randint(1,n))

    def test_largep(self): #tests with 50 digit primes
        large = [22953686867719691230002707821868552601124472329079,
30762542250301270692051460539586166927291732754961,
29927402397991286489627837734179186385188296382227,
46484729803540183101830167875623788794533441216779,
95647806479275528135733781266203904794419563064407,
64495327731887693539738558691066839103388567300449,
58645563317564309847334478714939069495243200674793,
48705091355238882778842909230056712140813460157899,
15452417011775787851951047309563159388840946309807,
53542885039615245271174355315623704334284773568199]
        for i in range(10):
            assert prime(large[i])
    
    def test_semiprime(self): #tests with semiprimes from 2 30-digit primes
        large = [671998030559713968361666935769,
282174488599599500573849980909,
521419622856657689423872613771,
362736035870515331128527330659,
115756986668303657898962467957,
590872612825179551336102196593,
564819669946735512444543556507,
513821217024129243948411056803,
416064700201658306196320137931,
280829369862134719390036617067]
        for i in range(10):
            x = large[randint(0,9)]*large[randint(0,9)]
            assert not prime(x)

    def test_carmichael(self): #test that carmichael values fail
        c = [825265,
             321197185,
             5394826801,
             232250619601,
             9746347772161,
             1436697831295441,
             60977817398996785,
             7156857700403137441,
             1791562810662585767521,
             87674969936234821377601,
             6553130926752006031481761,
             1590231231043178376951698401]
        for i in range(len(c)):
            assert not prime(c[i])


if __name__ == "__main__":
    unittest.main()
