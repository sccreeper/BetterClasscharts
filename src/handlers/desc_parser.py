from html.parser import HTMLParser
from cssutils import CSSParser
from cssutils.css import CSSRule
import cssutils

import globals

#HTML parsew inheritired from Python parser to parse HW descriptions
#TODO In future implement this: https://kivy.org/doc/stable/api-kivy.core.text.markup.html

#Bytes to define what type of data string is.

NORMAL_STRING_DATA = "0"
IMAGE_STRING_DATA = "1"

class Parser(HTMLParser):
    
    #Text types
    in_paragraph = False
    in_href = False
    
    #Styling types
    in_bold = False
    in_underlined = False
    
    #Bullet points
    in_bulletpoint = False

    #Assume in normal string at start.
    parsed_string = [f"{NORMAL_STRING_DATA}"]

    current_string_index = 0 

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.in_paragraph = True
        elif tag == "a": #Links
            
            self.parsed_string[self.current_string_index] += f"[color={globals.CURRENT_CONFIG['accent_colour']}][ref={attrs[0][1]}]" #Colour so the link actually shows up as seperate to the body

            self.in_href = True
        elif tag == "br": #Linebreak
            self.parsed_string[self.current_string_index] += "\n"
        #Styling
        elif tag == "u": #Underlined
            self.parsed_string[self.current_string_index] += "[u]"
            
            self.in_underlined = True
        
        #Bold
        elif tag == "span":
            #print(attrs)

            if attrs[0][0] == "style":
                if attrs[0][1] == "font-weight: bolder;" or attrs[0][1] == "font-weight: bold;":
                    self.parsed_string[self.current_string_index] += "[b]"
                    self.in_bold = True
                                    
        
        elif tag == "strong" or tag == "b":
            self.parsed_string[self.current_string_index] += "[b]"

            self.in_bold = True

        #Bullet points

        elif tag == "li":
            self.parsed_string[self.current_string_index] += "[b]  • [/b]" 

            self.in_bulletpoint = True

        elif tag == "img":
            self.parsed_string.append(f"{IMAGE_STRING_DATA}")
            self.current_string_index += 1

            self.parsed_string[-1] += attrs[0][1] #Img src data

            self.parsed_string.append(f"{NORMAL_STRING_DATA}")
            self.current_string_index += 1

    def handle_endtag(self, tag):
        if tag == "p" and self.in_paragraph:
            self.parsed_string[self.current_string_index] += "\n\n"
            self.in_paragraph = False
        elif tag == "a" and self.in_href:
            self.parsed_string[self.current_string_index] += "[/ref][/color]"
            self.in_href = False
        
        #Styling
        elif tag == "u" and self.in_underlined:
            self.parsed_string[self.current_string_index] += "[/u]"
            self.in_underlined = False
        #Bold
        elif tag == "strong" and self.in_bold or tag == "span" and self.in_bold or tag == "b" and self.in_bold:
            self.parsed_string[self.current_string_index] += "[/b]"
            self.in_bold = False
        
        elif tag == "li" and self.in_bulletpoint:
            self.parsed_string[self.current_string_index] += "\n"

    def handle_data(self, data):
        
        self.parsed_string[self.current_string_index] += data
    
    def parse(self, html):

        self.convert_charrefs = True

        self.feed(html)

        return self.parsed_string
        

