import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_template(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url='https://png.pngtree.com/png-vector/20190129/ourlarge/pngtree-menu-vector-icon-png-image_355811.jpg',
            title='選單',
            text='拜託給我過',
            actions=[
                MessageTemplateAction(
                    label='ptt看板',
                    text='showptt'
                ),
                MessageTemplateAction(
                    label='原神資訊',
                    text='genshin'
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
