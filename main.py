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

def get_number_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = input(prompt).strip()


            if user_input == "":
                print(f"잘못된 입력입니다. {min_value}~{max_value} 중에서 선택하세요.")
                continue


            number = int(user_input)


            if min_value <= number <= max_value:
                return number
            else:
                print(f"잘못된 입력입니다. {min_value}~{max_value} 중에서 선택하세요.")


        except ValueError:
            print(f"잘못된 입력입니다. {min_value}~{max_value} 중에서 선택하세요.")
        except KeyboardInterrupt:
            print("\n프로그램을 안전하게 종료합니다.")
            return max_value
        except EOFError:
            print("\n입력이 종료되어 프로그램을 안전하게 종료합니다.")
            return max_value

def main():
    while True:
        show_menu()
        choice = get_number_input("선택: ", 1, 5)


        if choice == 1:
            print("퀴즈 풀기 기능 준비 중")
        elif choice == 2:
            print("퀴즈 추가 기능 준비 중")
        elif choice == 3:
            print("퀴즈 목록 기능 준비 중")
        elif choice == 4:
            print("점수 확인 기능 준비 중")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
