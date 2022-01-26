import sys
import zmq

def start_client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")

    socket.send_string("18429 クライアントからサーバへ送るメッセージ：サーバ君調子はどう？")

    recv_message = socket.recv_string()
    print("%s" % recv_message)

    socket.close()
    context.destroy()

if __name__ == "__main__":
    start_client()