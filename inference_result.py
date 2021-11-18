import json
import streamlit as st
import socket
import sys


average_processing_time = 0
average_communication_time = 0
image_id = 1

sum_processing_time = 0
sum_communication_time = 0
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8552        # Port to listen on (non-privileged ports are > 1023)


def write_data(parsed_data):
	global image_id
	global sum_processing_time	
	global sum_communication_time

	global average_processing_time 
	global average_communication_time 

	data = json.loads(parsed_data)
	
	filename = image_id
	processing_time = round(data['processing_time (ms)'],3)
	sending_time = round(data['sending_time (ms)'],3)
	total_time = round (data['total_time (ms)'], 3)
	text = data['text']


	st.header("""Time measurement""")
	st.write("""Processing time:  """ + str(processing_time)+"ms")
	st.write("""Comunnication time:  """ + str(sending_time)+"ms")
	st.write("""Total time:  """ + str(total_time) +"ms")

	sum_communication_time += sending_time
	sum_processing_time += processing_time

	average_communication_time = round(sum_communication_time / image_id , 3)
	average_processing_time = round(sum_processing_time / image_id, 3)

	st.write("""Average processing time:  """ + str(average_processing_time)+"ms")
	st.write("""Average communication time:  """ + str(average_processing_time)+"ms")

	st.write("""Filename:  """ + str(filename))
	st.write("""Detected text:  """ )
	st.write(text)

	image_id += 1


	




def main():
	st.title('Running inference server...')

	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind(( '', PORT))
			s.listen()
			conn, addr = s.accept()
			with conn:
				st.write("""Connection accepted from IP: """ + str(addr[0]))
				st.write("""Ready to receive data: """)
				while True:
					data = conn.recv(1024).decode('utf-8')    # this returns a JSON-formatted String
					try:
						parsed_data = json.loads(json.dumps(data))

						write_data(parsed_data)
						if not data:
							break
					except Exception as e:

						st.write("An exception ocurred: " + str(e))
						break
					
	except KeyboardInterrupt:
		raise SystemExit



if __name__ == "__main__":
	main()
