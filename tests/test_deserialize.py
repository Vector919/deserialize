import unittest
from deserialize import deserialize


class TestDeserializer(unittest.TestCase):
    def setUp(self):
        self.test_json = '{"object":{"key":{"test_data":10}}}'
        self.test_json_array = '{"thing":[{"key1":"val1"}, {"key2":"val2"}]}'
        self.test_flat_json = '{"keyval.keypair.keynum":200}'
        self.test_xml = """
                        <DATA>
                           <NODE1>
                                <LEAF_NODE>
                                    Person
                                </LEAF_NODE>
                           </NODE1>

                           <NODE2>Place</NODE2>
                           <NODE3>Thing</NODE3>
                        </DATA>
                        """

    def test_from_json(self):
        """
        Ensure the nested keys in the JSON data
        get properly deserialized as object properties
        """
        json_object = deserialize.fromJSON(self.test_json)

        # ensure the proper object attributes are created
        self.assertTrue(hasattr(json_object, 'object'))
        self.assertTrue(hasattr(json_object.object, 'key'))
        self.assertTrue(hasattr(json_object.object.key, 'test_data'))

        # ensure the value is properly assigned
        self.assertEqual(10, json_object.object.key.test_data)

    def test_from_flat_json(self):
        """
        Ensure the proper keys get created from a flat JSON structure
        """
        json_object = deserialize.fromFlatJSON(self.test_flat_json)

        self.assertTrue(hasattr(json_object, 'keyval'))
        self.assertTrue(hasattr(json_object.keyval, 'keypair'))
        self.assertTrue(hasattr(json_object.keyval.keypair, 'keynum'))

        self.assertEqual(json_object.keyval.keypair.keynum, 200)



    def test_array_from_json(self):
        json_object = deserialize.fromJSON(self.test_json_array)

        self.assertTrue(hasattr(json_object, 'thing'))
        self.assertTrue(isinstance(json_object.thing, list))

        self.assertEqual(json_object.thing[0]['key1'], 'val1')

    def test_json_config(self):
        json_object = deserialize.fromJSON(self.test_json, config={'test_data': lambda x: x+2})
        self.assertEqual(json_object.object.key.test_data, 12)

    def test_from_xml(self):
        xml_object = deserialize.fromXML(self.test_xml)

        # ensure the objects are correctly created recursively
        self.assertTrue(hasattr(xml_object, 'NODE1'))
        self.assertTrue(hasattr(xml_object.NODE1, 'LEAF_NODE'))

        # ensure the value is properly assigned
        self.assertIn('Person', xml_object.NODE1.LEAF_NODE)

if __name__ == '__main__':
    unittest.main()
