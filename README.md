# R6 Server Changer (R6SC)

Ubisoft사의 Rainbow Six Siege 게임 플레이시 할당되는 중계 서버를 유저가 직접 간편하게 변경할 수 있는 기능을 포함한 소프트웨어입니다.

프로그램의 재배포는 언제든지 자유롭게 가능하지만 반드시 이 Github repository 링크나 https://blog.xeros.dev/215 를 통해 해주시기 바랍니다. (제 3자가 악성코드를 바인딩, 재패키징하여 배포하는것을 방지하기 위함입니다. )

## 버전 목록 및 패치 내역

#### 1.0.0

- 초기 개발 단계 완성 이후 배포

#### 1.1.1

- 프로그램 버전, 업데이트 체크 API 서버와의 통신이 원할하지 않아 실행시 오작동하는 문제 수정
- 서버 설정 변경 이후 프로그램 재부팅 전까지 프로그램 화면에 바뀐 서버명이 정상적으로 노출되지 않던 문제 수정
- 게임 클라이언트에서 최근 서버 변경 설정값을 변경하여, 서버 변경 기능이 정상적으로 반영되지 않던 문제 수정
- 아이콘이 게임 내 캐릭터인 "도깨비"의 아이콘으로 변경되었습니다.

## 현재 발견되거나 예상되는 문제점

- Ubisoft 계정 프로필이 여러개인 경우 정상 작동하지 않을것으로 예상됨
- Ubisoft 설정 파일이 위치한 디렉토리에 관련없는 파일 혹은 디렉토리가 존재 할 경우 정상 작동하지 않을것으로 예상됨

