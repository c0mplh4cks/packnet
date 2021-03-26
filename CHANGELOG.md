# CHANGELOG

**Additions [+], modifications [~], deletions [x] and notes [!] are described per version in this document.**



### v1.0.0

  * **[!]** **Released on GitHub & PyPi**


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
    * Connect Acknowledgement
    * Subscribe Request
    * Subscribe Acknowledgement
    * Publish
  * **[~]** Updated installation instructions in `README.md`


### v1.6.1

  * **[~]** Added ICMPv6 to `__init__.py`


### v2.0.0

  * **[!]** **Reupload on GitHub & PyPi**
    * new GitHub url: `https://github.com/c0mplh4cks/packnet`
    * new PyPi url: `https://pypi.org/project/packnet`
  * **[~]** Renamed package from `c0mplh4cks-pylib` to `packnet`
  * **[~]** Changed Header object name to `Header` in every Protocol module
  * **[~]** Modified imports in `__init__.py`
  * **[x]** Removed `examples`
  * **[x]** Removed `screem`
  * **[x]** Removed usage instructions


### v2.0.1

  * **[+]** Documentation added in `README.md`
  * **[~]** Renamed `SubscribeREQ` to `Subscribe` in MQTT Protocol module
  * **[~]** Fixed `__init__.py` by importing every Protocol module
  * **[~]** Removed `vhl` attribute in IPv4 Header and replaced by version and header length
  * **[~]** Changed 0b0110 to 6 in IPv6 Header object for improved readability


### v2.0.2

  * **[+]** Added `getpublicip` function to standards
  * **[~]** Changed table of contents, minor changes for readability and moved about section in `README.md`
  * **[~]** Changed the reading of options in TCP (Must be improved in future)


### v2.0.3

  * **[~]** Numerous fixes to the options in the TCP protocol module
  * **[~]** Changed how the ip gets returned in the `getpublicip` function in the `standards` module


### v2.1.0

  * **[+]** Added `protocol` attribute to every protocol
  * **[+]** Added Packager module for automated interpreting and building networking packets
  * **[+]** Added `RAW` module for raw undecodable data
  * **[+]** Added AAAA types to DNS module
  * **[+]** Added `getmac` function to interface module for requiring MAC addresses using ARP
  * **[~]** Changed how the `getpublicip` function required the public ip by using sockets
  * **[~]** Fixed pointer bugs in `standards.decode.name` function
  * **[~]** Fixed DNS flags bug
  * **[~]** Fixed DNS Answer length mistake
  * **[~]** Fixed automatic card binder in the interface module


### v2.1.1

  * **[~]** Changed method name in `packager` class from `build` to `fill`
  * **[~]** Changed by adding source and destination arguments to `fill` method from the `packager` module
  * **[+]** Added `build` method to `packager` class for encoding the contents
  * **[~]** `getmac` method from the `interface` class now makes use the `Packager` module


### v2.1.2

  * **[+]** Added `Redirect` class to `ICMP` module
  * **[~]** Small improvements for `interface` module
  * **[~]** Improved `packager` module


### v2.1.3

  * **[~]** Moved `Tree` from `Packager` to separate module
  * **[~]** Changed `Packager` to make use of `Tree` module
  * **[~]** Fixed `tobyte` function from `standards` module


### v2.1.4

  * **[~]** Improved `build` functions by replacing lists with dictionaries


### v3.0.0

*This update was focused on internal code improvements*

  * **[+]** Added `datatype` classes
    * INT
    * IP
    * NAME
    * MAC
    * CHECKSUM
    * ADDR
    * LEN
  * **[x]** Removed `encode`, `decode` and `checksum` functions from `standards`
  * **[~]** Changed `standards` into `general`
  * **[~]** Numerous small fixes
  * **[+]** Added `Frame` class for improved code
  * **[+]** Added automated compression for `name` in `DNS`
  * **[x]** Removed MQTT protocol class
  * **[x]** Removed RAW class
  * **[~]** **Made big internal code improvements for each file**


### v3.0.1

  * **[+]** Added/Updated documentation
  * **[~]** Bug causing permission issues in `general` fixed
  * **[~]** The `maclookup` function in `general` now returns `None` when no result has been found
  * **[~]** Improved debug info for `debug` method in `frame`
  * **[~]** Improved usage of `ADDR` and `LEN` custom datatypes
  * **[~]** Adjusted usage of `ICMPv6` and `IPv6` to work with improved `IP` datatype
  * **[~]** Fixed mistake regarding `randint` in `ICMP.Echo`
