# PACKNET
*Hacked together into entirety by c0mplh4cks*


____


## About

This package is created to build low-level networking packets which can be used when building various types of applications. Using this package, it is possible to make packets ranging from OSI model level 2 to level 7. One of the endless applications could be a network device discovery tool using the address resolution protocol for example. Apart from only building numerous headers and payloads, this package makes it also possible to read received data and extract useful information, making it possible to interact with a Python script.


____


## Table of Contents
* [OSI model](#osi-model)
* [Installation](#installation)
  1. [PyPi](#installation-from-pypi)
  2. [GitHub](#installation-from-github)
* [Packager](#packager)
  1. [Building packets](#building-packets-using-packager)
  2. [Reading packets](#reading-packets-using-packager)
* [General](#general)
  1. [getpublicip](#getpublicip)
  2. [maclookup](#maclookup)
  3. [getmac](#getmac)
* [Interface](#interface)
* [Custom Datatypes](#custom-datatypes)
  1. [INT](#datatype-int)
  2. [IP](#datatype-ip)
  3. [MAC](#datatype-mac)
  4. [ADDR](#datatype-addr)
  5. [LEN](#datatype-len)
  6. [NAME](#datatype-name)
  7. [CHECKSUM](#datatype-checksum)
* [Protocol Classes](#protocol-classes)
  1. [ETHERNET](#protocol-ethernet)
  2. [ARP](#protocol-arp)
  3. [IPv4](#protocol-ipv4)
  4. [IPv6](#protocol-ipv6)
  5. [ICMP](#protocol-icmp)
  6. [ICMPv6](#protocol-icmpv6)
  7. [TCP](#protocol-tcp)
  8. [UDP](#protocol-udp)
  9. [DNS](#protocol-dns)


____


[Go back](#table-of-contents)
## OSI model

Open Systems Interconnection model


No | Layer        | Function                    | Protocol *(included in package)*
---|--------------|-----------------------------|------------------------------
7  | Application  | Application communication   | DNS
6  | Presentation | Representation & Encryption |
5  | Session      | Interhost communication     |
4  | Transport    | Connections & QoS           | TCP, UDP
3  | Network      | IP                          | IPv4, IPv6, ICMP, ICMPv6, ARP
2  | Data Link    | MAC                         | Ethernet
1  | Physical     | Bits                        |


Introduced to standardize networking protocols, allowing multiple networking devices from different developers to communicate among each other. The model consists of multiple layers with its own unique function. The OSI model differs from the TCP/IP model since it contains the presentation and session layers.


____


[Go back](#table-of-contents)
## Installation

The following will show how this package can be installed.


### Installation from PyPi

Install package by using `pip`:
```
pip3 install packnet
```
or
```
pip install packnet
```


### Installation from Github

Clone the repository:
```
git clone https://github.com/c0mplh4cks/packnet
```

Move inside the directory:
```
cd packnet
```

Install the library by running the following command:
```
pip3 install .
```
or
```
pip install .
```


____


[Go back](#table-of-contents)
## Packager

Packages is a class to simplify building packets.


### Building packets using packager

This example shows how to build a ARP packet using packager. For more information about the ARP class: [ARP](#protocol-arp)

```python
import packnet

src = ["192.168.0.1", 0, "aa:aa:aa:aa:aa:aa"]   # defining ip, port and mac
dst = ["192.168.0.2", 0, "bb:bb:bb:bb:bb:bb"]

package = packnet.Packager()        # creating packager object
package.fill( packnet.ARP.Header )  # tell packager to make use of the ARP class
package.src = src                   # set the source and destination addresses
package.dst = dst

print( package.packet )   # print the created packet in bytes
```


### Reading packets using packager

This example also shows the usage of packager using the ARP protocol.

```python
import packnet

encoded = b'\xbb\xbb\xbb\xbb\xbb\xbb\xaa\xaa\xaa\xaa\xaa\xaa\x08\x06\x00\x01\x08\x00\x06\x04\x00\x01\xaa\xaa\xaa\xaa\xaa\xaa\xc0\xa8\x00\x01\xbb\xbb\xbb\xbb\xbb\xbb\xc0\xa8\x00\x02'
# Encoded ARP packet ^ which we want to decode using packager.
package = packnet.Packager()  # creating packager object
package.packet = encoded      # decoding the encoded packet

# displaying the source and destination address
print( package.src, package.dst )

# looping through all the layers which the packet contained (these layers are not always the same as in the TCP/IP or OSI model)
for layer in package:
  print( layer )  

# displaying other useful information about the package object
package.debug()   

package[0].debug()  # accessing the first layer (ETHERNET)
package[1].debug()  # accessing the second layer (ETHERNET)

# displaying the operation code of the ARP protocol
print( package[1].op )  

```


____


[Go back](#table-of-contents)
## General

General is a module containing some simple functions for gathering information.


### getpublicip

This function does exactly what its name says: it requires the public ip by connecting to ifconfig.me

```python
import packnet

print( packnet.general.getpublicip() )
```


### maclookup

This function does a lookup for the vendor of the mac address.

```python
import packnet

result = packnet.general.maclookup("aa:aa:aa:aa:aa:aa") # Try with your own mac
print( result ) # The function returns `None` when there is no vendor matching the mac
```


### getmac

This function requires the mac address of the given ip address by using ARP.
**This function only works using root access, due to the use of a low-level socket**

```python
import packnet

print( packnet.general.getmac("192.168.0.0") )
# It returns a ADDR object containing the IP address, the port (always zero) and the MAC address
```


____


[Go back](#table-of-contents)
## Interface

This class makes it easier to require your addresses and simplifies the use of sockets.

```python
import packnet

# the passive argument can be set to `True` if you don't want the socket to be bound.
interface = packnet.Interface(card="eth0", port=0, passive=False, timeout=64)

# display the bounded card
print( interface.card )

# `interface.addr` returns a ADDR object containing the bound address.
print( interface.addr )

# `send` requires `bytes` as argument
interface.send( b"hello" )  # `hello` doesn't work, it needs to be a proper packet.

# the amount of bytes to be received, can be set using the `length` argument
print( interface.recv(length=1024) )
```


____


[Go back](#table-of-contents)
## Custom datatypes

Custom datatypes made to simplify encoding/decoding will be described here.
Each example will cover most of the methods/use cases and should not require further explanation.

### datatype INT

```python
import packnet

integer = packnet.INT(2, size=4, format="big")

print( integer )
print( integer.to_bytes() )
print( integer.from_bytes(b"\x00\x00\x00\xff") )  # returns (length of bytes, integer)

integer.integer = 5
```


### datatype IP

This class can be used of IPv4 and IPv6 by setting the version argument.

```python
import packnet

ip = packnet.IP("192.168.0.0", version=4)

print( ip )
print( ip.to_bytes() )
print( ip.from_bytes(b"\xff\xff\xff\xff") )  # returns (length of bytes, ip)

ip.ip = "127.0.0.1"
```


### datatype MAC

```python
import packnet

mac = packnet.MAC("ff:ff:ff:ff:ff:ff")

print( mac )
print( mac.to_bytes() )
print( mac.from_bytes(b"\x00\x00\x00\x00\x00\x00") )  # returns (length of bytes, ip)

mac.mac = "aa:aa:aa:aa:aa:aa"
```


### datatype ADDR

```python
import packnet

addr = packnet.ADDR(ip="127.0.0.1", version=4, port=0, mac="ff:ff:ff:ff:ff:ff")

print( addr )
print( addr.mac.to_bytes() )    # same for `ip` and `port`
print( addr[2].to_bytes() )
print( addr["mac"].to_bytes() )
addr.mac.from_bytes(b"\xff\xff\xff\xff\xff\xff")

addr.ip.version = 6
```


### datatype LEN

```python
import packnet

length = packnet.LEN(header=0, payload=0, total=0, size=1)

print( length )
length.size = 2
print( length.header )
length.header.integer = 20
print( length )
print( length.total, length[2], length["total"] )
```


### datatype NAME

```python
import packnet

name = packnet.NAME("test.com")
print( name, name.name )
print( name.to_bytes(header=b"") )  # the `header` argument is used for compression
name.from_bytes(b"\x05hello\x03com\x00", header=b"")
name.name = "test.net"
```


### datatype CHECKSUM

```python
import packnet

checksum = packnet.CHECKSUM(
  packnet.INT(1, size=2),
  b"\xff\xff"
)
print( checksum.to_bytes() )
```


____


[Go back](#table-of-contents)
## Protocol classes

Every protocol currently implemented will be explained here using examples.  
It is recommended to use the `Packager` class for decoding. More about `Packager` here: [Packager](#packeger).  
Each protocol class makes use of the custom datatypes. More about customd datatypes here: [Custom datatypes](#custom-datatypes).  
Not every attribute and application is covered, but the examples should give a good example for usage.


### protocol ETHERNET

```python
import packnet

# defining `ETHERNET.Header` object
eth = packnet.ETHERNET.Header()   

# setting attributes
eth.src.mac = "aa:aa:aa:aa:aa:aa"
eth.dst.mac = "bb:bb:bb:bb:bb:bb"
eth.protocol.integer = 0x0806

# printing encoded packet in bytes
print( eth.packet )

# print debug information
eth.debug()
```


### protcol ARP

```python
import packnet

# defining `ARP.Header` object
arp = packnet.ARP.Header()

# setting attributes
arp.src.addr = ("255.255.255.255", 0, "ff:ff:ff:ff:ff:ff")
arp.dst.addr = ("255.255.255.255", 0, "ff:ff:ff:ff:ff:ff")
arp.op.integer = 2

# printing encoded packet in bytes
print( arp.packet )

# print debug information
arp.debug()
```


### protocol IPv4

```python
import packnet

# defining `IPv4.Header` object
ipv4 = packnet.IPv4.Header()

# setting attributes
ipv4.src.ip = "192.168.0.1"
ipv4.dst.ip = "192.168.0.2"
ipv4.protocol.integer = 6

# printing encoded packet in bytes
print( ipv4.packet )

# print debug information
ipv4.debug()
```


### protocol IPv6

```python
import packnet

# defining `IPv6.Header` object
ipv6 = packnet.IPv6.Header()

# setting attributes
ipv6.src.ip = "ffff::ffff"
ipv6.dst.ip = "ffff::ffff"
ipv6.protocol.integer = 58

# printing encoded packet in bytes
print( ipv6.packet )

# print debug information
ipv6.debug()
```


### protocol ICMP

```python
import packnet

# defining `ICMP.Echo` object
echo = packnet.ICMP.Echo()
echo.id.integer = 1

# defining `ICMP.Header` object
icmp = packnet.ICMP.Header()

# setting attributes
icmp.type.integer = 8

# printing encoded packet in bytes
print( icmp.packet + echo.packet )

# print debug information
icmp.debug()
echo.debug()
```


### protocol ICMPv6

```python
import packnet

# defining `ICMPv6.Echo` object
echo = packnet.ICMPv6.Echo()
echo.id.integer = 1

# defining `ICMPv6.Header` object
icmpv6 = packnet.ICMPv6.Header()

# setting attributes
icmpv6.type.integer = 8
icmpv6.src.ip = "aaaa::aaaa"  # ip's required for calculating checksum
icmpv6.dst.ip = "bbbb::bbbb"

# printing encoded packet in bytes
print( icmpv6.packet + echo.packet )

# print debug information
icmpv6.debug()
echo.debug()
```


### protocol TCP

```python
import packnet

# defining `TCP.Header` object
tcp = packnet.TCP.Header()   

# setting attributes
tcp.src.ip = "255.255.255.255"  # ip's required for calculating checksum
tcp.dst.ip = "255.255.255.255"
tcp.seq.integer = 3
tcp.ack.integer = 100
tcp.src.port = 1234
tcp.dst.poprt = 4321

# adding options
for _ in range(4):
  tcp.options.append( packnet.TCP.Padding() )

# printing encoded packet in bytes
print( tcp.packet )

# print debug information
tcp.debug()
```


### protocol UDP

```python
import packnet

# defining `UDP.Header` object
udp = packnet.UDP.Header()

# setting attributes
udp.src.ip = "255.255.255.255"  # ip's required for calculating checksum
udp.dst.ip = "255.255.255.255"
udp.src.port = 4321
udp.dst.port = 1234

# adding payload
udp.payload = "hello".encode()

# printing encoded packet in bytes
print( udp.packet )

# print debug information
udp.debug()
```


### protocol DNS

```python
import packnet

# definign `DNS.Query` object
query = packnet.DNS.Query()
query.name.name = "test.com"

# defining `DNS.Header` object
dns = packnet.DNS.Header()

# setting attributes
dns.id.integer = 1234

# adding query to header
dns.question.append( query )

# printing encoded packet in bytes
print( dns.packet )

# print debug information
dns.debug()
```
