import zmq
import time

from zmq.sugar import socket

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

i = 0
while True:
    i += 1
    for topic in range(1,4):

        data = topic * 1
        socket.send_string("{0} {1}".format("book/comic/kimetu/"+str(topic),data))
        print("Topic {0} <- {1} sent".format("book/comic/kimetu", data))
        socket.send_string("{0} {1}".format("book/comic/gintama/"+str(topic),data))
        print("Topic {0} <- {1} sent".format("book/comic/gintama", data))

    time.sleep(1)