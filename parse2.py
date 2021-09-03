import xml.parsers.expat, sys

class MyXML:
    Parser = ""

    # Prepare for parsing
    def _ _init_ _(self, xml_filename):
        assert xml_filename != ""
        self.xml_filename = xml_filename
        self.Parser = xml.parsers.expat.ParserCreate(  )

        self.Parser.CharacterDataHandler = self.handleCharData
        self.Parser.StartElementHandler = self.handleStartElement
        self.Parser.EndElementHandler = self.handleEndElement

    # Parse the XML file
    def parse(self):
        try:
            xml_file = open(self.xml_filename, "r")
        except:
            print "ERROR: Can't open XML file %s"%self.xml_filename
            raise
        else:
            try: self.Parser.ParseFile(xml_file)
            finally: xml_file.close(  )

    # to be overridden by implementation-specific methods
    def handleCharData(self, data): pass
    def handleStartElement(self, name, attrs): pass
    def handleEndElement(self, name): pass
