import pytest
from ghkit.error import LoginError, MessengerError, SendError, AccessTokenError, MessageTypeError


def test_messenger_error():
    """测试消息通知错误"""
    # 测试通用消息错误
    error = MessengerError("消息错误")
    assert str(error) == "消息错误"
    
    # 测试登录错误
    error = LoginError("登录失败")
    assert str(error) == "登录失败"
    
    # 测试发送错误
    error = SendError("发送失败")
    assert str(error) == "发送失败"
    
    # 测试获取凭证错误
    error = AccessTokenError("获取凭证失败")
    assert str(error) == "获取凭证失败"
    
    # 测试消息格式错误
    error = MessageTypeError("消息格式错误")
    assert str(error) == "消息格式错误"


def test_error_inheritance():
    """测试错误继承"""
    # 测试错误继承关系
    assert isinstance(LoginError(""), MessengerError)
    assert isinstance(SendError(""), MessengerError)
    assert isinstance(AccessTokenError(""), MessengerError)
    assert isinstance(MessageTypeError(""), MessengerError) 