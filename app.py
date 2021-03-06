from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('8qq4YY4yNgZshILLmOob26ZjFlq35plhdpAgCnpQM0o0gwcDT7fIWYJYiWm4D8e+ghMXGShKyWrRZ8VUTBiQ66It3OjY+EMvFGAY7QF8pP9tX5z3f2fBzmblSctsp8fXa75c686ja9ADVl2dctXCoQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('81eee38d1e7f45038a7e3911904cefed')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你再問什麼?"

    if msg == 'hi':
        r = 'hi'
    elif msg == '吃飽沒':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()