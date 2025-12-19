"""
main01.py
수업용 GitHub 업로드 테스트 예제

기능:
1) 오늘 날짜/시간 출력
2) 현재 폴더의 파일 목록 출력
3) 사용자 입력 받아 인사 출력
"""

from datetime import datetime
from pathlib import Path


def show_time():
    now = datetime.now()
    print(f"[시간] {now:%Y-%m-%d %H:%M:%S}")


def list_files():
    here = Path(".")
    files = sorted([p.name for p in here.iterdir() if p.is_file()])

    print("\n[현재 폴더 파일 목록]")
    for name in files:
        print(f"- {name}")


def greet():
    name = input("\n이름을 입력하세요: ").strip()
    if not name:
        name = "지수"
    print(f"안녕하세요, {name}! GitHub 업로드 테스트 성공!")


def main():
    show_time()
    list_files()
    greet()


if __name__ == "__main__":
    main()
