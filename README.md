# About
This is a simple python script to read what is inside the QR-code from your European Covid19 Vaccine Certificate.

Idea and Code from this article:
https://hackernoon.com/how-to-decode-your-own-eu-vaccination-green-pass-with-a-few-lines-of-python-9v2c37s1

</br>

---

</br>

## How to run
#### 1. Use a QR-Code reader to get the content of your own QR-Code. 
You can try some online tool like this one: https://www.onlinebarcodereader.com/


The extracted code should look similar to this example:

> HC1:6BFNX1:HM*I0PS3TLU.NGMU5AG8JKM:SF9VN1RFBIKJ:3AXL1RR+ 8::N$OAG+RC4NKT1:P4.33GH40HD*98UIHJIDB 4N*2R7C*MCV+1AY
3:YP*YVNUHC.G-NFPIR6UBRRQL9K5%L4.Q*4986NBHP95R*QFLNUDTQH-GYRN2FMGO73ZG6ZTJZC:$0$MTZUF2A81R9NEBTU2Y437XCI9DU 4S3N%JRP:HPE3$ 435QJ+UJVGYLJIMPI%2+YSUXHB42VE5M44%IJLX0SYI7BU+EGCSHG:AQ+58
CEN RAXI:D53H8EA0+WAI9M8JC0D0S%8PO00DJAPE3 GZZB:X85Y8345MOLUZ3+HT0TRS76MW2O.0CGL EQ5AI.XM5 01LCWBA.RE.-SUYH+S7SBE0%B-KT+YSMFCLTQQQ6LEHG.P46UNL6DA2C$AF-SQ00A58HYO5:M8 7S$ULGC-IP49MZCS
U8ST3HDRJNPV3UJADJ9BVV:7K13B4WQ+DCTEG4V8OT09797FZMQ3/A7DU0.3D148IDZ%UDR9CYF


</br>


#### 2. Install `poetry` to manage python dependencies.
Quick install: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

Read more: https://python-poetry.org/docs/#installation


</br>


#### 3. Type `poetry run python decode.py 'HC1:6BFNXSI...'` from the root directory.

This is what the output should look like:
```json
{
  "1": "DE",
  "4": 1655209933,
  "6": 1623673933,
  "-260": { 
    "1": {
      "v": [
        {
          "ci": "URN:UVCI:01DE/IZ12345A/21E0JXD7UQY6ECLM3WT7YF#8",
          "co": "DE",
          "dn": 2,
          "dt": "2021-04-01",
          "is": "Robert Koch-Institut",
          "ma": "ORG-100031184",
          "mp": "EU/1/20/1507",
          "sd": 2,
          "tg": "840539006",
          "vp": "1119349007"
        }
      ],
      "dob": "1964-08-12",
      "nam": {
        "fn": "Mustermann",
        "gn": "Erika",
        "fnt": "MUSTERMANN",
        "gnt": "ERIKA"
      },
      "ver": "1.0.0"
    }
  }
}
```
