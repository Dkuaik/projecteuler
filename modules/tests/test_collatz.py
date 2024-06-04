import unittest
import assertpy

# def collatz(n):
#     if n <= 0:
#         raise ValueError("Input must be a positive integer")
#     if n % 2 == 0:
#         return n // 2
#     else:
#         return 3 * n + 1

# class Collatz(unittest.TestCase):
#     def test_value_collatz(self):
#         assertpy.assert_that(collatz(4)).is_equal_to(2)
#         assertpy.assert_that(collatz(5)).is_equal_to(16)
#         assertpy.assert_that(collatz(1)).is_equal_to(4)
#     def test_error_collatz(self):
#         try:
#             collatz(0)
#         except ValueError: 
#             assert True
#         else:
#             assert False