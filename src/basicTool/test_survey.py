import unittest
from basicTool.survey import AnonymousSurvey


class TestAnonymousSurvey( unittest.TestCase ):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Chinese']

    def tearDown(self):
        self.responses.clear()

    def test_store_single_response(self):
        """针对AnonymousSurvey类的测试"""
        self.my_survey.store_response( self.responses[0] )
        self.assertIn( self.responses[0], self.my_survey.responses )

    def test_store_three_response(self):
        """测试三个答案并存储正确"""
        for response in self.responses:
            self.my_survey.store_response( response )
        for response in self.responses:
            self.assertIn( response, self.my_survey.responses )


if __name__ == '__main__':
    unittest.main()
