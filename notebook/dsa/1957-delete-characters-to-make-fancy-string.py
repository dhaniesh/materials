import unittest

class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        count = 0
        result = ''

        for c in s:
            if c == prev:
                count += 1
            else:
                count = 1
                prev = c
            if count < 3:
                result += c
        return result


class TestMakeFancyString(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        s = "leeetcode"
        self.assertEqual(self.sol.makeFancyString(s), "leetcode")

    def test_case_2(self):
        s = "aaabaaaa"
        self.assertEqual(self.sol.makeFancyString(s), "aabaa")

    def test_case_3(self):
        s = "aabb"
        self.assertEqual(self.sol.makeFancyString(s), "aabb")

    def test_case_4(self):
        s = "xxxxxy"
        self.assertEqual(self.sol.makeFancyString(s), "xxy")

    def test_case_5(self):
        s = "abc"
        self.assertEqual(self.sol.makeFancyString(s), "abc")


if __name__ == "__main__":
    unittest.main()
    print("helloworld")

