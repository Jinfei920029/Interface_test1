import requests
import unittest
from testPlan.common.commonFun import ShoppingCartInterfaces,Fun
import json

class MyTest(unittest.TestCase):        #封装测试环境的初始化
    token = Fun.take_token('../common/token.json')
    def setUp(self):
        print("-----start test Shopping Cart Interfaces-----")
        pass

    def test_01_AddToCart(self):
        print("Add to shopping cart Test")
        token = self.token
        url1 = self.url1 = ShoppingCartInterfaces.AddToCart_url
        head1 = Fun.merge_Two_Dicts(ShoppingCartInterfaces.header1, token)
        data1 = ShoppingCartInterfaces.data1
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_02_DeleteItemsInShoppingCart(self):
        print("Delete items in shopping cart Test")
        token = self.token
        url1 = self.url1 = ShoppingCartInterfaces.DeleteItemsInShoppingCart_url
        head1 = Fun.merge_Two_Dicts(ShoppingCartInterfaces.header1, token)
        data1 = ShoppingCartInterfaces.data2
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_03_ModifyProductInShoppingCart(self):
        print("Modify product in shopping cart Test")
        token = self.token
        url1 = self.url1 = ShoppingCartInterfaces.ModifyProductInShoppingCart_url
        head1 = Fun.merge_Two_Dicts(ShoppingCartInterfaces.header1, token)
        data1 = ShoppingCartInterfaces.data3
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_04_BrowseTheItemsInTheShoppingCart(self):
        print("Browse the items in the shopping cart Test")
        token = self.token
        url1 = self.url1 = ShoppingCartInterfaces.BrowseTheItemsInTheShoppingCart_url
        head1 = Fun.merge_Two_Dicts(ShoppingCartInterfaces.header1, token)
        data1 = ShoppingCartInterfaces.data4
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def tearDown(self):
        print("-----end test Basic Support-----")
        pass
if __name__=="__main__":
    unittest.main()