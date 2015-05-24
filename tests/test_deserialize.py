import unittest
from deserialize import deserialize


class TestDeserializer(unittest.TestCase):
    def setUp(self):
        self.test_data = '{"object":{"key":{"test_data":10}}}'

    def test_from_json(self):
        """
        Ensure the nested keys in the JSON data
        get properly deserialized as object properties
        """
        json_object = deserialize.fromJSON(self.test_data)

        # ensure the proper object attributes are created
        self.assertTrue(hasattr(json_object, 'object'))
        self.assertTrue(hasattr(json_object.object, 'key'))
        self.assertTrue(hasattr(json_object.object.key, 'test_data'))

        # ensure the value is properly assigned
        self.assertEqual(10, json_object.object.key.test_data)

if __name__ == '__main__':
    unittest.main()
