from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        
    def handle_starttag(self, tag, attrs):
        if tag not in ['meta', 'link', 'br', 'hr', 'img', 'input', 'source']:
            self.tags.append(tag)
            
    def handle_endtag(self, tag):
        if tag not in ['meta', 'link', 'br', 'hr', 'img', 'input', 'source']:
            if not self.tags:
                print(f"Error: closing tag </{tag}> with no open tags")
                return
            last_tag = self.tags.pop()
            if last_tag != tag:
                print(f"Error: unmatched tag </{tag}>, expected </{last_tag}> at line {self.getpos()[0]}")
                self.tags.append(last_tag) # put it back

parser = MyHTMLParser()
with open('/Users/alikbekmukanbetov/Desktop/presentation/index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())
    
if parser.tags:
    print(f"Unclosed tags remaining: {parser.tags}")
else:
    print("All tags matched perfectly.")

