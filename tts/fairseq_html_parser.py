from html.parser import HTMLParser

# Sample HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MMS - TTS Supported Languages</title>
<style>
p { margin:0 }
</style>
</head>
<body>
<p> Iso Code &emsp; Language Name </p>
<p> abi &emsp; Abidji </p>
<p> ace &emsp; Aceh </p>
<p> aca &emsp; Achagua </p>
<!-- ... more items ... -->
</body>
</html>
"""

# Create a subclass of HTMLParser
class FairseqHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.languages = []
        self.current_tag = ''

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_endtag(self, tag):
        self.current_tag = ''

    def handle_data(self, data):
        if self.current_tag == 'p':
            # Split the data by the em-space and filter out empty strings
            parts = [part for part in data.split('\u2003') if part]
            if len(parts) == 2:
                # Append a tuple with the ISO code and language name
                self.languages.append((parts[0].strip(), parts[1].strip()))

    def get_iso_codes(self):
        """Return a list of ISO language codes."""
        return [iso_code for iso_code, _ in self.languages]

def main():
    # Instantiate the parser
    parser = FairseqHTMLParser()

    # Feed the HTML content to the parser
    parser.feed(html_content)

    # Print the list of languages
    for iso_code, language_name in parser.languages:
        print(f"Iso Code: {iso_code}, Language Name: {language_name}")

if __name__ == "__main__":
    main()
