# Symptoms

Sometimes (I did not yet recognize a pattern), the kitchen light switches will stop working.
The log of the z2m container will not show anything on switch press.
When triggering a light from the Home Assistant or Z2M web interface, an error appears in the logs:
```
[2024-08-02 07:30:24] error:    z2m: Publish 'set' 'state' to 'kitchen_light_sink' failed: 'Error: ZCL command 0xb4e3f9fffe8327cb/1 genOnOff.off({}, {"timeout":10000,"disableResponse":false,"disableRecovery":false,"disableDefaultResponse":false,"direction":0,"srcEndpoint":null,"reservedBits":0,"manufacturerCode":null,"transactionSequenceNumber":null,"writeUndiv":false}) failed (no response received (72))'

```

This also happens with some of my smart plugs while others are working just fine.
```
[2024-08-02 07:29:25] error:    z2m: Publish 'set' 'state' to 'plug02' failed: 'Error: ZCL command 0xa4c138c44434498e/1 genOnOff.off({}, {"timeout":10000,"disableResponse":false,"disableRecovery":false,"disableDefaultResponse":false,"direction":0,"srcEndpoint":null,"reservedBits":0,"manufacturerCode":null,"transactionSequenceNumber":null,"writeUndiv":false}) failed (no response received (65))'
```

# Debugging
I then switched z2m into debugging mode by switching the log-level to "debug".
According to the sebug log, the sending of the zigbee messages for controlling the lights via web interface works just fine.
The ZCL command gets send to the controller who sends it over the air to the light.
It then waits for a response that is never received, resulting in the error above.

Maybe the light controller needs to be re-bound?

# Solution
Reconnecting light controllers to power solved the problem...
