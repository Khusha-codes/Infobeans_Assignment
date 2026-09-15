import language_tool_python

tool = language_tool_python.LanguageTool("en-US")

text = "She go to college every day."

matches = tool.check(text)

print(matches)