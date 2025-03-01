# model-serving-structure

1. api.py 를 통한 entry point 생성
   - GET /api/data
   - docker 관리
2. tasks.py 를 통한 function 생성 (Celery)
   - task 관리 param 1~8 통해서 data 1~8 읽어서 type + data 리턴
   - common/data1~8.txt 읽기
   - docker 관리
3. Celery를 받기 위한 redis docker
4. k8s를 통한 function worker 관리

## celery worker 실행

`celery -A tasks worker --loglevel=info`
