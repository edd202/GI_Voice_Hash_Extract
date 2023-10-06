import shutil
import os


print('복사할 해시값이 있는 텍스트파일의 이름을 입력하세요')
print('ex) Korean_YaeMiko_VO_friendship')
inputFile = input()
fileName = inputFile+'.txt'

path='./'+inputFile

if not os.path.isdir(path):
    os.mkdir(inputFile)

f = open(fileName, 'r')
lines = f.readlines()
for line in lines:
    fromFile = './dest_wav/'+line.strip()+'.wav'
    toFile = './'+inputFile+'/'+line.strip()+'.wav'
    shutil.copy2(fromFile,toFile)
f.close()

print(inputFile+' 작업완료')
