from seleniumbase import BaseCase
from pom.home_page import HomePage

class HomeTest(BaseCase):

    locators = {
        "logout" : ".woocommerce-MyAccount-content a[href*=logout]"
    }

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        HomePage.login(self)
        HomePage.open_page(self)


    def tearDown(self):
        print("RUNNING AFTER EACH TEST")

        self.open('https://practice.automationbro.com/my-account/')
        self.click(self.locators["logout"])
        self.assert_element_visible("button[name=login]")

        super().tearDown()

    def test_home_page(self):


        self.assert_title('Practice E-Commerce Site – Automation Bro')

        self.assert_element(HomePage.logo_icon)
        #click on the get started button and assert the url
        self.click(HomePage.get_started_btn)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)
        #get the text of header and assert the value
        self.assert_text("Think different. Make different.", HomePage.heading_text)
        #scroll to bottom, assert the copyright text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro", HomePage.copyright_text)

    def test_input(self):
        self.open('https://practice.automationbro.com/contact/')

        self.send_keys(".contact-name input", "Test_name")
        self.send_keys(".contact-email input", "mail@test.com")
        self.send_keys(".contact-phone input", "123456789")
        self.send_keys(".contact-message textarea", "Test message")

        self.click("#evf-submit-277")

        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")
