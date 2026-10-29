# HW4 : todo 앱에 API 더하기

## 더한 것

- 설명 칸(note)을 API로도 주고받게 했습니다.
- GET /api/todos/?done=true로 완료한 것만 골라 받게 했습니다.

## 실행하는 법

가상환경을 활성화한 뒤 `HW4` 폴더에서 실행합니다.

    pip install -r ../requirements.txt
    flask --debug run
    화면 http://127.0.0.1:5000/
    문서 http://127.0.0.1:5000/api/docs

## 화면

### 1. 주소 여섯 줄이 모두 보이는 문서
![docs] <img width="943" height="861" alt="docs" src="https://github.com/user-attachments/assets/0c4842ed-189e-436a-b905-7c16cb542826" />


### 2. note를 넣어 만들었더니 201이 온 모습
![post] <img width="886" height="414" alt="post" src="https://github.com/user-attachments/assets/446b26f2-9c9c-4bf7-a5a2-8345efa104d7" />


### 3. 없는 번호를 불렀더니 404가 온 모습
![404] <img width="882" height="330" alt="notfound" src="https://github.com/user-attachments/assets/ef64730a-4096-4faa-aa9e-0bd537d427e0" />
