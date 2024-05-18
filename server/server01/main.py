import time
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connection established')

@sio.event
def disconnect():
    print('Disconnected from server')

def send_facial_expression(expression):
    sio.emit('facial_expression', expression)

if __name__ == '__main__':
    sio.connect('http://localhost:5000')

    expressions = ['facial-expression-1', 'facial-expression-2', 'facial-expression-3', 'robot_off']
    for expr in expressions:
        send_facial_expression(expr)
        time.sleep(2)  # Wait for 2 seconds

    sio.disconnect()
