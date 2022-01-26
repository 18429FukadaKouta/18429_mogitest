import sys
import zmq


topic = "book/comic"

#ZeroMQ のバックグラウンド・スレッドのコンテキスト
context = zmq.Context()

# このクライアントは、ポート5556に接続します（バックグラウンドにて）
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

#チャネルのめもりをあわせる
socket.setsockopt_string(zmq.SUBSCRIBE,topic)


while True:
    string = socket.recv_string()
    Topic, data = string.split()

    print("Topic {0} -> {1} received".format(Topic,data))