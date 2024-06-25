import pandas as pd # type: ignore
import random

# 고유 ID 범위 설정
num_rooms = 1000
num_facilities = 26

# 각 room_id가 가질 facility 개수 범위 설정
min_facilities_per_room = 5
max_facilities_per_room = 10

# 데이터 저장을 위한 리스트 초기화
room_facilities = []

# room_id와 facility 할당
for room_id in range(1, num_rooms + 1):
    # room_id별 facility 개수 랜덤 설정
    num_facilities_for_room = random.randint(min_facilities_per_room, max_facilities_per_room)
    
    # facility 리스트 생성
    facilities = random.sample(range(1, num_facilities + 1), num_facilities_for_room)
    
    # room_id와 facility 관계 저장
    for facility in facilities:
        room_facilities.append((room_id, facility))

# DataFrame 생성
df = pd.DataFrame(room_facilities, columns=['room_id', 'facility'])

# 고유 ID 추가
df['id'] = range(1, len(df) + 1)

# 컬럼 순서 재배치
df = df[['id', 'room_id', 'facility']]

# 엑셀 파일로 저장
df.to_excel('room_facilities.xlsx', index=False, engine='openpyxl')
