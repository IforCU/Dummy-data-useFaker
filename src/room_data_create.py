import random
from openpyxl import Workbook
from faker import Faker

# Faker 인스턴스 생성 (한국어 로케일)
fake = Faker('ko_KR')

# 엑셀 워크북 및 시트 생성
wb = Workbook()
ws = wb.active
ws.title = "숙소 정보"

# 헤더 추가
headers = ["title", "sub_title", "price", "guest_favorite", "max_people_count", "bathrooms_count", "description"]
ws.append(headers)

# 더미 데이터 생성 및 추가
for _ in range(1000):  # 100개의 데이터를 생성
    title = fake.sentence(nb_words=6)  # 6개의 단어로 구성된 제목 생성
    sub_title = ""  # 비어 있는 서브 타이틀
    price = random.randint(100, 10000) * 100  # 10000~1000000 사이의 랜덤 가격
    guest_favorite = ""  # 비어 있는 guest_favorite
    max_people_count = random.randint(1, 20)  # 1~20 사이의 랜덤 인원수
    bathrooms_count = random.randint(1, 10)  # 1~10 사이의 랜덤 욕실 수
    description = fake.paragraph(nb_sentences=3)  # 3개의 문장으로 구성된 설명 생성
    
    ws.append([title, sub_title, price, guest_favorite, max_people_count, bathrooms_count, description])

# 엑셀 파일 저장
wb.save("숙소_정보.xlsx")
