import json
import function

with open('data.json', 'r', encoding="utf-8") as f:
    study = json.load(f)

situation_list = [record["상황"] for record in study]
emotion = [record["감정"] for record in study]

answer = input("상황을 입력하세요: ")

number = 0
q = 0
for i in range(len(situation_list)):
    new = function.percenter(answer, situation_list[q])
    if new >= number:
        correct = situation_list[q]
    q += 1

if correct in situation_list:
    p = function.find_emotion(study, correct)
    print("감정은 {}입니다".format(p))
else:
    print("좆까세요")

