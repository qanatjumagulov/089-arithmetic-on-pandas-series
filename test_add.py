from unittest import TestCase


class TestAdd(TestCase):
    def test_add(self):
        from build import add

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 9])

        res = add(ds1, ds2)

        self.assertEqual(res[0], 3)
        self.assertEqual(res[1], 7)
        self.assertEqual(res[2], 11)
        self.assertEqual(res[3], 15)
        self.assertEqual(res[4], 19)

    def test_subtract(self):
        from build import subtract, multiply, divide

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 9])

        res = subtract(ds1, ds2)

        self.assertEqual(res[0], 1)
        self.assertEqual(res[1], 1)
        self.assertEqual(res[2], 1)
        self.assertEqual(res[3], 1)
        self.assertEqual(res[4], 1)

    def test_multiply(self):
        from build import multiply

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 9])

        res = multiply(ds1, ds2)

        self.assertEqual(res[0], 2)
        self.assertEqual(res[1], 12)
        self.assertEqual(res[2], 30)
        self.assertEqual(res[3], 56)
        self.assertEqual(res[4], 90)

    def test_divide(self):
        from build import divide

        import pandas as pd
        ds1 = pd.Series([2, 4, 6, 8, 10])
        ds2 = pd.Series([1, 3, 5, 7, 9])

        res = divide(ds1, ds2)

        self.assertEqual(res[0], 2.000000)
        self.assertEqual(res[1], 1.3333333333333333)
        self.assertEqual(res[2], 1.200000)
        self.assertEqual(res[3], 1.1428571428571428)
        self.assertEqual(res[4], 1.1111111111111112)
