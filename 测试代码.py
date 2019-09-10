import unittest
from name_function import get_formatted_name
from survey import AnonymousSurvey
'''
python标准库中的模块unittest提供了代码测试工具
单元测试用于核实函数的某个方面没有问题；
测试用例是一组单元测试，这些单元测试一起核实函数在各种情况下的行为都符合要求。
全覆盖测试用例包含一整套单元测试，覆盖了各种可能的使用方法。
'''


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Jason', 'joplin')
        self.assertEqual(formatted_name, 'Jason Joplin')


# unittest.main()


# 测试类
#    各种断言方法
'''
assertEqual(a, b) 核实a == b
assertNotEqual(a, b) 核实a != b
assertTrue(x) 核实x为True
assertFalse(x) 核实x为False
assertIn(item, list) 核实item在list中
assertNotIn(item, list)核实item不在list中
'''
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
while True:
    language = input("Language:")
    if language == 'q':
        break
    my_survey.store_response(language)

print("\nThank you to everyone who participate in the survey!")
my_survey.show_result()
