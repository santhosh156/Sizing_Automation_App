# project/test.py
import unittest
from project import app

class ProjectTests(unittest.TestCase):
    """ This class will include functions to setUp() and tearDown() each unit test. """
    def __init__(self, arg):
        super(ProjectTests, self).__init__()
        self.arg = arg

    def runTest(self):
        pass

    # setup and teardown #
    # executed prior to each test
    def setUp(self):
        """ Executed prior to each test """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        """ Executed after each test """
        pass

    # tests #


    def test_index_page(self):
        """ Unit test for index page """
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Sizing Automation', response.data)
        self.assertIn(b'This is a sizing automation application for testing, which estimates the testing effort based on the requirements document.', response.data)
        self.assertIn(b'It uses advanced natural language processing techniques to automate the estimation process.', response.data)
        self.assertIn(b'Get Started', response.data)


if __name__ == "__main__":
    unittest.main()
