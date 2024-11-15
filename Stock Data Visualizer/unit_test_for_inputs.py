import unittest
from datetime import datetime, date

from main import validate_date

class TestProject3Inputs(unittest.TestCase):

    def test_symbol_valid(self):
        valid_symbols = ["AAPL", "GOOG", "MSFT"]
        for symbol in valid_symbols:
            self.assertTrue(symbol.isupper() and 1 <= len(symbol) <= 7)

    def test_symbol_invalid(self):
        invalid_symbols = ["aapl", "TOOLONGSYMBOL", "12345", "!@#$%"]
        for symbol in invalid_symbols:
            is_valid = symbol.isupper() and 1 <= len(symbol) <= 7 and symbol.isalpha()
            self.assertFalse(is_valid)


    def test_chart_type_valid(self):
        valid_chart_types = ["1", "2"]
        for chart_type in valid_chart_types:
            self.assertIn(chart_type, ["1", "2"])

    def test_chart_type_invalid(self):
        invalid_chart_types = ["3", "bar", "0"]
        for chart_type in invalid_chart_types:
            self.assertNotIn(chart_type, ["1", "2"])

    def test_time_series_valid(self):
        valid_time_series = ["1", "2", "3", "4"]
        for series in valid_time_series:
            self.assertIn(series, ["1", "2", "3", "4"])

    def test_time_series_invalid(self):
        invalid_time_series = ["5", "daily", "0"]
        for series in invalid_time_series:
            self.assertNotIn(series, ["1", "2", "3", "4"])

    def test_validate_date_valid(self):
        valid_dates = ["2024-01-01", "2000-12-31"]
        for date_str in valid_dates:
            result = validate_date(date_str)
            self.assertIsNotNone(result)
            self.assertIsInstance(result, date)  



    def test_validate_date_invalid(self):
        invalid_dates = ["01-01-2024", "2024/01/01", "2024-13-01", "invalid"]
        for date in invalid_dates:
            result = validate_date(date)
            self.assertIsNone(result)

    def test_date_order_valid(self):
        start_date = datetime.strptime("2024-01-01", "%Y-%m-%d").date()
        end_date = datetime.strptime("2024-01-31", "%Y-%m-%d").date()
        self.assertTrue(start_date <= end_date)

    def test_date_order_invalid(self):
        start_date = datetime.strptime("2024-02-01", "%Y-%m-%d").date()
        end_date = datetime.strptime("2024-01-31", "%Y-%m-%d").date()
        self.assertFalse(start_date <= end_date)

if __name__ == "__main__":
    unittest.main()
