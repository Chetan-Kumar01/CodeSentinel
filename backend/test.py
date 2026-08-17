# import os
# import math

# from fastapi import FastAPI

# x = 10
# name = "Chetan"

# class Student:
#     pass


# def greet():
#     print("Hello")


# def add(a, b):
#     return a + b

from app.services.code_quality_analyzer import CodeQualityAnalyzer


code = """
def calculate(a, b, c, d, e, f):

    result = a + b + c + d + e + f

    return result
"""


analyzer = CodeQualityAnalyzer()

result = analyzer.analyze(code)

print(result)