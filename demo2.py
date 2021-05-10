from tidevice._usbmux import Usbmux
from tidevice import Device
# from tidevice import *
from pprint import pprint
from tidevice._ipautil import IPAReader, IPAError


if __name__ == '__main__':
    print("测试代码")
    # 设备链接信息
    d = Device()
    print(d.name)
    # USB操作
    u = Usbmux()
    print(u.device_list())

    buid = u.read_system_BUID()
    print("BUID:", buid)

    d = Device()
    dev_pkey = d.get_value("DevicePublicKey", no_session=True)
    print("DevicePublicKey:", dev_pkey)

    wifi_address = d.get_value("WiFiAddress", no_session=True)
    print("WiFi Address:", wifi_address)

    app_arr = d.connect_instruments().app_list()

    for item in app_arr:
        print("================================================")
        print("DisplayName:", item["DisplayName"])
        print("Version:", item["Version"])
        print("CFBundleIdentifier:", item["CFBundleIdentifier"])
        print("Type:", item["Type"])
        print("BundlePath:", item["BundlePath"])



    # 重启手机
    # d.reboot()
    # print(d.get_value())

    # IPAReader, IPAError



    # with d.create_inner_connection() as s:
    #     ret = s.send_recv_packet({
    #         "Request": "GetValue",
    #         "Label": "example",
    #     })
    #     pprint(ret['Value'])

## 安装ipa
# from tidevice._ipautil import IPAReader, IPAError
#
#
# def test_get_infoplist(wda_filepath: str):
#     ir = IPAReader(wda_filepath)
#     assert ir.get_bundle_id() == "com.facebook.WebDriverAgentRunner.xctrunner"
#
#     data = ir.get_mobileprovision()
#     assert "Version" in data
#     assert data['Version'] == 1