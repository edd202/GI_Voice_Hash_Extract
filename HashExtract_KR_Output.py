import json


print('\n추출할 데이터 입력\n')
print('스토리 관련\nVO_COOP - 전설퀘\nVO_EQ - 이벤트\nVO_AQ - 마신퀘\nVO_LQ - 전설퀘\nVO_WQ - 월드 퀘스트(이벤트 맵안의 월퀘포함)\n')
print('실제플레이 관련\nVO_tips 스토리중 기믹 조언\nVO_HS - 주전자\nVO_gameplay - 플레이 대사\nVO_freetalk - 직접 대화걸때 대사\nVO_friendship - 캐릭터창에서 대사\nVO_Card 원스스톤 대사\n')
print('입력 : ')

DataSelect=input()
DataSetList=['VO_COOP','VO_EQ','VO_AQ','VO_LQ','VO_WQ','VO_tips','VO_HS','VO_gameplay','VO_freetalk','VO_friendship','VO_Card']

if DataSelect not in DataSetList:
    print('잘못된 입력입니다.')
    exit()

print('추출한 캐릭터명을 영어로 입력해주세요 ex) 느비예트 -> neuvillette \n')
print('오류가 난다면 json 파일을 열고 해당 캐릭터의 보이스라인중 sourceFileName에 적힌 캐릭터네임을 입력해주세요\n')
print('입력 : ')
character = input()

fileName = character+' '+DataSelect+'.txt'
keyword = DataSelect+('\\VO_')+character


print('\n'+character+' '+DataSelect+' 해시값 리스트\n')
print(keyword)

with open ("KR_Output.json", "r", encoding='UTF8') as f:
    data = json.load(f)
    type(data)

data.keys()
f = open(fileName, 'w')
count = int(0)

for json_key in data.keys():
    try:
        if data[json_key]['sourceFileName'] :
            text = data[json_key]['sourceFileName']
            if text.startswith(keyword) :
                Value = json_key
                print(Value)
                f.write(Value+'\n')
                count = count+int(1)
    except:
        count = count+int(0)
        
f.close()
print('\n'+str(count)+'개의 해시값 추출 완료')
