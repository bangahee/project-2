import json

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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

class QuizGame:
    def __init__(self, state_file="state.json"):
        self.state_file = state_file
        self.default_quizzes = [
            Quiz("7 + 5는?", ["10", "11", "12", "13"], 3),
            Quiz("12 - 4는?", ["8", "6", "7", "9"], 1),
            Quiz("3 × 6는?", ["18", "16", "17", "19"], 1),
            Quiz("16 ÷ 4는?", ["2", "4", "3", "5"], 2),
            Quiz("9 + 8는?", ["17", "15", "16", "18"], 1),
        ]
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def load_state(self):
        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            quiz_data = data.get("quizzes", [])
            self.quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in quiz_data
            ]
            self.best_score = data.get("best_score")

            if not self.quizzes:
                self.quizzes = self.default_quizzes.copy()

        except FileNotFoundError:
            self.quizzes = self.default_quizzes.copy()
            self.best_score = None
        except json.JSONDecodeError:
            print("state.json 파일 형식이 올바르지 않아 기본 퀴즈를 불러옵니다.")
            self.quizzes = self.default_quizzes.copy()
            self.best_score = None
        except Exception:
            print("파일 불러오기 중 오류가 발생하여 기본 퀴즈를 불러옵니다.")
            self.quizzes = self.default_quizzes.copy()
            self.best_score = None

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception:
            print("파일 저장 중 오류가 발생했습니다.")

    def show_menu(self):
        print("\n" + "=" * 40)
        print("기본 사칙연산 퀴즈")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_number_input(self, prompt, min_value, max_value):
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

    def get_text_input(self, prompt):
        while True:
            try:
                user_input = input(prompt).strip()

                if user_input == "":
                    print("빈 입력은 허용되지 않습니다. 다시 입력하세요.")
                    continue

                return user_input

            except KeyboardInterrupt:
                print("\n입력이 중단되었습니다. 메뉴로 돌아갑니다.")
                return None
            except EOFError:
                print("\n입력이 종료되었습니다. 메뉴로 돌아갑니다.")
                return None

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        correct_count = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print("\n" + "-" * 40)
            print(f"[문제 {index}]")
            quiz.display()

            user_answer = self.get_number_input("정답 입력 (1~4): ", 1, 4)

            if user_answer is None:
                print("퀴즈 풀이를 종료하고 메뉴로 돌아갑니다.")
                return

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다! 정답은 {quiz.answer}번입니다.")

        score = int((correct_count / len(self.quizzes)) * 100)

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("\n새로운 최고 점수입니다!")

        self.save_state()

        print("\n" + "=" * 40)
        print(f"결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답!")
        print(f"점수: {score}점")
        print("=" * 40)

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")

        question = self.get_text_input("문제를 입력하세요: ")
        if question is None:
            return

        choices = []
        for i in range(1, 5):
            choice = self.get_text_input(f"선택지 {i}: ")
            if choice is None:
                return
            choices.append(choice)

        answer = self.get_number_input("정답 번호 (1~4): ", 1, 4)
        if answer is None:
            return

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()

        print("퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("-" * 40)

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_number_input("선택: ", 1, 5)

            if choice is None or choice == 5:
                print("프로그램을 종료합니다.")
                break
            elif choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_best_score()

if __name__ == "__main__":
    game = QuizGame()
    game.run()
