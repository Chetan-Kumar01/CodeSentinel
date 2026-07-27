from app.services.ast_parser import ASTParser

with open("test.py", "r") as f:
    code = f.read()

parser = ASTParser()

result = parser.parse(code)

print(result)
