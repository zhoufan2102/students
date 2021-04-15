
# 界面

import time
class View:

    @classmethod   # 用类方法
    def welcome_view(cls):
        #  时间银行系统
        #  开户，查询，存款，取款，转账，改密，锁卡，解锁，补卡，销户，退出

        print('*******************************')
        print('*****                     *****')
        print('*****        世界银行       *****')
        print('*****         12.0        *****')
        print('*****                     *****')
        print('*****    欢迎来到世界银行！   *****')
        print('*****                     *****')
        print('*****                     *****')
        print('*****                     *****')
        print('*******************************')

        time.sleep(2)
    # 登录
    @classmethod
    def login(cls):
        # 模拟用户
        user = {'zhangsan':'123456'}

        #输入用户名
        user_name = input("请输入用户名：")
        if user_name not in user:
            print('=>用户名不存在')
            return
        # 输入密码
        password = input('请输入密码：')
        if user[user_name] !=password:
            print('=>密码错误！')
            return

        # 登录成功
        print('=>恭喜你！登录成功！正在加载主页面...')
        time.sleep(1)
        return True

    # 主界面
    @classmethod
    def main_view(cls):
        #  时间银行系统
        #  开户，查询，存款，取款，转账，改密，锁卡，解锁，补卡，销户，退出

        print('************************************')
        print('*****                           *****')
        print('*****             世界银行        *****')
        print('*****      （1）开户   （2）查询    *****')
        print('*****      （3）存款   （4）取款    *****')
        print('*****      （5）转账  （6）改密     *****')
        print('*****      （7）锁卡   （8）解锁    *****')
        print('*****      （9）补卡   （0）销户    *****')
        print('*****            （q）退出         *****')
        print('**************************************')

