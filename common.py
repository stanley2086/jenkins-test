import os

def get_UDID_list():

    UDID_list=[]
    cmd = "adb devices"
    get_cmd = os.popen(cmd).readlines()
    device_number=str(get_cmd).count('device')
    if device_number >1:
        devices_list=get_cmd[1:-1]
        for item in devices_list:
            UDID=item.strip('\tdevice\n')
            UDID_list.append(UDID)
        return (UDID_list)
    else:
        return False

import os
import subprocess

# 得到手机信息
def get_phone_info(devices):
    cmd = "adb -s "+ devices +" shell cat /system/build.prop "
    phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    print(phone_info)
    l_list = {}
    release = "ro.build.version.release=" # 版本
    model = "ro.product.model=" #型号
    brand = "ro.product.brand=" # 品牌
    device = "ro.product.device=" # 设备名
    for line in phone_info:
         for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                l_list["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                l_list["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                l_list["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                l_list["device"] = temp[len(device) :]
                break
    print('F_get_phone_info: %s' %l_list)
    return l_list

def call_adb(command):
    command_result = ''
    command_text = 'adb %s' % command
    results = os.popen(command_text, "r")
    while 1:
        line = results.readline()
        if not line: break
        command_result += line
    results.close()
    return command_result

    # 检查设备
def attached_devices():
    result = call_adb("devices")
    devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
    flag = [device for device in devices if len(device) > 2]
    if flag:
        return True
    else:
        return False