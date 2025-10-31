## Controlling your Fritz Smart Home devices via Alexa

Unfortunately the very useful skill FBSmarthome was discontinued due to the associated cost within the AWS environment.
AVM announced to bring full matter support on their FritzBox (which would help) but it is not clear when this will 
happen. However, when you are using an Amazon Echo as your Zigbee and Matter Hub, it would be nice to also steer 
AVM Fritz devices (such as heating controllers DECT 302) via Alexa.

Using this simple class, you can just bild an Alexa-FritzBox integration yourself.
A very simple setup could look like this:

1. Setup an URL caller skill within Alexa
2. Setup a smarthome user within your Fritzbox
3. Setup a simple API that calls this class based on the predefined URLs within the skill

Step 3 is the interesting part of course, but if you know a bit of Python and Flask, it is no biggie.
There are full scale libs to accomplish this but for me this was just enough.

See also:
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AHA-HTTP-Interface.pdf