import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_split_basic(self):
        node = TextNode("Hello `code` world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(3, len(nodes))
        self.assertEqual("Hello ", nodes[0].text)
        self.assertEqual(TextType.TEXT, nodes[0].text_type)
        self.assertEqual("code", nodes[1].text)
        self.assertEqual(TextType.CODE, nodes[1].text_type)
        self.assertEqual(" world", nodes[2].text)
        self.assertEqual(TextType.TEXT, nodes[2].text_type)

if __name__ == "__main__":
    unittest.main()