#!/usr/bin/env python
# encoding: utf-8
import requests  # 加载费时,之前加载过所以还好


def post_comment(msg):
    url = "http://geek.ai100.com.cn/?api"
    payload = {}
    payload["type"] = "comment"
    # "#test from paperweekly bot\n hello ai100"
    payload["comment_content"] = msg
    payload["post_id"] = 544  # 文章ID 94
    payload["user_id"] = 3  # pw=3
    try:
        # json:json data:表单 params:url参数
        response = requests.post(url, data=payload, timeout=2)
        return response
    except Exception as e:
        print(str(e))


def run(**kwargs):
    msg = kwargs.get("msg")
    print({"ai_forum": msg})
    content = msg  # "#test from paperweekly bot\n hello ai100"
    print(post_comment(content).content)
if __name__ == '__main__':
    post_comment("hello by pw bot")
