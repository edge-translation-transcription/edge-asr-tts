#!/bin/bash

# Start Redis
REDIS_PID=$(pgrep redis-server)

if [ -z "$REDIS_PID" ]; then
	echo "Starting Redis..."
	redis-server --daemonize yes
else
	echo "Redis is already running with PID: $REDIS_PID"
fi

echo "Launching GUI"
# Start streamlit in the background

STREAMLIT_PID=$(pgrep -f 'streamlit run')

if [ ! -z "$STREAMLIT_PID" ]; then
	echo "Killing streamlit process with PID: $STREAMLIT_PID"
	kill -9 $STREAMLIT_PID
else
	echo "No streamlit process currently running"
fi
streamlit run message_gui.py --server.port 8501 --server.headless true --browser.gatherUsageStats false & 

# launch main app with whatever commandline args are sent in
python3.11 -W "ignore" diart_whisper.py "$@"
