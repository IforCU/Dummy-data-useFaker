import random
import openpyxl
from faker import Faker
import openpyxl.workbook
from faker.providers import DynamicProvider

# Faker 라이브러리를 지정함.
fake = Faker()

# openpyxl를 이용해 Workbook 생성
workbook = openpyxl.Workbook()

# Workbook의 Sheet를 지정함
sheet = workbook.active

# column 값 설정
# 예시 id, 이름, 이미지, 역할, 슈퍼호스트, 호스팅 날짜, 가입날짜, 국적, 내위치, 전화번호, 이메일 등등
columns = ["id", "name", "image", "roll", "superhost", "host_since", "created_at", "country", "location", "phone_number", "email"]
sheet.append(columns)

# 1000개의 데이터 셋 생성
for i in range(1, 1001):
    # 호스팅 날짜는 가입 날짜보다 빠르면 안된다.
    signup_date = fake.date_between(start_date='-20y', end_date='today')
    hosting_date = fake.date_between(start_date=signup_date, end_date='today') if random.choice([True, False]) else None
    # 호스팅 날짜가 없으면 user 있으면 host가 되어야 함.
    role = "HOST" if hosting_date else "USER"
    # 역할이 host면 슈퍼호스트 유무를 가질 수 있고 user면 무조건 false
    superhost = fake.boolean() if role == "HOST" else False
    
    row = [
        i,  # ID
        fake.name(),  # 이름
        fake.image_url(),  # 이미지
        role,  # 역할
        superhost,  # 슈퍼호스트
        hosting_date.isoformat() if hosting_date else "N/A",  # 호스팅 날짜
        signup_date.isoformat(),  # 가입 날짜
        fake.country(),  # 국적
        fake.address(),  # 내 위치
        fake.phone_number(),  # 전화번호
        fake.email()  # 이메일
    ]
    sheet.append(row)

# 엑셀 파일 저장
workbook.save("user.xlsx")
