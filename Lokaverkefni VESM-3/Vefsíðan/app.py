from flask import Flask, render_template, request, redirect
from Adafruit_IO import Client
import requests
import time
import json

adafruit_IO_username = "Lukas_Mani"
adafruit_IO_password = "aio_Wese57C99lrlyGGkAN2sLIJeoyst"

app = Flask(__name__)
aio = Client(adafruit_IO_username,adafruit_IO_password)

def next_free(whole, lot_to_be_free):
    lots_gotten = whole // lot_to_be_free
    remaining = whole - (lots_gotten * 5)

    counter_to_free = lot_to_be_free - remaining

    return counter_to_free

def update_textfile(number_of_past_sales):
    with open("file.txt","w") as f:
        f.write("{}".format(number_of_past_sales))

def update_json(number_of_present_sales=0, number_of_past_sales=0, number_of_container=0, which_mode=0,):
    if which_mode == 0:
        present_sales = aio.data("product-sale")

        difference = number_of_present_sales - number_of_past_sales
        print(difference)
        worklist = []

        with open("file.json","r") as f:
            text = json.load(f)

        holder = text

        for x in range(difference):
            worklist.append(present_sales[x].value)

            print(worklist)
        
        with open("file.json","w") as f:
            for x in range(len(worklist)):
                if worklist[x] == "1":
                    holder["holf1"] = 0

                elif worklist[x] == "2":
                    holder["holf2"] = 0

                elif worklist[x] == "3":
                    holder["holf3"] = 0
            
            json.dump(holder,f)
    
    if which_mode == 1:
        with open("file.json","r") as f:
            text = json.load(f)

        holder = text
        
        with open("file.json","w") as f:
            if number_of_container == "1":
                holder["holf1"] = 1

            elif number_of_container == "2":
                holder["holf2"] = 1

            elif number_of_container == "3":
                holder["holf3"] = 1

            json.dump(holder,f)

def state():
    with open("file.json","r") as f:
        text = json.load(f)

    if text['holf1'] == 1:
        first = "Ekki t??mt"
    else:
        first = "t??mt"
    
    if text['holf2'] == 1:
        second = "Ekki t??mt"
    else:
        second = "t??mt"

    if text['holf3'] == 1:
        third = "Ekki t??mt"
    else:
        third = "t??mt"

    if first == "t??mt" and second == "t??mt" and third == "t??mt":
        requests.post('https://maker.ifttt.com/trigger/all_empty/with/key/f49illFEJnJOEtg2RynJ58K4G7XTj3omROXiT5rBcjZ')

    return [first, second, third]

def firstruncheck():
    global firstrun

    if firstrun == True:
        firstrun = False
        
def newsale(product_sales, past_sales):
    global firstrun
    if firstrun == False:
        if product_sales == past_sales:
            past = past_sales
            return [past, False]

        elif product_sales > past_sales:
            past = product_sales
            return [past, True]
    else:
        past = product_sales
        return [past, False]

def biggest():
    product_data = aio.data("product-sale")

    counter1 = 0
    counter2 = 0
    counter3 = 0

    for x in product_data:
        if int(x.value) == 1:
            counter1 += 1
        elif int(x.value) == 2:
            counter2 += 1
        elif int(x.value) == 3:
            counter3 += 1

    if counter1 > counter2 and counter1 > counter3:
        most_popular = products[1]
    
    elif counter2 > counter1 and counter2 > counter3:
        most_popular = products[2]

    elif counter3 > counter1 and counter3 > counter2:
        most_popular = products[3]
    
    else:
        return "Engin vara er vins??lari en ??nnur"

    return most_popular

products = {1:"TEST1",2:"TEST2",3:"TEST3"}
firstrun = True

with open("file.txt","r") as f:
    text = f.read()
past = int(text)

@app.route("/supersecret")
def index():
    global past

    with open("file.json","r") as f:
        product_data = aio.data("product-sale")

        gogn = json.load(f)

    counter1 = 0
    counter2 = 0
    counter3 = 0

    net_sales = 0
    lot = 5
    net_sales_counter = 0
    skip_counter = 1

    heild = len(product_data)
    next_free_counter = next_free(heild,lot)

    for x in product_data:
        if skip_counter % lot != 0:
            if x.value == "1":
                net_sales += 5
            elif x.value == "2":
                net_sales += 6
            elif x.value == "3":
                net_sales += 7
        else:
            skip_counter = skip_counter
        skip_counter += 1

    most_popular = biggest()

    newsalecheck = newsale(len(product_data), past)
    firstruncheck()
    if newsalecheck[1] == True:     
        update_json(heild, past,0,0)
        past = newsalecheck[0]

    state_of_products = state()
    update_textfile(past)

    return render_template("index.html", gogn = gogn, heild = heild, most_popular = most_popular, state_of_products = state_of_products, net_sales = net_sales, next_free_counter = next_free_counter)
@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/update")
def update():
    holf_number = request.args.get("num")
    update_json(0,0,holf_number,1)

    return redirect("/supersecret")

@app.errorhandler(404)
def villa(error):
    return render_template("villusida.html")

if __name__ == '__main__':
    app.run(debug=True)