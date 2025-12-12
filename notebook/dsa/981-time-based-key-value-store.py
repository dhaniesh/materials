"""
981. Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""

import unittest

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            t, v = arr[mid]

            if t == timestamp:
                return v
            elif t < timestamp:
                res = v
                l = mid + 1
            else:
                r = mid - 1

        return res


class TestTimeMap(unittest.TestCase):

    def test_example_1(self):
        ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
        args = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
                ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

        obj = None
        result = []

        for op, arg in zip(ops, args):
            if op == "TimeMap":
                obj = TimeMap()
                result.append(None)
            elif op == "set":
                result.append(obj.set(*arg))
            elif op == "get":
                result.append(obj.get(*arg))

        expected = [None, None, "bar", "bar", None, "bar2", "bar2"]
        self.assertEqual(result, expected)

    def test_empty_key(self):
        obj = TimeMap()
        self.assertEqual(obj.get("no_key", 10), "")

    def test_multiple_keys(self):
        obj = TimeMap()
        obj.set("a", "x", 1)
        obj.set("b", "y", 2)

        self.assertEqual(obj.get("a", 1), "x")
        self.assertEqual(obj.get("b", 2), "y")
        self.assertEqual(obj.get("a", 5), "x")
        self.assertEqual(obj.get("b", 1), "")

    def test_exact_and_closest(self):
        obj = TimeMap()
        obj.set("foo", "a", 5)
        obj.set("foo", "b", 10)
        obj.set("foo", "c", 15)

        self.assertEqual(obj.get("foo", 10), "b")  # exact
        self.assertEqual(obj.get("foo", 14), "b")  # closest below
        self.assertEqual(obj.get("foo", 4), "")    # none below


if __name__ == "__main__":
    unittest.main()

