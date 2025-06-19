# WebAppSample
WebAppSample

.deployment   파일
[config]
SCM_DO_BUILD_DURING_DEPLOYMENT=false

.env
# Azure 구독 및 리소스 그룹, 워크스페이스 정보 설정
SUBSCRIPTION_ID = "구독 ID"       # 구독 ID로 변경

RESOURCE_GROUP = "rg-yb001"         # 리소스 그룹 이름으로 변경

WORKSPACE_NAME = "yb001-ml"         # AML 워크스페이스 이름으로 변경
