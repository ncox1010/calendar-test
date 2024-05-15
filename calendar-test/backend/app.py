from flask import Flask # type: ignore
import csv
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/Sampledata/table', methods=["GET"])
def SampledataTable():
    with open('Sampledata.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        del data[0]
        json_grid = []
        for r in data:
            if r:
                cal = False
                wat = False
                book = False
                if (r[8] == "Add to calendar"):
                    cal = True
                if (r[8] == "Wishlist"):
                    wat = True
                if (r[8] == "Bookmark"):
                    book = True
                json_row = {
                    "Title":r[0],
                    "Calendar": cal,
                    "Watchlist": wat,
                    "Bookmarked": book,
                    "Event Category": r[11]
                }
                json_grid.append(json_row)
    return json_grid

@app.route('/Sampledata/events', methods=["GET"])
def Sampledata():
    json_events = []
    with open('Sampledata.csv', 'r') as file:
        reader = csv.reader(file)
        #print (reader)
        data = list(reader)
        del data[0]
        for r in data:
            if r:  # Check if the row is not empty
                json_event = {
                    "title": r[0],
                    "start": "",  # Assuming the date is in the 7th column
                    "end": "",
                    "color": ""
                }
                # Create a new dictionary for each event
                date_str = r[6].strip("[]")  # Remove the square brackets
                date_list = [date.strip().strip("'") for date in date_str.split("' ,'")]
                for d in date_list:
                    if ("', '" in d):
                        date_list.remove(d)
                        date_list.extend(d.split("', '"))
                date_list = sorted(date_list)
                if len(date_list) == 1:
                    json_event["start"] = dateFormat(date_list[0])
                else:
                    json_event["start"] = dateFormat(date_list[0])
                    json_event["end"] = dateFormat(date_list[-1])

                time_str = r[8].strip("[]")
                time_list = [time.strip().strip("'") for time in time_str.split("-")]

                json_event["start"] = json_event["start"] + " " + (str (timeCondition(time_list[0])))


                if r[11] == 'Family':
                    json_event["color"] = "red"
                elif r[11] == 'Exhibit':
                    json_event["color"] = "blue"
                else:
                    json_event["color"] = "green"
                json_events.append(json_event)
        return (json_events)
    
def timeCondition (time):
    time = time.strip("'")
    if (time[0:-2].lower() == "AM"):
        time = time[0:-2]
        if len(time) == 4:
            time = "0" + time
    else:
        time = time[0:-2]
        if len(time) == 4:
            time = "0" + time
        time_holder = time[0:2]
        time_holder = (str ((int (time_holder)) + 12))
        time = time_holder + time[2:]
    return time
    
def dateFormat (date):
    date_str = ""
    date_li = date.split(" ")
    if (len(date_li) != 3):
        return "Invalid date"
    month = date_li[0]
    day = date_li[1]
    if (',' in day):
        day = day.strip(',')
    year = date_li[2]
    if (',' in year):
        year = year.strip(',')
    date_str += year
    if (month.lower() == "january" or month.lower() == "jan"):
        date_str += "-01-"
    elif (month.lower() == "february" or month.lower() == "feb"):
        date_str += "-02-"
    elif (month.lower() == "march" or month.lower() == "mar"):
        date_str += "-03-"
    elif (month.lower() == "april"or month.lower() == "apr"):
        date_str += "-04-"
    elif (month.lower() == "may"):
        date_str += "-05-"
    elif (month.lower() == "june" or month.lower() == "jun"):
        date_str += "-06-"
    elif (month.lower() == "july" or month.lower() == "jul"):
        date_str += "-07-"
    elif (month.lower() == "august" or month.lower() == "aug"):
        date_str += "-08-"
    elif (month.lower() == "september" or month.lower() == "sep"):
        date_str += "-09-"
    elif (month.lower() == "october" or month.lower() == "oct"):
        date_str += "-10-"
    elif (month.lower() == "november" or month.lower() == "nov"):
        date_str += "-11-"
    elif (month.lower() == "december" or month.lower() == "dec"):
        date_str += "-12-"

    if len(day) == 1:
        date_str += "0"
        date_str += day
    else:
        date_str += day

    return date_str
        


    
@app.route('/Parserfile/events', methods=["GET"])
def Parserfile():
    json_events = []
    with open('Parserfile.csv', 'r') as file:
        reader = csv.reader(file)
        #print (reader)
        data = list(reader)
        del data[0]
        for r in data:
            if r:  # Check if the row is not empty
                json_event = {
                    "title": r[0],
                    "start": "",  # Assuming the date is in the 7th column
                    "end": "",
                    "color": ""
                }
                # Create a new dictionary for each event
                if (r[6] == "null"):
                    date_components = r[7].split(' ')
                    date_re = ''
                    for d in date_components[0:3]:
                        date_re += d
                        date_re += " "
                    print(date_re.strip(' '))
                    json_event["start"] = dateFormat(date_re.strip(' '))
                    #print(json_event)
                else:     
                    date_str = r[6].strip("[]")  # Remove the square brackets
                    date_list = [date.strip().strip("'") for date in date_str.split("-")]
                
                    if len(date_list) == 1:
                        json_event["start"] = dateFormat(date_list[0])
                    else:
                        json_event["start"] = dateFormat(date_list[0])
                        json_event["end"] = dateFormat(date_list[-1])

                if (r[9] != 'null'):
                    time_str = r[9].strip("[]")
                    time_list = [time.strip().strip("'") for time in time_str.split("-")]
                    #print(time_list)
                    json_event["start"] = json_event["start"] + " " + (str (timeCondition(time_list[0])))
                    json_event["end"] = json_event["end"] + " " + (str (timeCondition(time_list[1])))
                else :
                    time = r[10]

                
                if r[12] == 'Family':
                    json_event["color"] = "red"
                elif r[12] == 'Exhibit':
                    json_event["color"] = "blue"
                else:
                    json_event["color"] = "green"
                json_events.append(json_event)
        return (json_events)
    
@app.route('/Parserfile/table', methods=["GET"])
def ParserfileTable():
    with open('Parserfile.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        del data[0]
        json_grid = []
        for r in data:
            if r:
                cal = False
                wat = False
                book = False
                if (r[8] == "Add to Calendar"):
                    cal = True
                if (r[8] == "Wishlist"):
                    wat = True
                if (r[8] == "Bookmark"):
                    book = True
                json_row = {
                    "Title":r[0],
                    "Calendar": cal,
                    "Watchlist": wat,
                    "Bookmarked": book,
                    "Event Category": r[12]
                }
                json_grid.append(json_row)
    return json_grid
    
if __name__ == "__main__":
    app.run("localhost", 6969)