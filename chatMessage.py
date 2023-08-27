from faker import Faker
import datetime

def createChatMessage():
    fake = Faker()

    returnMessage = ""

    dt_now = datetime.datetime.now()

    name = fake.name()
    time = dt_now.strftime('%m/%d %H:%M:%S')
    message = fake.text()

    returnMessage = "name : " + name + "\n" + "time : " + time + "\n" + "message : " + message

    return returnMessage
