class HomePage():
    logo_icon = '.custom-logo-link'
    get_started_btn = '#get-started'
    heading_text = 'h1'
    copyright_text = '.tg-site-footer-section-1'
    menu_links = "//*[starts-with(@id, 'menu-item')]"



    def open_page(self):
        self.open('https://practice.automationbro.com')


    def login(self):
        self.open('https://practice.automationbro.com/my-account/')
        self.add_text("#username", 'testuser666')
        self.add_text("#password", "testuser666!")
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

