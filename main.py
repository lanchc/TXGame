# 程序入口文件
import Tools.utility as common
from Tools.touch import kk_touch

if __name__ == '__main__':
    # 记录开始时间
    begin_time = common.kk_time_current_timestamp()

    while True:
        ## 点击结束
        kk_touch.delayed_click(1060, 676)
        ## 点击开始
        kk_touch.delayed_click(1096, 620)
        ## 重新开始
        kk_touch.delayed_click(1144, 688)
        ## 运行时间
        run_time = common.kk_time_difference(begin_time)
        ## 运行一分钟
        if run_time.seconds > 600 :
            print("运行10分钟了")
            common.kk_delay(5)
            ## 重新记录
            begin_time = common.kk_time_current_timestamp()