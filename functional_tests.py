from selenium import webdriver
import unittest
class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone heard about a list application
        # He went to the home page of this application
        self.browser.get('http://localhost:8000')
        # He noticed the title and header containing a word "To-Do"
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        # The applicatio invites him to input a to-do list
        # He type "Buy peacock feathers in a input box"
        # He hit enter key and the page updated
        # The table shows "1: Buy peacock feathers"
        # Then the page showed another input box which could be typed other to-do list
        # He typed "Use peacock feathers to make a fly"
        # Then the page updated again, the list show those two tasks
        # He wanted to know if this website could remember his lists
        # He saw a unique URL generated by the website
        # And there was a description about this function
        # He accessed that URL and found his list was still there
        # He was satisfried and went to sleep
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')