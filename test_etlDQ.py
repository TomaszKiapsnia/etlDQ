from unittest import TestCase
from etlDQ import Metric


class TestMetric(TestCase):

    def test_eq_metrics(self):
        m1 = Metric('metric1')
        m2 = Metric('metric2')
        self.assertEqual(m1, m2)

    def test_ne_metrics(self):
        m1 = Metric('metric1')
        m3 = Metric('metric3')
        self.assertNotEqual(m1, m3)
