from faker import Faker
from openpyxl import Workbook
import random
from datetime import datetime, timedelta

# Faker 인스턴스 생성
faker = Faker()

# Workbook 생성
wb = Workbook()
ws = wb.active

# 엑셀 파일의 첫 번째 행에 헤더 추가
headers = ['id', 'cleanliness', 'accuracy', 'checkin', 'communication', 'location', 'value', 'creation_date', 'content', 'room_id', 'user_id']
ws.append(headers)

# 데이터 생성
record_id = 1  # id는 1부터 시작

# 각 room_id에 대해 5~100개의 데이터를 생성
for room_id in range(1, 1001):  # room_id는 1부터 1000까지
    num_reviews = random.randint(5, 100)  # 각 room_id에 대해 5~100개의 리뷰 생성
    for _ in range(num_reviews):
        cleanliness = random.randint(0, 5)
        accuracy = random.randint(0, 5)
        checkin = random.randint(0, 5)
        communication = random.randint(0, 5)
        location = random.randint(0, 5)
        value = random.randint(0, 5)
        
        # 최근 4년 이내의 날짜 생성
        start_date = datetime.now() - timedelta(days=4*365)
        random_days = random.randint(0, 4*365)
        creation_date = start_date + timedelta(days=random_days)
        creation_date_str = creation_date.strftime("%Y-%m-%d")
        
        content = faker.text(max_nb_chars=200)  # 리뷰 내용 생성
        user_id = random.randint(1, 3534)
        
        ws.append([record_id, cleanliness, accuracy, checkin, communication, location, value, creation_date_str, content, room_id, user_id])
        record_id += 1

# 엑셀 파일 저장
wb.save("reviews_data.xlsx")
