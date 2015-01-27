from TravelingTony.TestCase                   import TestCase
from TravelingTony.Constants                  import TT_Constants
from TravelingTony.pages.ShareOnTwitterPage  import ShareOnTwitterPage
import unittest
import time

class ShareOnTwitterTest(TestCase, unittest.TestCase): 
#this class inherites from the testcase calss, and the setup below will execute the code in Testcase.
#AFter doing all the work this test will only execute the share on twitter.
    def setUp(self):
        super(ShareOnTwitterTest, self).setUp()
        
        
    def test_SendRequestTest(self):
        share_on_twitter_page_obj = ShareOnTwitterPage(self.driver)
        share_on_twitter_page_obj.share()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)
    
    def tearDown(self):
        super(ShareOnTwitterTest, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



