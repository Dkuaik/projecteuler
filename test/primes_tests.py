import unittest
import assertpy
import Modulos as md

class Primes(unittest.TestCase):
    def test_value_isPrime(self):
        first_ten_primes=[2,3,5,7,11,13,17,19,23,29]
        primes_prube=[]
        for i in range(10):
            primes_prube.append(md.isPrime(first_ten_primes[i]))
        assertpy.assert_that(primes_prube).is_equal_to([True,True,True,True,True,True,True,True,True,True])