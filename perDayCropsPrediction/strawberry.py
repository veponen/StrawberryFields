import sqlite3
conn = sqlite3.connect('generator.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE dates
             (Nr crt, Random)''')

<<<<<<< refs/remotes/origin/group2
conn.commit()
=======
def strawberryCorpsGeneration(): #main we call this from the main.py
    days=count_days(start_date,end_date)
    harvest=generate_rnd_nums_ordered(days)
    # print(harvest)
    random_harvest=randomize_harvest(harvest)
    berryCorps=add_to_dict(random_harvest)
    save_to_file(berryCorps)
    save_to_database(berryCorps)


def make_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="qwerty",
        port='12346'
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")

def save_to_database(data):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="qwerty",
        port='12346',
        database="mydatabase"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO corpses (date, value) VALUES (STR_TO_DATE(%s, '%d.%m.%Y') , %s)"
    val=[]
    for x in range(0, len(data)):
        val.append((data[x]["date"], data[x]["harvest"])) 

    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "was inserted.")
    

def save_to_file(data):
    f = open(os.path.join(__location__, "strawberryharvest.txt"), "w")
    for x in range(0, len(data)):
        text=data[x]["date"] + "; " + data[x]["harvest"] + "\n"
        f.write(text)
    f.close()

def add_to_dict(datas):
    dictionary={}
    current_day=start_date
    for x in range(0, len(datas)):
        dictionary[x]={}
        dictionary[x]["date"]=current_day.strftime("%d.%m.%Y")
        dictionary[x]["harvest"]=str(datas[x])
        current_day += datetime.timedelta(days=1)
    return dictionary


def randomize_harvest(harvest_data):
    new_harvest_data=[]
    for x in range(0, len(harvest_data)):
        curr_num=harvest_data[x] - random.randrange(-20,20)
        if(curr_num<0):
            curr_num=0
        new_harvest_data.append(curr_num)
    return new_harvest_data

def generate_rnd_nums_ordered(amount):
    numbers=[]
    bell=[]
    for x in range(0,amount):
        numbers.append(random.random())
    numbers.sort()
    for x in range(0,len(numbers)):
        bell.append(bell_equation(numbers[x]) * max_corps)
    return bell

def bell_equation(input_num):
    return (math.sin(2 * math.pi * (input_num - 1/4)) + 1) / 2

def count_days(start_date, end_date):
    x=0
    while (start_date != end_date): #repeats till the last day
        start_date += datetime.timedelta(days=1)
        x += 1
    x += 1
    return x
    

print (strawberryCorpsGeneration())
>>>>>>> local
