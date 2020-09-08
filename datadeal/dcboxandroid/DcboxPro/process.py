from dcboxandroid.DcboxPro.dcbox198 import ProScript


def main(ip,v):

    # se=expr.device_detect()
    # se='127.0.0.1:21503'

    ps=ProScript(IP=ip)
    ps.install(ve=v)
    ps.click_login()
    ps.first_passwd_login()
    ps.logout()
    ps.verify_login()
    ps.logout()
    ps.forgot_pswd()
    ps.pawd_login()



def main_model_login():
    """
    密码登录
    忘记密码

    请确保不是首次登录app
    """
    se = '127.0.0.1:21503'
    ps = ProScript(se)
    ps.install()
    ps.click_login()
    ps.pawd_login()
    ps.logout()
    ps.forgot_pswd()
    ps.pawd_login()

