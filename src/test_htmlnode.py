import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>","Check this out",None,{"href":"https://www.google.com","target":"__blank"})
        node2 = HTMLNode("<a>","Check this out",None,{"href":"https://www.youtube.com","target":"__blank"})
        self.assertIsInstance(node.props_to_html(),str)
        self.assertNotEqual(node.props_to_html(),node2.props_to_html())
        self.assertEqual(node.value,node2.value)


if __name__=="__main__":
    unittest.main()
