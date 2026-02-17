import json
import function

with open('data.json', 'r', encoding="utf-8") as f:
    study = json.load(f)

situation_list = [record["상황"] for record in study]
emotion = [record["감정"] for record in study]

answer = input("상황을 입력하세요: ")

if answer in situation_list:
    p = function.find_emotion(study, answer)
    print("감정은 {}입니다".format(p))
else:
    print("좆까세요")

