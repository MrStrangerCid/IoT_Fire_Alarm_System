#!/usr/local/bin/python
import nexmo

client = nexmo.Client(key='key', secret='secret')

client.send_message({
    'from': 'Fire Alarm',
    'to': 'number',
    'text': 'Fire has been detected! Vacate the premisses, contact local fire authority',
})
