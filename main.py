class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(f"문제: {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer
    
default_quizzes = [
    Quiz("7 + 5는?", ["10", "11", "12", "13"], 3),
    Quiz("12 - 4는?", ["8", "6", "7", "9"], 1),
    Quiz("3 × 6는?", ["18", "16", "17", "19"], 1),
    Quiz("16 ÷ 4는?", ["2", "4", "3", "5"], 2),
    Quiz("9 + 8는?", ["17", "15", "16", "18"], 1),
]

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
