# ドローン制御を定義するクラス
class DroneControl(object):#クラスの名前はCapWord方式
    def __init__(self, drone_name):#変数名は小文字
        assert isinstance(drone_name, object)
        self.drone_name = drone_name

    # 指定座標まで飛行していくメソッド
    def control(self,x,y,z):#関数名は小文字、変数名には意味を持たせる
        # ドローンのAPI呼び出し箇所、ダミー
        print("{0}の目的座標:{1},{2}へ高度:{3}[m]で飛行".format(self.drone_name,x,y,z))


drone = DroneControl("鳥羽ドローン１号")#変数名は小文字
drone.control(342,754,100)
