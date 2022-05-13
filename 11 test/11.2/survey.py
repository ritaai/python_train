# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月17日
"""
class AnonymousSurvey:
    """手机匿名调查问卷地答案。"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到地所有答卷"""
        print("Survey result:")
        for response in self.responses:
            print(f"- {response}")
