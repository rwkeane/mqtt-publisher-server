# mqtt-publisher-server

This repo provides two main utilities:
- A gRPC based server that publishes to a specifies MQTT server based on credentials provided in a separate file.
- A client script, allowing users to call into the server asynchronously.

The original use case for this script is to support callbacks from the [wyoming-satellite](https://github.com/rhasspy/wyoming-satellite) to the original Home Assistant instance, but it can work as a general-purpose tool to send commands from the command line over mqtt using a very lightweight script. 

NOTE THE FOLLOWING:
- An example input file is provided in `/tools/example_input.txt`.
- A script showing how the tool can be used is included at `tools/start_satellite_broker.sh`.
- An example service file that can be used to set this tool to run at boot has been included at `/tools/mqtt-publisher.service`.

If using this tool for its original purpose - sending commands from a wyoming satellite to Home Assistant, this can be done by calling:

```
start_satellite_broker.sh <wyoming-src-dir> <mqtt-client-script-path> REMAINING ARGS
```

Where `REMAINING ARGS` are all normal inputs to the wyoming satellite script. Note that the `Event Commands` are already supplied by the `start_satellite_broker.sh`, so they cannot be provided again here.