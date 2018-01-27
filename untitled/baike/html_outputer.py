from baike.resource_html_parser import ResourseHtml


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        self.getResourse = ResourseHtml()

    def output_html(self):
        # fout = open('output.html', 'w')
        # fout.write("<html><meta charset=\"utf-8\" />")
        # fout.write("<body>")
        # fout.write("<table>")
        #
        # for data in self.datas:
        #     fout.write("<tr>")
        #     fout.write("<td>%s</td>" % data['url'])
        #     fout.write("</tr>")
        #
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        #
        # fout.close()
        del self.datas[0]
        self.getResourse.getResourse(self.datas)

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)
