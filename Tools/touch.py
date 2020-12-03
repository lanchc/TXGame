import wda
import Tools.utility as common


# 操作设备
c = wda.Client()
s = c.session()


# 触摸事件
class Touch:

    # 构造方法
    def __init__(self):
        pass

    # 点击位置
    def click(self, x, y):
        xx, yy = common.kk_transform_coordinates(x, y)
        s.tap(xx, yy)

    # 延迟点击
    def delayed_click(self, x, y):
        xx, yy = common.kk_transform_coordinates(x, y)
        s.tap(xx, yy)
        common.kk_delay()

    # 截图当前
    def screen_capture(self):
        s.screenshot('./kk_screen.png')
        common.kk_delay()

# 导出类
kk_touch = Touch()