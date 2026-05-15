import unittest


def z_score(x, mu, sigma):
    # Group Members: Matthew Hammer, Mei Tate, Cohen Flanagan

    if sigma == 0:
        raise ValueError("Standard deviation cannot be zero.")

    result = (x - mu) / sigma

    return result


class UnitTests(unittest.TestCase):

    def test_mean_has_zero_zscore(self):
        self.assertAlmostEqual(z_score(50.82, 50.82, 1), 0.0)

    def test_z_scores_from_table(self):

        cases = [
            (19, 50.82, 4, -7.955),
            (75, 50.82, 7, 3.454285714285714),
            (96, 50.82, 1, 45.18),
            (-21, -0.5, 8, -2.5625),
            (-11, -0.5, 3, -3.5),
            (7, -0.5, 9, 0.8333333333333334),
            (125, 337.5, 12, -17.708333333333332),
            (275, 337.5, 8, -7.8125),
            (650, 337.5, 5, 62.5),
        ]

        for x, mu, sigma, expected in cases:
            with self.subTest(x=x, mu=mu, sigma=sigma):
                self.assertAlmostEqual(
                    z_score(x, mu, sigma),
                    expected
                )

    def test_sigma_zero_raises_error(self):
        with self.assertRaises(ValueError):
            z_score(1, 50.82, 0)


if __name__ == "__main__":
    unittest.main()