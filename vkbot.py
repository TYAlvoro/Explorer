import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType 

class Bot:
    def __init__(self):
        self.vk_session = None
        self.authorized = False
        self.vk_api_access = self.do_auth()
        if self.vk_api_access is not None:
            self.authorized = True
    
    def do_auth(self):
        token = "vk1.a.uNWpTMlQ-VL1T95nXSIrYJtSlxOtCgsL9q9hoKbn8tWUnZBSiV9eWicIiiRMyeebSDBVxGmVRFsVKHTowMfn6mUSq6OoafS-Ef8Rkobf90DazMNGGm6fmn-ZFCbrOmcmQTANu1A68y4NSrgjqg1XG67ltdzYHAgvaGTVhghJe4K-njcKAXdSJho8koruPiA7wBR77p-FvQd2bmKRkGiNTQ"
        self.vk_session = vk_api.VkApi(token=token)
        return self.vk_session.get_api()

    def get_msg_text(self):
        long_poll = VkLongPoll(self.vk_session)
        for event in long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                return str(event.text)

    def send_msg(self, id, msg):
        self.do_auth().messages.send(user_id=id, message=msg, random_id=0)