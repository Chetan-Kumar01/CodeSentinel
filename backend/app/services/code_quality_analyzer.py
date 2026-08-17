import ast


class CodeQualityAnalyzer:

    def analyze(self, code):

        tree = ast.parse(code)

        issues = []

        for node in ast.walk(tree):

            # Check long functions
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

                function_lines = node.end_lineno - node.lineno + 1

                if function_lines > 50:

                    issues.append({
                        "type": "long_function",
                        "severity": "medium",
                        "name": node.name,
                        "message": f"Function '{node.name}' is {function_lines} lines long."
                    })

                # Check too many arguments
                argument_count = len(node.args.args)

                if argument_count > 5:

                    issues.append({
                        "type": "too_many_arguments",
                        "severity": "medium",
                        "name": node.name,
                        "message": f"Function '{node.name}' has {argument_count} arguments."
                    })

                # Check missing docstring
                if ast.get_docstring(node) is None:

                    issues.append({
                        "type": "missing_docstring",
                        "severity": "low",
                        "name": node.name,
                        "message": f"Function '{node.name}' has no docstring."
                    })

            # Check long classes
            elif isinstance(node, ast.ClassDef):

                class_lines = node.end_lineno - node.lineno + 1

                if class_lines > 300:

                    issues.append({
                        "type": "long_class",
                        "severity": "high",
                        "name": node.name,
                        "message": f"Class '{node.name}' is {class_lines} lines long."
                    })

                # Check missing class docstring
                if ast.get_docstring(node) is None:

                    issues.append({
                        "type": "missing_docstring",
                        "severity": "low",
                        "name": node.name,
                        "message": f"Class '{node.name}' has no docstring."
                    })

        return {
            "total_issues": len(issues),
            "issues": issues
        }