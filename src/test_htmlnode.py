import unittest
from htmlnode import HTMLNode

class TesthtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "click me", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://example.com\"")
    
    def test_props_to_html2(self):
        node = HTMLNode("a", "click me", None, {"href": "https://example.com", "target": "blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://example.com\"" " target=\"blank\"")
    
    def test_props_to_html3(self):
        node = HTMLNode("a", None, None, None)
        self.assertEqual(node.props_to_html(), "")
    

if __name__ == "__main__":
    unittest.main()