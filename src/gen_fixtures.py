import json

def get_item(number):
    return {
        "num_photos": 0, 
        "photo_name": "", 
        "number": number,
        "text_colour": "light",
        "caption": ""
    }

if __name__ == '__main__':
    january = {
        "name": "January",
        "items": [],
    }

    february = {
        "name": "February",
        "items": [],
    }


    january['items'].append(get_item(-1))
    january['items'].append(get_item(-1))
    for i in range(16, 32):
        january['items'].append(get_item(i))

    february['items'].append(get_item(-1))
    february['items'].append(get_item(-1))
    february['items'].append(get_item(-1))
    february['items'].append(get_item(-1))
    for i in range(1, 17):
        february['items'].append(get_item(i))

    fixtures = [january, february]
    print json.dumps(fixtures, indent=4)

