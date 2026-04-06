def show_menu():
    print("\n" + "=" * 40)
    print("기본 사칙연산 퀴즈")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            print("퀴즈 풀기 기능 준비 중")
        elif choice == "2":
            print("퀴즈 추가 기능 준비 중")
        elif choice == "3":
            print("퀴즈 목록 기능 준비 중")
        elif choice == "4":
            print("점수 확인 기능 준비 중")
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~5 중에서 선택하세요.")

if __name__ == "__main__":
    main()