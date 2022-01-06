from transitions.extensions import GraphMachine
import re
from utils import *


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    def is_going_to_anime(self, event):
        text = event.message.text
        return text.lower() == "我是肥宅"

    def on_enter_anime(self, event):
        userid = event.source.user_id
        send_button_animetemplate(userid)
    
    def is_going_to_ncku(self, event):
        text = event.message.text
        return text.lower() == "慧做事，貞放心"

    def on_enter_ncku(self, event):
        userid = event.source.user_id
        send_button_nckutemplate(userid)

    def is_going_backmenu(self, event):
        text = event.message.text
        if re.match('選單', text):
            return True
        else:
            return False

    def on_enter_menu(self, event):
        print("going to menu")

        userid = event.source.user_id
        send_button_template(userid)