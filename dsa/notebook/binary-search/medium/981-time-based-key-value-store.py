"""
981. Time Based Key-Value Store (Medium)

Design a time-based key-value data structure that supports the following operations:
- `set(key, value, timestamp)`: Store the key-value pair, along with the given timestamp.
- `get(key, timestamp)`: Return the value of the key at the given timestamp or the value at the closest timestamp less than or equal to the given timestamp.

It is guaranteed that for every call to `get`, there will be at least one `set` call with the given key.

Example 1:
Input:
["TimeMap", "set", "get", "set", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", "bar2", 4], ["foo", 4]]
Output:
[null, null, "bar", null, "bar2"]

Example 2:
Input:
["TimeMap", "set", "get", "get", "set", "get"]
[[], ["love", "high", 10], ["love", 10], ["love", 20], ["love", "low", 30], ["love", 10]]
Output:
[null, null, "high", "high", null, "low"]

Constraints:
- 1 <= key.length, value.length <= 100
- 1 <= timestamp <= 10^7
- All `set` operations are guaranteed to be called before `get` operations.
- At most 2 * 10⁵ calls will be made to `set` and `get`.
"""

from typing import List
import unittest

"""
Approach:
We will store the values and timestamps in a dictionary, where the key is the string key, 
and the value is a list of tuples (timestamp, value). We will use binary search to efficiently 
find the value at the closest timestamp.
"""

class TimeMap:

    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


class TestTimeMap(unittest.TestCase):
    def setUp(self):
        self.time_map = TimeMap()

    def test_example_1(self):
        self.time_map.set("foo", "bar", 1)
        self.assertEqual(self.time_map.get("foo", 1), "bar")
        self.time_map.set("foo", "bar2", 4)
        self.assertEqual(self.time_map.get("foo", 4), "bar2")

    def test_example_2(self):
        self.time_map.set("love", "high", 10)
        self.assertEqual(self.time_map.get("love", 10), "high")
        self.assertEqual(self.time_map.get("love", 20), "high")
        self.time_map.set("love", "low", 30)
        self.assertEqual(self.time_map.get("love", 10), "high")

    def test_single_set_get(self):
        self.time_map.set("key", "value", 1)
        self.assertEqual(self.time_map.get("key", 1), "value")

    def test_no_matching_get(self):
        self.time_map.set("key", "value", 5)
        self.assertEqual(self.time_map.get("key", 3), "")

    def test_empty_key(self):
        self.time_map.set("key", "value", 1)
        self.assertEqual(self.time_map.get("", 1), "")

if __name__ == "__main__":
    unittest.main()
