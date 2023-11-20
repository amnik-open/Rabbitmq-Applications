import pika, sys

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='logs', routing_key='',
                      body=message)
print(" [x] Sent 'Hello World!'")

connection.close()
