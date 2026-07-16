import streamlit as st
import redis
import time
import json
import logging

logging.basicConfig(level=logging.ERROR)

r = redis.Redis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)
st.empty()
st.title("Retail for All")
st.caption("Translate and caption conversations on resource contrained client devices")
channel = "r4a_messages"

pubsub = r.pubsub()
pubsub.subscribe(channel)
logging.debug(f"Subscribed to channel {channel}")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Begin speaking and I will respond in your language"}]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

while True:
    for redis_message in pubsub.listen():
        logging.debug(f"In loop, Message: {redis_message} received")
        
        if redis_message['type'] == "message" and redis_message['channel'] == channel:
            logging.debug(f"Received message {redis_message} from channel {channel}, processing..")
            message_data = json.loads(redis_message['data'])
            st.session_state.messages.append({'role': message_data['role'],'content': message_data['text']})
            st.chat_message(message_data['role']).write(message_data['text'])
    time.sleep(0.01)
