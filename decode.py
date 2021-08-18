import json
import sys
import zlib
 
import base45
import cbor2
from cose.messages import CoseMessage

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

 
if len(sys.argv) > 1:
    payload = sys.argv[1][4:]
    print("\n\033[1m" + "*** Decoding payload: " + "\033[0m" + payload + "\n")
    
    # decode Base45 (remove HC1: prefix)
    decoded = base45.b45decode(payload)
    
    # decompress using zlib
    decompressed = zlib.decompress(decoded)

    # decode COSE message (no signature verification done)
    cose = CoseMessage.decode(decompressed)

    # decode the CBOR encoded payload as a JSON
    json_output = json.dumps(cbor2.loads(cose.payload), indent=2)

    # format JSON to be printed
    formatted_output = highlight(json_output, JsonLexer(), TerminalFormatter())
    print(formatted_output)

else:
    print("\033[91m (!) Missing payload. Usage: python decode.py 'HC1:6BFNXSI...'")
