from xmljson import parker
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import json

'''
    Lambda function that takes in JSON of form:
    { 
        isFile: True/False (if you are uploading a file path: True)
        xml: File path or txt of XML to be converted
        attributes: True/False (if you want to keep the attributes on the xml tags "id", "name:, etc.
    }
    :return the JSON converted from XML
'''


def lambda_handler(event, context):
    data = json.loads(event)

    if data['isFile']:
        xml = open(data['xml'], 'r').read()
    else:
        xml = data

    if data['attributes']:
        result = bf.data(fromstring(xml))
    else:
        result = parker.data(fromstring(xml), preserve_root=True)

    return json.dumps(result)


if __name__ == "__main__":
    event = {
        'isFile': True,
        'xml': 'sample_xml.xml',
        'attributes': True
    }
    print(lambda_handler(json.dumps(event), ''))