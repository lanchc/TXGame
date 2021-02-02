import wda
import time
from Tools.touch import kk_touch
## 操作设备
c = wda.Client()
s = c.session()

# s.swipe(10, 100, 200, 100)
# s.tap(100, 100)

#  设置
# s.tap(50, 120)
# 查找
# x --> 水平, y 垂直
# s.tap(150, 120)
# vpn
# s.tap(144, 146)

# s.tap(316, 624)

# kk_touch.delayed_click(100, 100)

s.screenshot('./kk_screen5.png')
# 坐标转化 PxCook
# 1060, 676
# 1096, 620
# 1144, 688

# 下一步
# 530，338
# 闯关
# 548,310
# 重新
# 572,344