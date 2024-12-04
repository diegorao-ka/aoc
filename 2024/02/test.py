import unittest

from script import _is_safe

class Test(unittest.TestCase):
    def testIsSafeDampened(self):
        # Safe without removing any levels.
        self.assertTrue(_is_safe([7, 6, 4, 2, 1], False))
        self.assertTrue(_is_safe([1, 3, 6, 7, 9], False))

        # Unsafe no matter which level is removed.
        self.assertFalse(_is_safe([1, 2, 7, 8, 9], True))
        self.assertFalse(_is_safe([9, 7, 6, 2, 1], True))

        # Safe removing one level (the second).
        self.assertFalse(_is_safe([1, 3, 2, 4, 5], False))
        self.assertTrue(_is_safe([1, 3, 2, 4, 5], True))

        # Safe removing one level (the third).
        self.assertFalse(_is_safe([8, 6, 4, 4, 1], False))
        self.assertTrue(_is_safe([8, 6, 4, 4, 1], True))

        # Safe removing one level (the first).
        self.assertFalse(_is_safe([9, 1, 2, 3, 4], False))
        self.assertTrue(_is_safe([9, 1, 2, 3, 4], True))

        # Safe removing one level (the last).
        self.assertFalse(_is_safe([1, 2, 3, 4, 9], False))
        self.assertTrue(_is_safe([1, 2, 3, 4, 9], True))

        # Case that tripped me up
        self.assertFalse(_is_safe([88, 86, 88, 89, 90, 93], False))
        self.assertTrue(_is_safe([88, 86, 88, 89, 90, 93], True))


if __name__ == '__main__':
    unittest.main()