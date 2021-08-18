import json
import sys
import zlib
 
import base45
import cbor2
from cose.messages import CoseMessage
 
if len(sys.argv) > 1:
    payload = sys.argv[1][4:]
    print("\n\033[1m\033[95m Decoding payload: "+ payload + "\033[0m\n")
    
    # decode Base45 (remove HC1: prefix)
    decoded = base45.b45decode(payload)
    
    # decompress using zlib
    decompressed = zlib.decompress(decoded)
    # decode COSE message (no signature verification done)
    cose = CoseMessage.decode(decompressed)
    # decode the CBOR encoded payload and print as json
    print(json.dumps(cbor2.loads(cose.payload), indent=2))
else:
    print("\033[91m (!) Missing payload. Usage: python decode.py 'HC1:6BFNXSI...'")
