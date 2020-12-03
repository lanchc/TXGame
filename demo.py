import wda
from Tools.touch import kk_touch
## 操作设备
c = wda.Client()
s = c.session()

# s.swipe(10, 100, 200, 100)
s.tap(100, 100)
# kk_touch.click(100, 100)