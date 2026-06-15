from services.learning_content import generate_learning_content

text = """
FastAPI is a Python framework used
to build APIs quickly.
"""

result = generate_learning_content(text)

print(result)