# Server/client demo application

## Introduction

The aim is to provide a testing application where the server part will be replaces by a C# program that interfaces with Dartfish.
The events sent by the client will therefore create a event in the Dartfish Live Collaboration environment (when a session is running).

## Usage

First start the server using the command below. The default ip address is 127.0.0.1 (localhost) and the default port is 5000.

```bash
python ./server.py

python ./server.py --host 10.10.135.212 --port 5000
```

Then start the client 

```bash
python ./client.py

python ./client.py --host 10.10.135.212 --port 5000
```

Whatever is sent by the client will be sent back by the server upon arrival.

## Supported commmands

A number of JSON objects can be sent to the Dartfish application. There are all documenten below.

### Relay exchange event

The basics for each relay exchange event should contain a number of mandatory fields:

| tag                             | value                                                   |
|---------------------------------|---------------------------------------------------------|
| type                            | relay_exchange                                          |
| pushing-athlete                 | name of the athlete that is pushing the other athlete   |
| incoming athlete                | name of the athlete that received the push              |
| corner                          | 1 = first corner after the finish line, 2 other corner  |
| timestamp                       | unix epoch in milliseconds since Jan 1st, 1970          |
| metrics                         | obeject containing all metrics/evaluations of the push  |
| - acceleration-incoming-athlete | acceleration expressed in m/s^2                         | 
| - desceleration-pushing-athlete | desceleration expressed in m/s^2                        |            

Please extend upon this to complete the list of metrics


```json
{
    "type" : "relay_exchange",
    "pushing-athlete" : "John Doe",
    "incoming-athlete" : "Jane Doe",
    "corner" : 1,
    "timestamp" : 1733318347197,
    "metrics" : {
        "acceleration-incoming-athlete" : 5.3,
        "desceleration-pushing-athlete" : 2.3,
        
    }
}
```

### Start recording event

```json
{
    "type" : "start_recording",
    "timestamp" : 1733318347197
}
```

### Stop recording event

```json
{
    "type" : "stop_recording",
    "timestamp" : 1733318347197
}
```

# Troubleshooting

Any questions/remarks can be addressed to maarten.slembrouck@ugent.be