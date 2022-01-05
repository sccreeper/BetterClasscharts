from html.parser import HTMLParser

#HTML parsew inheritired from Python parser to parse HW descriptions
#TODO In future implement this: https://kivy.org/doc/stable/api-kivy.core.text.markup.html
class Parser(HTMLParser):

    in_paragraph = False

    parsed_string = ""

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.in_paragraph = True
        # elif tag == "br":
        #     self.parsed_string += "\n"

    def handle_endtag(self, tag):
        if tag == "p" and self.in_paragraph:
            self.parsed_string += "\n"
            self.in_paragraph = False

    def handle_data(self, data):

        self.parsed_string += data
    
    def parse(self, html):
        self.feed(html)

        return self.parsed_string
        
