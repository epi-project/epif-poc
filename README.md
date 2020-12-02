# EPIF PoC

## Interception
All outgoing network traffic from the compute container (`node-a`) is transparently intercepted and send to the redirector deamon (`redirector.py`), which is running locally in the compute container. The redirector extracts the original destination, i.e. address and port (`SO_ORIGINAL_DST`), and forwards the traffic to the proxy (`node-b`), along with the original destination. The communication between the redirector and the proxy is based on SOCKS.