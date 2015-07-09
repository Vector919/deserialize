import json
import xml.etree.ElementTree as xml


class JSONdata(object):
    pass


class XMLData(object):
    pass


def _recurse_json_keys(data, keys_object, config={}):
    """
    Collect all of the keys from the given JSON data,
    by recursively searching the hierarchy, and attaching
    child keys to a parent object

    Args:
        keys_object: parent object to set attrs/child objects of
        data: the remaining parsed json data to create objects from
        config: special keys that can be used to mutate results
    """
    for key in data:

        if not isinstance(data, list) and isinstance(data[key], dict):
            top_key = JSONdata()
            setattr(keys_object, key, top_key)
            _recurse_json_keys(data[key], top_key, config)

        elif isinstance(key, dict):
            top_list = []
            for element in data:
                top_element = JSONdata()
                _recurse_json_keys(element, top_element, config)
                top_list.append(top_element)
            setattr(keys_object, key, top_list)

        else:
            if key in config:
                special_key = config[key](data[key])
                setattr(keys_object, key, special_key)
            else:
                setattr(keys_object, key, data[key])


def _recurse_xml_keys(xml_root, top_key):
    """
    Recursively set all of the child nodes
    from an XML object
    """
    for child in xml_root:
        if len(child):
            child_object = XMLData()
            setattr(top_key, child.tag, child_object)
            _recurse_xml_keys(child, child_object)
        else:
            setattr(top_key, child.tag, child.text)




def fromJSON(data, config={}):
    """
    Take a JSON string, and return nested objects representing the
    structure of the JSON and it's data
    """
    json_data = json.loads(data)
    gen_obj = JSONdata()
    _recurse_json_keys(json_data, gen_obj, config)
    return gen_obj


def fromXML(data):
    """
    Take an XML string
    """
    xml_data = xml.fromstring(data)
    top_level = XMLData()
    _recurse_xml_keys(xml_data, top_level)
    return top_level

def fromFlatJSON(data):
    """
    Generate a generic object from a flat json structure with dot notation
    Example
    {
        'key.key1.key2': "value"
    }

    >> json_object.key.key1.key2

    allows for representing a complex structure without using nested keys
    """
    json_data = json.loads(data)
    top_key = JSONdata()

    for key in json_data:
        object_nodes = key.split(".")
        last_key = top_key
        for n in xrange(0, len(object_nodes)+1):
            if len(object_nodes) == 1:
                last_node = object_nodes.pop(0)
                setattr(last_key, last_node, json_data[key])

            elif object_nodes:
                last_node = object_nodes.pop(0)
                final_key = JSONdata()
                setattr(last_key, last_node, final_key)
                last_key = final_key
            else:
                continue
    return top_key
