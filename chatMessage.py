from faker import Faker
import datetime

def createClientMessage(name, message):
    # exitならそのまま返す
    if message == "exit": return message

    # fakerオブジェクトの作成
    fake = Faker()

    # chat メッセージの形式を作成
    returnMessage = ""
    dt_now = datetime.datetime.now()
    time = dt_now.strftime('%m/%d %H:%M:%S')

    returnMessage = "name : " + name + "\n" + "time : " + time + "\n" + "message : " + message

    return returnMessage


def createChatMessage():
    fake = Faker()

    returnMessage = ""

    dt_now = datetime.datetime.now()

    name = fake.name()
    time = dt_now.strftime('%m/%d %H:%M:%S')
    message = fake.text()

    returnMessage = "name : " + name + "\n" + "time : " + time + "\n" + "message : " + message

    return returnMessage
