from datetime import datetime
import json


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init():
    global entries,next_id,GUESTBOOK_ENTRIES_FILE

    try:
        # next_id should end up being set to one greater than the maximum ID found in the previous entry data
        with open(GUESTBOOK_ENTRIES_FILE) as f:
            entries = json.load(f)
        for each_dict in entries:
            if next_id <= int(each_dict['id']) :
                next_id = int(each_dict['id'])+ 1
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE,next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id": next_id}
    entries.insert(0, entry) ## add to front of list
    next_id +=1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    for i in range(len(entries)):
        if entries[i]['id'] == int(id):
            entries.pop(i)
            break
    next_id -=1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        # for element in entries:
        #     print(element)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
