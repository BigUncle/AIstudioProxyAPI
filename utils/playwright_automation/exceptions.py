"""
此模块定义了 `playwright_automation` 模块特定的异常。
"""

class PlaywrightAutomationError(Exception):
    """
    Playwright 自动化模块的基础异常类。
    所有特定于此模块的自定义异常都应从此类继承。
    """
    pass

class BrowserLaunchError(PlaywrightAutomationError):
    """
    当启动浏览器失败时引发此异常。
    例如，如果无法找到浏览器可执行文件或启动参数无效。
    """
    pass

class NavigationError(PlaywrightAutomationError):
    """
    当页面导航失败时引发此异常。
    例如，URL 无效、页面加载超时或导航被阻止。
    """
    pass

class ElementNotFoundError(PlaywrightAutomationError):
    """
    当在页面上找不到指定的元素时引发此异常。
    """
    pass

class ElementInteractionError(PlaywrightAutomationError):
    """
    当与页面元素交互失败时引发此异常。
    例如，点击一个不可点击的元素或向一个不可编辑的字段输入文本。
    """
    pass