class MetricsAnalyzer:

    def analyze(self, code, ast_result):

        lines = code.splitlines()

        total_lines = len(lines)

        blank_lines = 0
        comment_lines = 0
        code_lines = 0

        for line in lines:

            stripped = line.strip()

            if not stripped:
                blank_lines += 1

            elif stripped.startswith("#"):
                comment_lines += 1

            else:
                code_lines += 1

        metrics = {
            "total_lines": total_lines,
            "code_lines": code_lines,
            "blank_lines": blank_lines,
            "comment_lines": comment_lines,
            "number_of_imports": len(ast_result["imports"]),
            "number_of_classes": len(ast_result["classes"]),
            "number_of_functions": len(ast_result["functions"]),
            "number_of_variables": len(ast_result["variables"])
        }

        return metrics