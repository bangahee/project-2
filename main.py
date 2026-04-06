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
            return None
        except EOFError:
            print("\n입력이 종료되어 프로그램을 안전하게 종료합니다.")
            return None

def play_quiz(quizzes):
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    print(f"\n퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    correct_count = 0

    for index, quiz in enumerate(quizzes, start=1):
        print("\n" + "-" * 40)
        print(f"[문제 {index}]")
        quiz.display()

        user_answer = get_number_input("정답 입력 (1~4): ", 1, 4)

        if user_answer is None:
            print("퀴즈 풀이를 종료하고 메뉴로 돌아갑니다.")
            return

        if quiz.is_correct(user_answer):
            print("정답입니다!")
            correct_count += 1
        else:
            print(f"오답입니다! 정답은 {quiz.answer}번입니다.")

    score = int((correct_count / len(quizzes)) * 100)

    print("\n" + "=" * 40)
    print(f"결과: {len(quizzes)}문제 중 {correct_count}문제 정답!")
    print(f"점수: {score}점")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = get_number_input("선택: ", 1, 5)

        if choice is None or choice == 5:
            print("프로그램을 종료합니다.")
            break
        elif choice == 1:
            play_quiz(default_quizzes)
        elif choice == 2:
            print("퀴즈 추가 기능 준비 중")
        elif choice == 3:
            print("퀴즈 목록 기능 준비 중")
        elif choice == 4:
            print("점수 확인 기능 준비 중")

if __name__ == "__main__":
    main()
