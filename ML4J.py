import json

situation = input("상황: ")
emotion = input("감정: ")

with open('data.json', 'r', encoding="utf-8") as f:
    emote = json.load(f)

situation_list = [record["상황"] for record in emote]

record = {
    "상황": situation,
    "감정": emotion,
}

if situation in situation_list:
    print("이미 있는 상황입니다.")
    exit()
else:
    emote.append(record)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(emote, f, ensure_ascii=False)

print("저장 완료")
