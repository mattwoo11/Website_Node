import unittest
from inline_markdown import *

class TestsplitNode(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("hello *world* foo", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(result,  [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" foo", TextType.TEXT),
    ])