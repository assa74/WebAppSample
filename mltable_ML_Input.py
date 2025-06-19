from azure.ai.ml import MLClient
from azure.ai.ml.entities import Data
from azure.identity import DefaultAzureCredential

import mltable
import os

# Azure 구독 및 리소스 그룹, 워크스페이스 정보 설정
subscription_id = "dc6618c1-53d2-4bc8-ab82-68140c3fbde1"       # 구독 ID로 변경
resource_group = "rg-yb0616"         # 리소스 그룹 이름으로 변경
workspace_name = "yb0616aiml002"         # AML 워크스페이스 이름으로 변경

# CSV 파일 경로 설정
csv_path = "./mltable/fine_data_0616_mlt.csv"

# MLTable 객체 생성 (CSV 파일 기반)
ml_table = mltable.from_delimited_files(paths=[{"file": csv_path}])

# MLTable 파일을 저장할 폴더 지정 (예: 현재 디렉토리 내 "mltable" 폴더)
save_dir = "./mltable"
os.makedirs(save_dir, exist_ok=True)

# MLTable 저장 (YAML 파일 등으로 변환)
ml_table.save(save_dir)

print(f"MLTable 파일이 {save_dir}에 저장되었습니다.")



# 기본 자격 증명 사용 (Azure CLI 로그인 또는 환경 변수 구성 필요)
credential = DefaultAzureCredential()

# MLClient 객체 생성
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

# MLTable 파일이 저장된 폴더 경로 (YAML 파일 포함)
mltable_folder_path = "./mltable"  # 이전에 생성한 MLTable 폴더 경로

# Data 엔터티 생성 (MLTable 형식)
data_asset = Data(
    name="bs_MLTable2",
    path=mltable_folder_path,
    type="mltable",  # MLTable 형식임을 지정
    description="서초구 주소 데이터를 MLTable 형식으로 등록한 데이터 에셋",
)

# 데이터 에셋 등록 또는 업데이트
registered_data = ml_client.data.create_or_update(data_asset)
print(f"MLTable 데이터 에셋이 등록되었습니다: {registered_data.name}")

