# CHANGELOG

**Additions [+], modifications [~] and deletions [x] are described per version in this document.**



### v1.0.0

  * **Released on GitHub & PyPi**


### v1.3.0

  * **[+]** Added DNS Protocol module
    * DNS Header
    * Query
    * Answer
  * **[+]** Added Interface module
  * **[~]** Changed internal package structure


### v1.4.0

  * **[+]** Added ICMP Protocol module
    * ICMP Header
    * Echo


### v1.4.2

  * **[~]** Minor Changes to numerous modules
  * **[~]** Minor Fixes to numerous modules


### v1.5.0

  * **[+]** Added TimeExceeded Object to ICMP module
  * **[+]** Added Functions to the Standard module
    * Bytes to Int
    * Int to Bytes
  * **[+]** Added TCP Protocol
    * TCP Header
  * **[~]** Updated `README.md` files
  * **[~]** Updated `examples`
  * **[x]** Removed `chatapp` from `examples`


### v1.6.0

  * **[+]** Added IPv6 Address encoding/decoding to Standard module
  * **[+]** Added OSI Model Layer Information to each protocol module
  * **[+]** Added IPv6 Protocol module
    * IPv6 Header
  * **[+]** Added ICMPv6 Protocol module
    * ICMPv6 Header
    * Echo
  * **[+]** Added MQTT Protocol module
    * MQTT Header
    * Connect
    * Connect Acknowlegdement
    * Subscribe Request
    * Subscribe Acknowlegdement
    * Publish
  * **[~]** Updated installation instructions in `README.md`


### v1.6.1

  * **[~]** Added ICMPv6 to `__init__.py`


### v2.0.0

  * **Reupload on GitHub & PyPi**
  * new GitHub url: `https://github.com/c0mplh4cks/packnet`
  * new PyPi url: `https://pypi.org/project/packnet`
  * **[~]** Renamed package from `c0mplh4cks-pylib` to `packnet`
  * **[~]** Changed Header object name to `Header` in every Protocol module
  * **[~]** Modified imports in `__init__.py`
  * **[x]** Removed `examples`
  * **[x]** Removed `screem`
  * **[x]** Removed usage instructions
