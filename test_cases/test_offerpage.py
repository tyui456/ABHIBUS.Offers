from POM.offerpage import offerpage

class TestOfferPage:
    def test_offer(self,_driver):
        obj = offerpage(_driver)
        obj.click_offer()
        obj.click_leavingfrom()
        obj.click_goingto()
        obj.click_datetojourney()




