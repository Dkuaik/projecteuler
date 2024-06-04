import unittest
import assertpy
import primes
print(primes.is_prime(4))
# class Primes(unittest.TestCase):
#     def test_value_prime(self):
#         assertpy.assert_that(primes.is_prime(4)).is_false()
#         assertpy.assert_that(primes.is_prime(5)).is_true()
#         assertpy.assert_that(primes.is_prime(1)).is_false()
#     def test_error_prime(self):
#         try:
#             primes.is_prime(-1)
#         except ValueError: 
#             assert True
#         else:
#             assert False
