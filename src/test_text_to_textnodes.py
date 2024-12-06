
import unittest
from textnode import TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes(self):
        # Test 1: Text
        text = "Hello world"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello world")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        
        # Test 2: Bold text
        text = "Hello **world**"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, "")

        # Test 3: Italic text
        text = "Hello *world*"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, "")
        
        # Test 4: Code text
        text = "Hello `world`"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, "")

        # Test 5: Image text
        text = "Hello ![world](https://www.boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)  # Should be 3 nodes: text + image + text
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://www.boot.dev")

        # Test 6: Link text
        text = "Hello [world](https://www.boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)  # Should be 3 nodes: text + link + text
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text, "world")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://www.boot.dev")

        # Test 7: Complex mixed text
        text = "This is **text** with an *italic* word and a `code block`"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)


if __name__ == "__main__":
    unittest.main()