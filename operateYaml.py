__author__ = 'shikun'
import yaml

# -*- coding:utf-8 -*-

def getYaml(path):
    #读取yaml文件，形成一个list，list中由字典组成（键值对，比如[{de:'j',udid:334},{de:'m",udid:445}]
    try:
        with open(path, encoding='utf-8') as f:
            yaml_item = yaml.load(f)
            print('F_getYaml:%s'%yaml_item)
            return yaml_item
    except FileNotFoundError:
        print(u"找不到文件")

