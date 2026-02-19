import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev/dashboard")
        self.assertEqual(node.text, node2.text)
        self.assertIsNone(node.url)
        self.assertNotEqual(node,node2)
        self.assertIsNotNone(node2.url)
        self.assertIsInstance(node.text,str)



if __name__ == "__main__":
    unittest.main()