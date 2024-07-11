#!/bin/bash

# Check if a file path is provided as an argument
if [ $# -lt 1 ]; then
  echo "Usage: $0 <wyoming-satellite dir> <mqtt-client-script-path> [arguments for wyoming satellite init script]"
  exit 1
fi

satellite_dir="$1"
mqtt_client_script="$2"

# Change directory to the provided file path
cd "$(dirname "$satellite_dir")" || { 
  echo "Error: Could not change directory to '$(dirname "$satellite_dir")'" >&2
  exit 1
}

name=""
name_index=0

# Find the index of --name in arguments 3 and beyond
for ((i=3; i<=$#; i++)); do
  if [[ "${!i}" == "--name" ]]; then
    name_index=$i
    break
  fi
done

if [[ $name_index -gt 0 ]]; then
  # Extract the name (argument after --name)
  name="${@:$((name_index + 1)):1}"
fi

if [[ -z "$name" ]]; then
  echo "Error: --name option not found."
  exit 1
fi

echo "Starting with wyoming-satellite at '$satellite_dir' and client script at '$mqtt_client_script' for name '$name':"

# Execute foo.sh with the remaining arguments
./client_main.sh ${@:3} \
    --startup-command "python $mqtt_client_script '$name' startup" \
    --detect-command "python $mqtt_client_script '$name' detect" \
    --streaming-start-command "python $mqtt_client_script '$name' streaming-start" \
    --streaming-stop-command "python $mqtt_client_script '$name' streaming-stop" \
    --detection-command "python $mqtt_client_script '$name' detection" \
    --transcript-command "python $mqtt_client_script '$name' transcript" \
    --stt-start-command "python $mqtt_client_script '$name' stt-start" \
    --stt-stop-command "python $mqtt_client_script '$name' stt-stop" \
    --synthesize-command "python $mqtt_client_script '$name' synthesize" \
    --tts-start-command "python $mqtt_client_script '$name' tts-start" \
    --tts-stop-command "python $mqtt_client_script '$name' tts-stop" \
    --error-command "python $mqtt_client_script '$name' error" \
    --connected-command "python $mqtt_client_script '$name' connected" \
    --disconnected-command "python $mqtt_client_script '$name' disconnected" \
    --timer-started-command "python $mqtt_client_script '$name' timer-started" \
    --timer-updated-command "python $mqtt_client_script '$name' timer-updated" \
    --timer-cancelled-command "python $mqtt_client_script '$name' timer-cancelled" \
    --timer-finished-command "python $mqtt_client_script '$name' timer-finished"