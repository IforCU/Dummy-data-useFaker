import pandas as pd
import random

# 데이터 생성 함수
def generate_data():
    data = []
    for room_id in range(1, 1001):
        # id는 room_id와 동일하게 설정
        id = room_id
        
        # 침대 수 합계가 1~4 범위 내에 있도록 설정
        total_beds = random.randint(1, 4)
        queen_bed_count = random.randint(0, total_beds)
        remaining_beds = total_beds - queen_bed_count
        
        king_bed_count = random.randint(0, remaining_beds)
        remaining_beds -= king_bed_count
        
        double_bed_count = remaining_beds
        
        data.append({
            'id': id,
            'queen_bed_count': queen_bed_count,
            'king_bed_count': king_bed_count,
            'double_bed_count': double_bed_count,
            'room_id': room_id
        })
    
    return data

# 데이터 프레임 생성
data = generate_data()
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('bedroom.xlsx', index=False)
