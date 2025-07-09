class TestData:
    # 有效登录凭据
    VALID_LOGINS = [
        ("testuser1", "SecurePass123!"),
        ("testuser2", "AnotherPass456@")
    ]
    
    # 无效登录凭据及预期错误
    INVALID_LOGINS = [
        ("invaliduser", "wrongpass", "用户名或密码错误"),
        ("testuser1", "wrongpass", "用户名或密码错误"),
        ("", "password", "用户名不能为空"),
        ("testuser", "", "密码不能为空")
    ]
    
    # 无效注册数据及预期错误
    INVALID_REGISTRATIONS = [
        ("", "", "", ["用户名不能为空", "邮箱不能为空", "密码不能为空"]),
        ("user", "invalidemail", "short", ["邮箱格式不正确", "密码至少8个字符"]),
        ("existinguser", "existing@example.com", "ValidPass123!", ["用户名已存在", "邮箱已注册"])
    ]