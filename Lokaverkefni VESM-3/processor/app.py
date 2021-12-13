from Adafruit_IO import Client
import time
import json


adafruit_IO_username = "Lukas_Mani"
adafruit_IO_password = "aio_Wese57C99lrlyGGkAN2sLIJeoyst"

aio = Client(adafruit_IO_username,adafruit_IO_password)

def update(last_length):
    alltime_inputs = aio.data("input")

    if last_length < len(alltime_inputs):
        return True
    else:
        return False

def update_textfile():
    alltime_inputs = aio.data("input")
    card_inputs = aio.data("cards")

    with open("keypad.txt","w") as f:
        f.write("{}".format(len(alltime_inputs)))
    
    with open("cards_inputed.txt","w") as f:
        f.write("{}".format(len(card_inputs)))

def get_last_length(filename):
    with open("{}.txt".format(filename),"r") as f:
        text = f.read()
    
    return int(text)

def check_input(last_input):
    legal_list = ["11","12","13"]
    for x in legal_list:
        if last_input == x:
            return True

def get_back():
    nothing = 0

def card_in_check(last_length):
    card_data = aio.data("cards")

    if len(card_data) > last_length:
        return True
    else:
        return False

def check_user(card_id):
    with open("rfid_clients.json","r") as f:
        users = json.load(f)

    for x in users:
        if x == card_id:
            return True

def enough_on_card(card_id,item_to_buy):
    items = {"11":5,"12":6,"13":7}
    with open("rfid_clients.json","r") as f:
        users = json.load(f)

    available_balance = users[card_id]

    for x in items:
        if item_to_buy == x:
            cost = items[x]

    if cost > int(available_balance):
        return False
    else:
        return True

def transaction_through(card_id, item_to_buy):
    print("GOING")
    items = {"11":5,"12":6,"13":7}
    with open("rfid_clients.json","r") as f:
        users = json.load(f)

    available_balance = users[card_id]

    for x in items:
        if item_to_buy == x:
            container = x[-1]
            cost = items[x]

    aio.send_data("product-sale","{}".format(container))

    remaining_balance = int(available_balance) - cost

    users[card_id] = remaining_balance

    with open("rfid_clients.json","w") as f:
        json.dump(users,f)

def error_code_send(option):
    aio.send_data("error","{}".format(option))

    error_code = aio.data("error-length")

    for x in range(len(error_code)):
        counter += 1

    aio.send_data("error-length",counter)

while True:
    last_length = get_last_length("keypad")

    if update(last_length) == True:
        alltime_inputs = aio.data("input")

        last_input = alltime_inputs[0].value
        last_input = last_input[0:1]

        if check_input(last_input) == True:
            check = 0
            loop_break = False

            while loop_break ==False:
                for x in range(30):
                    check +=1
                    time.sleep(1)
                
                if check > 29:
                    loop_break = True
            
            if card_in_check(get_last_length("cards_inputed")) == True:
                card_feed = aio.data("cards")

                card_id = card_feed[0].value

                if check_user(card_id) == True:
                    if enough_on_card(card_id, last_input) == True:
                        transaction_through(card_id, last_input)
                    else:
                        error_code_send(4)
                        get_back()
                else:
                    error_code_send(3)
                    get_back()
            else:
                error_code_send(2)
                get_back()

        else:
            error_code_send(1)
            get_back()
    update_textfile()