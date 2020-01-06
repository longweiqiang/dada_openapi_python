#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 15:37
# @Author  : Weiqiang.long
# @Site    : 
# @File    : dada_client.py
# @Software: PyCharm
# @Description:

import hashlib

class DdMakeSign:

    def __init__(self, appKey, app_secret):
        self.appKey = appKey
        self.app_secret = app_secret


    def __jiamimd5(self, src):
        '''
        MD5加密
        :param src: 需要加密的数据
        :return: 加密后的数据
        '''
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()


    def make_sign(self, body):
        '''
        生成达达物流加密参数
        签名生成过程:
        第一步：将参与签名的参数按照键值(key)进行字典排序
        例如：将上述请求参数中的body、format、timestamp、app_key、v、source_id 进行字典排序。结果为：app_key、body、format、source_id、timestamp、v

        第二步：将排序过后的参数，进行key和value字符串拼接将参数中的key和value按照key的顺序进行字符串拼接。结果为：app_key123456body{"order_id":"20170301000001"}formatjsonsource_id73753timestamp1488363493v1.0

        第三步：将拼接后的字符串首尾加上app_secret秘钥，合成签名字符串将第二步的字符窜首尾拼接上app_secret。结果为：abcdefg123app_key123456body{"order_id":"20170301000001"}formatjsonsource_id73753timestamp1488363493v1.0abcdefg123

        第四步：对签名字符串进行MD5加密，生成32位的字符串对生成签名字符串进行MD5加密。结果为：71cee2d6544277940d8c72979e71d0e1

        第五步：将签名生成的32位字符串转换为大写将md5加密后的字符串转换为大写，结果为：71CEE2D6544277940D8C72979E71D0E1

        注：生成最终的签名的字符串：71CEE2D6544277940D8C72979E71D0E1作为请求参数的signature的值传入即可

        :param body: 需要加密的body数据
        :return:
        '''
        # 为body增加app_key
        body["app_key"] = self.appKey
        # 列表生成式，生成key=value格式（剔除signature字段）
        kv = ["".join(i) for i in body.items() if i[1] and i[0] != "signature"]
        # 参数名ASCII码从小到大排序
        str_kv = "".join(sorted(kv))
        # 将拼接后的字符串首尾加上app_secret秘钥，合成签名字符串
        striSignTemp = self.app_secret + str_kv + self.app_secret
        # 对签名字符串进行MD5加密，生成32位的字符串并转换为大写
        sign = self.__jiamimd5(src=striSignTemp).upper()
        # 得到sign签名后更新body值
        body["signature"] = sign
        return body
