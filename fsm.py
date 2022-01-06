from transitions.extensions import GraphMachine
import re
from utils import send_text_message, send_button_template


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "選單"

    
    def is_going_backmenu(self, event):
        text = event.message.text
        if re.match('選單', text):
            return True
        else:
            return False

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_menu(self, event):
        print("going to menu")

        userid = event.source.user_id
        send_button_template(userid)

    def on_enter_state2(self, event):
        print("i am going to state2")

        reply_token = event.reply_token
        send_text_message(reply_token, text="state2")