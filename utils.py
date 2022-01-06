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
        alt_text='頂樓風好大，我好冷，我好怕',
        template=ButtonsTemplate(
            thumbnail_image_url='https://imgur.dcard.tw/D2FEuC7h.jpg',
            image_size="contain",
            title='選單',
            text='拜託給我過',
            actions=[
                MessageTemplateAction(
                    label='巴哈姆特動畫瘋',
                    text='我是肥宅'
                ),
                MessageTemplateAction(
                    label='NCKU',
                    text='慧做事，貞放心'
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"

def send_button_animetemplate(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='動畫瘋',
        template=ButtonsTemplate(
            thumbnail_image_url='https://p2.bahamut.com.tw/B/2KU/08/15a2925edf3cc99fe0674f9b8d1bz385.JPG?v=1617180801865',
            title='動畫瘋',
            text='這是我老婆',
            actions=[
                URITemplateAction(
                    label='青春校園',
                    uri='https://ani.gamer.com.tw/animeList.php?c=13'
                ),
                URITemplateAction(
                    label='幽默搞笑',
                    uri='https://ani.gamer.com.tw/animeList.php?c=5'
                ),
                URITemplateAction(
                    label='推理懸疑',
                    uri='https://ani.gamer.com.tw/animeList.php?c=7'
                ),
                URITemplateAction(
                    label='不可以瑟瑟',
                    uri='https://ani.gamer.com.tw/animeList.php?c=age-valiage'
                ),
            ]
            
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"

def send_button_nckutemplate(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='成大選單',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/8/83/National_Cheng_Kung_University_logo.svg/1200px-National_Cheng_Kung_University_logo.svg.png',
            title='成大選單',
            text='知識是光善良是影',
            actions=[
                URITemplateAction(
                    label='Moodle',
                    uri='https://moodle.ncku.edu.tw/'
                ),
                URITemplateAction(
                    label='選課系統',
                    uri='https://course.ncku.edu.tw/'
                ),
                URITemplateAction(
                    label='成績查詢',
                    uri='https://qrys.ncku.edu.tw/ncku/qrys02.asp'
                ),
                URITemplateAction(
                    label='Dcard校版',
                    uri='https://www.dcard.tw/f/ncku'
                ),
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
