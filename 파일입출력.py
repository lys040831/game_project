file=open("test.txt","w",encoding="utf-8")
file.write("안녕")
file.close()

with open("test.txt","w",encoding="utf-8")as file:
	file.write("안녕하세요")
	
with open("memo.txt","w",encoding="utf-8")as file: #한 줄 저장
	file.write("오늘은 파일 입출력을 배웁니다.")   
	
with open("memo.txt","w",encoding="utf-8")as file: #여러 줄 저장
	file.write("1일차 학습\n")
	file.write("2일차 학습\n")
	file.write("3일차 학습\n")

# open()은 파일을 여는 함수.
# "test.txt"는 파일 이름.
# "w"는 쓰기 모드.
# encoding="utf-8"은 한글이 깨지지 않도록 설정.
# with를 사용하면 파일을 자동으로 닫아줍니다.

with open("memo.txt","r",encoding="utf-8")as file:
	content=file.read()

print(content)

# # "r"은 읽기 모드입니다.
# # read()는 파일 전체 내용을 하나의 문자열로 읽어옵니다.

with open("memo.txt","r",encoding="utf-8")as file:
	line1=file.readline()
	line2=file.readline()

print(line1)
print(line2)

with open("memo.txt","r",encoding="utf-8")as file:
	
	lines=file.readlines()
print(lines) #['1일차 학습\n','2일차 학습\n','3일차 학습\n']
# for line in lines:
# 	print(line.strip())  #리스트 반복문 써서 하나하나 읽어주는 것도 가능



with open("memo.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")