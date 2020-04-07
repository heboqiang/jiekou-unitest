# coding:utf-8
# heboqiang



import  unittest
import  json
from base.method import Method,IsContent
from page.laGou import *
from page.diyi1 import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
import requests
requests.packages.urllib3.disable_warnings()
from common.db import *
from common.logger import Log



'''下面封装了get，post，dubbo请求的测试用例'''


class LaGou(unittest.TestCase):
	# log = Log()
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()
		self.log = Log()


	def tearDown(self):
		pass

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		print(r.status_code)

		# print(r.json()['code'])
		# self.assertEqual(r.json ()['code'], 200)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))


	def test_post_001(self):
		"""测试post接口-直接请求"""
		print ("test_laGou_001方法执行")
		self.log.info("------测试post接口-直接请求：start!---------")
		# print(check_user(user=jp_user,name=18821768014))
		"sign为空"
		r = self.obj.post(row=1,data=self.operationJson.getRequestsData(row=1))
		print ("test_laGou_001 is:", r.text)
		self.log.info("获取请求结果：%s" % r.text)
		self.isContent (r=r, row=1)
		self.execl.writeResult (1,'pass')


	def test_post_002(self):
		print ("test_laGou_002方法执行")
		"测试post接口-参数化请求"
		self.log.info("------测试post接口-参数化请求：start!---------")
		r = self.obj.post(row=1,data=set_so_keyword1(phone='18821768014'))
		print ("test_laGou_002 is:", r.text)
		self.isContent (r=r, row=1)
		self.execl.writeResult (1,'pass')

	# def test_get_001(self):
	# 	'''测试get接口'''
	# 	r = self.obj.get(row=4,params=json.loads(self.operationJson.getRequestsData(4)))
	# 	print(type(json.loads(self.operationJson.getRequestsData(4))))
	# 	print(r.url)
	# 	self.isContent(r=r, row=4)
	# 	self.execl.writeResult(4, 'pass')
    #
	# def test_dubbo_003(self):
	# 	'''测试dubbo'''
	# 	r = self.obj.dubbo(row=5,param=self.operationJson.getRequestsData(5),method='tradeDetailQuery')
	# 	# print(type(json.loads(self.operationJson.getRequestsData(5))))
	# 	print (self.operationJson.getRequestsData(5))
	# 	print(r.text)
# print (set_so_keyword(app_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))p_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))

#
#
# if __name__ == '__main__':
#     LaGou().test_laGou_001()
