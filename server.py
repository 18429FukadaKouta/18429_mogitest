import zmq

def start_server():
    context=zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5556")

 

    while True:
        message=socket.recv_string()
        print("%s" % message)
        socket.send_string("18429 サーバからクライアントに送るメッセージ：絶好調やで")

    socket.close()
    context.destroy()

if __name__ == "__main__":
    start_server()