# -*- coding: utf-8 -*-
import json
import os

from zvt import zvt_env


class Config(object):
    jq_username = None
    jq_password = None
    http_proxy = "127.0.0.1:1087"
    https_proxy = "127.0.0.1:1087"
    smtp_host = "smtpdm.aliyun.com"
    smtp_port = "80"
    email_username = None
    email_password = None
    wechat_app_id = None
    wechat_app_secrect = None

    @classmethod
    def load(cls):
        config_path = os.path.join(zvt_env[''], 'config.json')
        if not os.path.exists(config_path):
            from shutil import copyfile
            copyfile(os.path.abspath(os.path.join(os.path.dirname(__file__), 'samples', 'config.json')), config_path)

        with open(config_path) as f:
            config_json = json.load(f)
            for k in config_json:
                zvt_env[k] = config_json[k]

