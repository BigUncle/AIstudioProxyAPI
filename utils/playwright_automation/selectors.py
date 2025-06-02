"""
此模块用于存放 Playwright 自动化过程中常用的 CSS 选择器或 XPath 表达式。

将选择器集中管理在此处有以下好处：
1.  提高代码的可维护性：当页面结构发生变化时，只需要修改此文件中的选择器，而不需要在多个测试脚本中查找和修改。
2.  提高代码的可读性：通过有意义的常量名称代替冗长的选择器字符串，使测试脚本更易于理解。
3.  减少重复：避免在不同的测试用例中重复定义相同的选择器。

示例：
LOGIN_BUTTON = "#login-button"
USERNAME_INPUT = "input[name='username']"
PASSWORD_INPUT = "//input[@id='password']"  # XPath 示例
"""

# 可以在下方定义常量选择器
# 例如:
# GOOGLE_SEARCH_BOX = "textarea[name='q']"