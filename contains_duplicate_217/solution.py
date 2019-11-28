import unittest
from typing import List


class ContainsDuplicatesIn:
    def __init__(self, source: List[int]):
        self.__source = source

    def __bool__(self) -> bool:
        return len(set(self.__source)) != len(self.__source)


class ContainsDuplicatesInOneIteration:
    def __init__(self, source: List[int]):
        elements = set()
        self.__value = False
        for item in source:
            if item in elements:
                self.__value = True
            elements.add(item)

    def __bool__(self):
        return self.__value


class ContainsDuplicatesTest(unittest.TestCase):

    def test_when_checking_duplicates_in_list_with_duplicates_expect_true(self):
        # given:
        subject = [1, 2, 2, 3]
        # when:
        result = ContainsDuplicatesIn(subject)
        # then:
        self.assertTrue(result)

    def test_when_checking_duplicates_in_list_with_uniques_expect_false(self):
        # given:
        subject = [1, 2, 3, 4]
        # when:
        result = ContainsDuplicatesIn(subject)
        # then:
        self.assertFalse(result)

    def test_when_checking_duplicates_in_empty_list_expect_false(self):
        # given:
        subject = []
        # when:
        result = ContainsDuplicatesIn(subject)
        # then:
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
