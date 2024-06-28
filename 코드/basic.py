import pandas as pd

# 파일 경로 (파일 경로가 정확한지 확인하세요)
file_path = r'C:\Users\Administrator\Desktop\대학\3학년 1학기\데이터마이닝 입문\전처리\pasta.csv'

try:
    # 'cp949' 인코딩으로 파일 읽기를 시도합니다
    data = pd.read_csv(file_path, encoding='cp949')
except FileNotFoundError:
    print("지정된 파일을 찾을 수 없습니다. 파일 경로를 확인하세요.")
    raise
except Exception as e:
    print(f"오류가 발생했습니다: {e}")
    raise

menu_list = [
    '스테이크와 폭립의 행복세트', '우삼겹 해장 파스타', '새우 바질페스토 파스타', '새우 비스크소스 파스타', '아란치니 로제 파스타',
    '매콤도로시크림파스타', '쉬림프 알리오올리오', '투움바 파스타', '도로시 크림 파스타', '우삼겹 알리오올리오',
    '봉골레 알리오올리오', '속풀이얼큰 파스타', '쉬림프&베이컨 로제파스타', '즈볼로제파스타', '미트소스 파스타',
    '베이컨 토마토파스타', '더블up치즈 뇨끼파스타', '새우 비스크소스 필라프', '우삼겹 필라프', '김치&베이컨 필라프',
    '쉬림프&베이컨 필라프', '치킨마요 필라프', '소고기야채 필라프', '투움바 크림리조또', '쉬림프&베이컨 크림리조또',
    '쉬림프&베이컨 로제리조또', '치킨너겟', '치킨텐더', '타코야끼', '감자튀김', '모둠튀김', '군만두 튀김',
    '육즙가득 통소세지', '새우튀김', '버팔로윙2개+가라아게2개', '버팔로윙', '가라아게', '치즈볼', '고구마튀김',
    '매쉬포테이토와 Grilled 스테이크', '단호박 샐러드와Grilled 스테이크', '단호박 샐러드와 Grilled 쉬림프',
    '매쉬포테이토와 Grilled왕새우', '도로시 찹스테이크', '큐브스테이크+Grilled왕새우', '도로시 감바스 알하이요+모닝빵2개',
    '폭립+감자튀김', '폭립 half+감자튀김', '포테이토 샐러드', '단호박 샐러드', '모닝빵$딸기잼'
]
# 메뉴 리스트를 길이에 따라 내림차순으로 정렬
menu_list_sorted = sorted(menu_list, key=len, reverse=True)

def match_menus(description):
    matched_menus = []
    if not isinstance(description, str):
        return ''  # 입력이 문자열이 아니면 빈 문자열 반환
    for menu in menu_list_sorted:
        if menu in description:
            matched_menus.append(menu)
    return ', '.join(matched_menus)  # 찾은 모든 메뉴를 쉼표로 구분된 문자열로 반환

# 'menu' 컬럼의 모든 항목을 문자열로 변환
data['menu'] = data['menu'].astype(str)

# 매칭 함수 적용
data['Selected_Menu'] = data['menu'].apply(match_menus)

# 결과 저장 경로
output_file_path = 'Processed_file_name.csv'
data.to_csv(output_file_path, index=False, encoding='utf-8-sig')

print("데이터 처리가 완료되었습니다. 파일이 저장되었습니다.")
