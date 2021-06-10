### 表格解析工具
>提供html表格解析功能，可以根据表格行查找元素内容，返回表格行列表
### 安装
> pip install html_parser


### 单个表格行数据获取
```
import urllib.request
from table_parser import HtmlTableParser


def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


def main():
    url = 'http://www.stats.gov.cn/tjsj/zxfb/202105/t20210517_1817510.html'
    xhtml = url_get_contents(url).decode('utf-8')
    p = HtmlTableParser()
    p.feed(xhtml)
    print(p.seach_item("采矿"))
    # ['采矿业', '…', '3.2', '…', '8.4']
    # 多行数据获取
    item_list = ["采矿业", "制造业", "产品销售率"]
    item_data = [p.seach_item(data) for data in item_list]
    """
    [['采矿业', '…', '3.2', '…', '8.4'], ['制造业', '…', '10.3', '…', '22.2'], 
    ['产品销售率（%）', '98.3', '0.4 ( 百分点 )', '97.9', '0.9 ( 百分点 )']]
    """
```
