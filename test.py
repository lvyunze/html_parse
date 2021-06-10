import urllib.request
from html_parse.table_parse import HtmlTableParser


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
    item_list = ["采矿业", "制造业", "产品销售率"]
    item_data = [p.seach_item(data) for data in item_list]

    print(item_data)
    """
   [['采矿业', '…', '3.2', '…', '8.4'], ['制造业', '…', '10.3', '…', '22.2'], 
   ['产品销售率（%）', '98.3', '0.4 ( 百分点 )', '97.9', '0.9 ( 百分点 )']]
    """


if __name__ == '__main__':
    main()
