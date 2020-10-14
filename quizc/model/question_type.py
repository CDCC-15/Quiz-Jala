import datetime
from enum import Enum
from quizc.model.validations import ValidatorType


class QuestionConfiguration(object):
    def __init__(self, has_additional_data, supported_validations):
        self.has_additional_data = has_additional_data
        self.supported_validations = supported_validations

    def convert_value(self, value):
        return value


class TextConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.MIN_LENGTH])


class DateConfiguration(QuestionConfiguration):
    DATE_FORMAT = '%d/%m/%Y'

    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.DATE])

    def convert_value(self, value):
        try:
            return datetime.datetime.strptime(value, DateConfiguration.DATE_FORMAT)
        except ValueError:
            return None


class PickOneQuestionConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, True, [ValidatorType.REQUIRED])


<<<<<<< HEAD
class NumericConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, True, [ValidatorType.REQUIRED, ValidatorType.MIN])

    def convert_value(self, value):
        return int(value)


=======
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1
class QuestionType(Enum):
    TEXT = (1, TextConfiguration())
    DATE = (2, DateConfiguration())
    PICK_ONE = (3, PickOneQuestionConfiguration())
<<<<<<< HEAD
    NUMERIC = (4, NumericConfiguration())
=======
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1

    def __init__(self, code, configuration):
        self.code = code
        self.configuration = configuration

    def get_validations(self):
        return self.configuration.supported_validations

    def get_code(self):
        return self.code

    def has_additional_data(self):
        return self.configuration.has_additional_data

    @staticmethod
<<<<<<< HEAD
    def get_by_code(code):
=======
    def get_by_code(code) :
>>>>>>> 90b8ccff3ce47341b3d767a3529804b87111e4d1
        for question_type in QuestionType:
            if question_type.code == code or question_type.code == int(code):
                return question_type
        return None
