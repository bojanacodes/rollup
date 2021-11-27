import unittest
import rollup

# Test checking that the BOM data calculations are correct
class TestRollup(unittest.TestCase):

    def test_proccess_data(self):

        data = [{"id": 0, "parent_part_id": None, "part_id": 3715, "quantity": 1},
                {"id": 1, "parent_part_id": 3715, "part_id": 3676, "quantity": 1},
                {"id": 21, "parent_part_id": 3676, "part_id": 2069, "quantity": 3}]

        result = {3715: 1, 3676: 1, 2069: 3 }

        self.assertEqual(rollup.process_data(data), result)

if __name__ == "__main__":
    unittest.main()
