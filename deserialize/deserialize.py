import json
import xml.etree.ElementTree as xml


class JSONdata(object):
    pass


class XMLData(object):
    pass


def _recurse_json_keys(data, keys_object):
    """
    Collect all of the keys from the given JSON data,
    by recursively searching the heirarchy
    """
    for key in data.keys():
        if isinstance(data[key], dict):
            top_key = JSONdata()
            setattr(keys_object, key, top_key)
            _recurse_json_keys(data[key], top_key)
        else:
            setattr(keys_object, key, data[key])


def _recurse_xml_keys(xml_root, top_key):
    for child in xml_root:
        if len(child):
            child_object = XMLData()
            setattr(top_key, child.tag, child_object)
            _recurse_xml_keys(child, child_object)
        else:
            setattr(top_key, child.tag, child.text)


def fromJSON(data):
    """
    Take a JSON string, and return nested objects representing the
    structure of the JSON and it's data
    """
    json_data = json.loads(data)
    gen_obj = JSONdata()
    _recurse_json_keys(json_data, gen_obj)
    return gen_obj


def fromXML(data):
    """
    Take an XML string
    """
    xml_data = xml.fromstring(data)
    top_level = XMLData()
    _recurse_xml_keys(xml_data, top_level)
    return top_level
