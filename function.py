def find_emotion(data, situation):
    for record in data:
        if record["상황"] == situation:
            return record["감정"]
    return None

def percenter(text, situation):
    text_list = list(text)
    situation_list = list(situation)
    mc = 0
    for x in situation_list:
        if x in text_list:
            mc += 1
            text_list.remove(x)

    p = len(situation)

    if len(situation) == 0:
        return 0

    percent = mc / p * 100
    return percent
