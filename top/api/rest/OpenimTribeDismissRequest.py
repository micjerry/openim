'''
Created by auto_sdk on 2015.08.26
'''
from top.api.base import RestApi
class OpenimTribeDismissRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.tribe_id = None
		self.user = None

	def getapiname(self):
		return 'taobao.openim.tribe.dismiss'
