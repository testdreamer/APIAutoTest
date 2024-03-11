#首先安装xmltodict，python3 -m pip install xmltodict

import xmltodict
import json

#定义XML转Json的函数
def xmltojson(xmlstr):
    xmlparse = xmltodict.parse(xmlstr)               #parse是XML解析器
    jsonstr = json.dumps(xmlparse,indent=2,sort_keys=True)
    return jsonstr

#定义Json转XML函数
def jsontoxml(jsonstr):
    xmlstr = xmltodict.unparse(jsonstr)
    return xmlstr

if __name__ == '__main__':
    xmlinfo = """
    <student>
    <bokeid>fighter006</bokeid>
    <bokeinfo>
     <cnbologsname>laolu</cnbologsname>
     <page>120</page>
    </bokeinfo>
    <data>
     <address>http://www.baidu.com</address>
     <title>python+dt+requests</title>
    </data>
    </student>
    """

    aa =  {
  "student": {
    "bokeid": "fighter006",
    "bokeinfo": {
      "cnbologsname": "laolu",
      "page": "120"
    },
    "data": {
      "address": "http://www.baidu.com",
      "title": "python+dt+requests"
    }
  }
}
    xtoj = xmltojson(xmlinfo)
    print('XML转json：',xtoj)
    jtox = jsontoxml(aa)
    print('json转XML',jtox)