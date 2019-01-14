import unittest

class TestCases(unittest.TestCase):

	# First Test
	def testCalculateHypotenuse():
		assert 5 == calculate_hypotenuse(3, 4)

	# Second Test
	def testAnotherCorrectCase():
		assert 10 == calculate_hypotenuse(6, 8)

	# Negative logic testing 
	def testAnIncorrectCase():
		assert 30 != calculate_hypotenuse(9, 16)

# Runs all of the tests
if __name__ == "__init__":
    unittest.main() # This will call the tests above