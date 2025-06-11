import time
import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

# 용산구 이태원2동의 중심 좌표를 기준으로 데이터 생성
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.5348, 126.9936],
    columns=["lat", "lon"],
)
st.map(df)

# 지도에 사용된 좌표 리스트 출력
coordinate_list = df[['lat', 'lon']].values.tolist()
st.write("좌표 리스트:", coordinate_list)

# 고유한 user_agent로 Nominatim 인스턴스 생성
geolocator = Nominatim(user_agent="MyAppIdentifier/1.0 (contact@yourdomain.com)")
address_list = []

# 예제에서는 좌표 리스트의 처음 5개만 처리함
for coord in coordinate_list[:5]:
    try:
        location = geolocator.reverse(f"{coord[0]}, {coord[1]}", language='ko')
        address_list.append(location.address if location else "주소를 찾을 수 없음")
    except Exception as e:
        address_list.append(f"오류 발생: {e}")
    time.sleep(1)  # Nominatim 정책에 따라 요청 간 지연 추가

# 주소 리스트를 표 형식으로 출력
address_df = pd.DataFrame(address_list, columns=["주소"])
st.table(address_df)

# 오류 없이 정상 응답된 주소만 필터링 (즉, 인터넷 연결 시설 확인된 것으로 간주)
confirmed_addresses = [addr for addr in address_list if not addr.startswith("오류") and "찾을 수 없음" not in addr]
confirmed_df = pd.DataFrame(confirmed_addresses, columns=["확인된 주소"])
st.table(confirmed_df)