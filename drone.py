# ドローン制御を定義するクラス
class c(object):
    def __init__(self, DRONE_NAME):
        assert isinstance(DRONE_NAME, object)
        self.drone_name = DRONE_NAME

    # 指定座標まで飛行していくメソッド
    def C(self,a,b,c):
        # ドローンのAPI呼び出し箇所、ダミー
        print("{0}の目的座標:{1},{2}へ高度:{3}[m]で飛行".format(self.drone_name,a,b,c))


ABCDIFG = c("鳥羽ドローン１号")
ABCDIFG.C(342,754,100)
