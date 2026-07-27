import ast


class ASTParser:

    def parse(self, code: str):

        tree = ast.parse(code)

        result = {
            "imports": [],
            "classes": [],
            "functions": [],
            "variables": []
        }

        for node in ast.walk(tree):

            # import os
            if isinstance(node, ast.Import):

                for alias in node.names:
                    result["imports"].append(alias.name)

            # from fastapi import FastAPI
            elif isinstance(node, ast.ImportFrom):

                module = node.module

                for alias in node.names:
                    result["imports"].append(f"{module}.{alias.name}")

            # class MyClass
            elif isinstance(node, ast.ClassDef):

                result["classes"].append(node.name)

            # def my_function()
            elif isinstance(node, ast.FunctionDef):

                result["functions"].append(node.name)

            # x = 10
            elif isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(target, ast.Name):
                        result["variables"].append(target.id)

        return result