**\[GitHub 메모 - 지수용]**

## 수업 중 빠른 사용 루틴

1. 파일 수정 후 저장
2. git status        (상태 확인)
3. git add .
4. git commit -m "수업 파일 추가"
5. git push


**0) 처음 1번만(또는 확인)**

git config --global user.name "poiuss"
git config --global user.email "88subini@gmail.net"

**확인**

git config --global --get user.name
git config --global --get user.email


**1) 완전 새 폴더를 GitHub에 처음 올릴 때**

(왜) 이 폴더를 Git 저장소로 만들고, 첫 업로드를 한다.

git init

(왜) 이 폴더에 .git이 생기고 Git이 관리 시작함


**git branch -M main**

(왜) 브랜치 이름을 main으로 통일


**git add .**

(왜) 올릴 파일을 "스테이징"에 올림


**git commit -m "첫 업로드"**

(왜) 스테이징된 파일을 하나의 기록(커밋)으로 저장

**git remote add origin https://github.com/아이디/저장소이름.git**

(왜) 내 폴더와 GitHub 저장소를 연결


**git push -u origin main**

(왜) GitHub로 업로드 + 이후 push 기본 대상 설정


**2) 업데이트(수정/추가 후 반복)**

(왜) 바뀐 것만 다시 기록하고 GitHub에 올린다.

git add .
git commit -m "설명"
git push

**3) push 인증**

Username: poiuss
Password: GitHub 비밀번호가 아니라 토큰(PAT)


###

다음 이미지의 Git 명령 요약 (VS Code 기준)

Pull: 원격 변경 사항 가져오기 및 병합
Push: 로컬 커밋을 원격으로 업로드
Clone: 원격 저장소를 새 로컬에 복제
Checkout to...: 브랜치 전환 및 신규 브랜치 생성
Fetch: 원격 저장소의 변경 이력만 갱신
Commit: 변경 사항을 로컬 저장소에 기록
Commit > Changes > Branch: 변경 파일 관리와 브랜치 작업 하위 메뉴
Remote: 원격 저장소 관리(추가/삭제/목록)
Stash: 현재 작업 숨기고 다른 작업 가능
Tags: 특정 커밋에 태그 만들기
Worktrees: 하나의 저장소에서 여러 워크트리 관리


