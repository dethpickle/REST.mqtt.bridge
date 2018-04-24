# REST.mqtt.bridge
A bridge for automation - some things like REST, others only speak mqtt

## Usage
Send a `POST` to `http://127.0.0.1:8088/RESTbridge`
Headers: `Content-Type: application/x-www-form-urlencoded`   

Body (form):
* `channel: "sensornamehere"`
* `payload: {"val":72.2}`
* `type: "sensornameprefix/"`

That will post to the channel `topicbase/type/channel` with the payload.  My use case likes a JSON payload since I have sensors in Home Assistant that can reference a JSON element.
 
