import requests
import unittest
from testPlan.common.commonFun import Recipe_Interfaces,Fun
import json

class MyTest(unittest.TestCase):        #封装测试环境的初始化
    token = Fun.take_token('../common/token.json')
    def setUp(self):
        print("-----start test Recipe_Interfaces-----")
        pass

    def test_01_GetRecipeCatalogs(self):
        print("get Recipe Catalogs Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeCatalogs_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data1
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_02_GetRecipeHotCatalogs(self):
        print("get Recipe Hot Catalogs Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeHotCatalogs_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data1
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_03_GetRecipeList(self):
        print("Get Recipe List Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeList_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data3
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_04_getSearchRecipe(self):
        print("get Search Recipe Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getSearchRecipe_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data4
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_05_getRecipeDetails(self):
        print("Get recipe details Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.GetRecipeDetails_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data5
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_06_getSeasonIngredientList(self):
        print("get Season Ingredient List Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getSeasonIngredientList_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data6
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_07_getRankingRecipe(self):
        print("get Ranking Recipe Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRankingRecipe_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data7
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_08_getChosenRecipe(self):
        print("get Chosen Recipe Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getChosenRecipe_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data8
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_09_getHotMenus(self):
        print("get Hot Menus Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getHotMenus_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data9
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_10_getVideos(self):
        print("get Videos Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getVideos_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data10
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_11_getRecipeByTime(self):
        print("get Recipe By Time Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeByTime_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data11
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_12_getRecipeByIngredients(self):
        print("get Recipe By Ingredients Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getRecipeByIngredients_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data12
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_13_addCollect(self):
        print("add Collect Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.addCollect_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data13
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_14_getCollect(self):
        print("get Collect Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.getCollect_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data14
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def test_15_delCollect(self):
        print("del Collect Test")
        token = self.token
        url1 = self.url1 = Recipe_Interfaces.delCollect_url
        head1 = Fun.merge_Two_Dicts(Recipe_Interfaces.header1, token)
        data1 = Recipe_Interfaces.data15
        data1_1 = json.dumps(data1)
        Fun.post_url(url = url1, data = data1_1,headers=head1)

    def tearDown(self):
        print("-----end test Basic Support-----")
        pass
if __name__=="__main__":
    unittest.main()