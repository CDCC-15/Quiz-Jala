<<<<<<< HEAD
from json_persistence import Store
=======
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1
from quizc.console.quiz_input_handler import QuestionInputHandler
from quizc.console.quiz_ui_menu import QuizUIMenu
from quizc.model.quiz import Quiz
from quizc.model.quiz_answers import QuizAnswer, Answer


class QuizUIHandler(object):

    @staticmethod
    def create_quiz() -> Quiz:
        menu = QuizUIMenu()
        return menu.handle_create_quiz()

<<<<<<< HEAD
    def fill_quiz(self, quiz) -> QuizAnswer:
=======
    @staticmethod
    def fill_quiz(quiz) -> QuizAnswer:
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1
        quiz_answer = QuizAnswer(quiz)
        question_handler = QuestionInputHandler()
        print("Quiz:" + quiz.title)
        for question in quiz.questions:
            answers = question_handler.ask_question_value(question)
            answer = Answer(answers, question)
            quiz_answer.add_answer(answer)
<<<<<<< HEAD
            self.store_quiz(quiz.title, quiz_answer)
=======
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1

        return quiz_answer

    @staticmethod
<<<<<<< HEAD
    def store_quiz(title, answer):
        store = Store(title, answer)
        store.save_data()

    @staticmethod
=======
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1
    def show_quiz(quiz_answer):
        print(quiz_answer.quiz.title)
        print("=============================================")
        for answer in quiz_answer.answers:
<<<<<<< HEAD
            print(answer.question.title)
            print("ATQ: " + answer.answers[0] + "\n")
=======
            print(answer)
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1

        return quiz_answer
