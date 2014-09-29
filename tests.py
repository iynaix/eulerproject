#tests to ensure various utilities used by the euler project work as expected

import unittest
from utils import primes_gen, power_gen


class PrimeGeneratorTest(unittest.TestCase):
    #primes below 1000
    prs = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
           67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
           139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
           211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
           281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
           367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
           443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
           523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
           613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
           691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
           787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
           877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
           971, 977, 983, 991, 997]

    def test_endpoint(self):
        """tests the generator with only the endpoint given"""
        self.assertEqual(list(primes_gen(1000)), self.prs)

    def test_range(self):
        """tests the generator with the start and end points given"""
        prs = [x for x in self.prs if x >= 100]
        self.assertEqual(list(primes_gen(100, 1000)), prs)

    def test_inifite(self):
        """tests the generator with no start and end points given"""
        res = []
        for x in primes_gen():
            if x > 1000:
                break
            res.append(x)
        self.assertEqual(res, self.prs)


class SeqGeneratorTest(unittest.TestCase):
    #squares below 1000
    sqs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256,
           289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841,
           900, 961]

    def test_endpoint(self):
        """tests the generator with only the endpoint given"""
        self.assertEqual(list(power_gen(2, 1000)), self.sqs)

    def test_range(self):
        """tests the generator with the start and end points given"""
        sqs = [x for x in self.sqs if x >= 100]
        self.assertEqual(list(power_gen(2, 100, 1000)), sqs)

    def test_inifite(self):
        """tests the generator with no start and end points given"""
        res = []
        for x in power_gen(2):
            if x > 1000:
                break
            res.append(x)
        self.assertEqual(res, self.sqs)


if __name__ == '__main__':
    unittest.main()
