import vk_api
from gtts import gTTS
from config import * 
import time
import requests
import json
import os
class SendMessage():
	def __init__(self,LOGIN,PASSWORD,LANG):
		self.LOGIN = LOGIN
		self.PASSWORD = PASSWORD
		self.LANG = LANG
	def LoginingANDgetUploadURL(self):
		self.vk = vk_api.VkApi(app_id=3116505,login=self.LOGIN , password= self.PASSWORD , scope="friends,audio,docs,messages" )
		self.vk.auth()
		self.url = self.vk.method('docs.getUploadServer',{'access_token': self.vk.token['access_token'],'type':'audio_message'})['upload_url']
	def getTextAndID(self):
		self.text2 = str(input('Enter the text you want to send by TEXT message (This field can be left blank) :'))
		self.text = str(input('Enter the text you want to send by VOICE message:'))
		self.ID = str(input("""In order to send a voice message to the chat you need \n to know the chat's chat and then add 2000000000 to this number \n
Example: chat room 1, then you need to write 2000000001\n

In order to send a voice message to the group, you need to know his name and be \n subscribed to this community. at the beginning, write down ^ and the name of the group\n
Example: ^ Lentach \n Enter the person's id or write his name and surname by putting the symbol '/' \n  Example:  /Peter Ivanov\n""" ))
	def uploadMP3onSERVER(self):
		self.tts = gTTS(text=self.text, lang=self.LANG)
		self.name = str(int(time.time())) + ".mp3"
		self.tts.save(self.name)
		self.files = [('file', (self.name, open(self.name, 'rb')))]
		self.url_2 = requests.post(self.url , files=self.files).text
		os.remove(self.name)
		self.RESPONSE = json.loads(self.url_2)['file']
		self.RESPONSE_2 = self.vk.method('docs.save',{'file': self.RESPONSE })
		self._id = self.RESPONSE_2[0]['id']
		self.owner_id = self.RESPONSE_2[0]['owner_id']
	def CheckingID(self):
		self.k = 0
		self.ID = self.ID.strip()
		if self.ID[0] == '^':
			self.ID = list(self.ID)
			self.k = 1
			del(self.ID[0])
			self.ID = ''.join(self.ID)
			self.ID = self.ID.strip()
			self.listgroup = self.vk.method('groups.get',{'extended':1,'fields':'can_message,id'})['items']
			for x in range(len(self.listgroup)):
				self.can_message = (self.listgroup[x]['can_message'])
				self.id_group1 = self.listgroup[x]['id']
				self.name_group = self.listgroup[x]['name']
				if (self.name_group==self.ID) and (self.can_message==1):
					self.ID_EDIT = int('-' + str(self.id_group1))
					break
		if self.ID[0]=="/" and self.k!=1:
			self.ID = list(self.ID)
			self.k=1
			del(self.ID[0])
			self.ID = ''.join(self.ID)
			self.ID = self.ID.strip()
			self.friends = self.vk.method('friends.get',{'order':'hints','fields':'nickname'})['items']
			for x in range(len(self.friends)):
				self.first = self.friends[x]['first_name']
				self.last = self.friends[x]['last_name']
				self.full_name = ('%s %s' % (self.first,self.last))
                		self.full_name2 = ('%s %s' % (self.last,self.first))

				if (self.full_name == self.ID) or (self.full_name2 == self.ID):
					self.ID_EDIT = self.friends[x]['id']
					break
			del(self.first)
			del(self.last)
		elif self.k!=1:
			self.ID_EDIT = self.ID
		try:
			self.ID_EDIT = int(self.ID_EDIT)
		except:
			print('People or group is not defined')
	def sendMSG(self):
		self.document = 'doc%s_%s' % (str(self.owner_id),str(self._id))
		self.vk.method('messages.send', {'peer_id':self.ID_EDIT,'attachment':self.document,'message':self.text2})
		print('Successfully')
	def main(self):
		self.LoginingANDgetUploadURL()
		while 1:
			self.getTextAndID()
			self.uploadMP3onSERVER()
			self.CheckingID()
			self.sendMSG()

#S = SendMessage(LOGIN,PASSWORD,LANG) #starting
#S.main() # starting
