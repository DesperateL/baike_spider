class HtmlOutputer(object):
    def __init__(self):#建立列表存放数据
        self.datas = []
    def collect_data(self, data):#收集数据
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):#将收集好的数据写出到一个html文件中
        fout = open('output.html','w',encoding='utf-8')#建立文件输出对象

        fout.write('<html>')
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' %data['url'])
            fout.write('<td>%s</td>' %data['title'])
            fout.write('<td>%s</td>' %data['summary'])

            fout.write('</tr>')


        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()