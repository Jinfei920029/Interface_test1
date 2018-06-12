import requests
import unittest
from testPlan.common.commonFun import Recipe_Interfaces,Fun
import json

class MyTest(unittest.TestCase):        #封装测试环境的初始化
    token = Fun.take_token('../common/token.json')
    def setUp(self):
        print("-----start test Recipe_Interfaces-----")
        pass

    def test_1_GetRecipeCatalogs(self):
        print("get Recipe Catalogs Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeCatalogs_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data1
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_2_GetRecipeHotCatalogs(self):
        print("get Recipe Hot Catalogs Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeHotCatalogs_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data1
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_3_GetRecipeList(self):
        print("Get Recipe List Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeList_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data3
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_4_getSearchRecipe(self):
        print("get Search Recipe Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getSearchRecipe_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data4
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_5_getRecipeDetails(self):
        print("Get recipe details Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.GetRecipeDetails_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data5
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def tearDown(self):
        print("-----end test Basic Support-----")
        pass
if __name__=="__main__":
    unittest.main()