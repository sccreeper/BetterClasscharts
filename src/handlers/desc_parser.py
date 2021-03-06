from html.parser import HTMLParser

import globals

#HTML parser inherited from Python parser to parse HW descriptions
class Parser(HTMLParser):

    parsed_string = ""
    
    #Text types
    in_paragraph = False
    in_href = False
    
    #Styling types
    in_bold = False
    in_underlined = False
    
    #Bullet points
    in_bulletpoint = False

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.in_paragraph = True
        elif tag == "a": #Links
            
            self.parsed_string += f"[color={globals.CURRENT_CONFIG['accent_colour']}][ref=url{attrs[0][1]}]" #Colour so the link actually shows up as seperate to the body

            self.in_href = True
        elif tag == "br": #Linebreak
            self.parsed_string += "\n"
        #Styling
        elif tag == "u": #Underlined
            self.parsed_string += "[u]"
            
            self.in_underlined = True
        
        #Bold
        elif tag == "span":
            #print(attrs)

            if attrs[0][0] == "style":
                if attrs[0][1] == "font-weight: bolder;" or attrs[0][1] == "font-weight: bold;":
                    self.parsed_string += "[b]"
                    self.in_bold = True
                                    
        
        elif tag == "strong" or tag == "b":
            self.parsed_string += "[b]"

            self.in_bold = True

        #Bullet points

        elif tag == "li":
            self.parsed_string += "[b]  • [/b]" 

            self.in_bulletpoint = True

        elif tag == "img":

            self.parsed_string += f"[u][ref=img{attrs[0][1]}]View image[/ref][/u]"


    def handle_endtag(self, tag):
        if tag == "p" and self.in_paragraph:
            self.parsed_string += "\n\n"
            self.in_paragraph = False
        elif tag == "a" and self.in_href:
            self.parsed_string += "[/ref][/color]"
            self.in_href = False
        
        #Styling
        elif tag == "u" and self.in_underlined:
            self.parsed_string += "[/u]"
            self.in_underlined = False
        #Bold
        elif tag == "strong" and self.in_bold or tag == "span" and self.in_bold or tag == "b" and self.in_bold:
            self.parsed_string += "[/b]"
            self.in_bold = False
        
        elif tag == "li" and self.in_bulletpoint:
            self.parsed_string += "\n"

    def handle_data(self, data):
        
        self.parsed_string += data
    
    def parse(self, html):

        self.convert_charrefs = True

        self.feed(html)

        return self.parsed_string
        

