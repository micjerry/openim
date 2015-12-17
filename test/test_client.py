import urllib.parse
import http.client
import json
import sys

from tornado.options import define, options
define("id", default="12345", help="run on the given port", type=str)

class TestCase:
    def __init__(self):
        pass

    def test(self):
        input = {
            "id" : "12",
            "contactid" : "34"
        }

        params = json.dumps(input)

        headers = {
            "Authorization": "12",
            "Host": "10.170.9.213",
            "Content-Type": "text/html;charset=utf-8"
        }

        try:
            connection = http.client.HTTPConnection("127.0.0.1", 27000)
            connection.request("POST", "/taobao/test", params, headers)
            response = connection.getresponse().read()
            print("response = (%s)" % response)
            connection.close()
        except Exception as e:
            print("error = (%s)" % str(e))

if __name__ == "__main__":
    ts = TestCase()
    ts.test()
