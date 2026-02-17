def find_emotion(data, situation):
    for record in data:
        if record["상황"] == situation:
            return record["감정"]
    return None
