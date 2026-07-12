# Networking — Interview Q&A

> Auto-extracted from the notes in [`04-networking/`](../04-networking/) by [`scripts/extract_qa.mjs`](../scripts/extract_qa.mjs).
> Do not edit by hand — regenerate with `node scripts/extract_qa.mjs`.

**91 answered questions** · **15 question prompts without recorded answers**

---

## 1. What is a network address? What is the purpose of each part of a network address?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Network addresses are the addresses used in packets. Each network address has a network port, which identifies a particular data link, and a host or node part, which identifies a specific device on the data link identified by the network part.

---

## 2. What is Routing?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Routing is the process of finding a path to transfer data from source to destination.

---

## 3. What is the advantage of VLAN?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

VLAN facilitates you to create a collision domain by groups other than just physical location while conventional LAN domains are always tied to a physical location.

---

## 4. What are the advantages of LAN switching?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Following are the main advantages of LAN switching:

1. It allows full-duplex data transmission and reception.

2. Media rate adaption.

3. Easy and efficient migration.

---

## 5. What is the difference between private IP and public IP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Public IP is used across the internet while private IP is used within the local LAN.

---

## 6. Explain the terms Unicast, Multicast, and Broadcast.

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Unicast: It specifies one-to-one communication.

Multicast: It specifies one to group communication.

Broadcast: It specifies one to all communication.

Multicast: It specifies one to the nearest communication.

---

## 7. What is the difference between static IP addressing and dynamic IP addressing?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Static IP addresses are reserved and they don’t change over time while dynamic IP addresses can be changed each time you connect to the internet.

Static IP addresses are given manually while dynamic IP addresses are provided by the DHCP server.

---

## 8. What is VLAN?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

VLAN stands for Virtual Local Area Network.

---

## 9. What is the difference between communication and transmission?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Communication is a process of sending and receiving data by an externally connected data cable whereas transmission is a process of sending data from source to destination.

---

## 10. What is the 2nd layer of the OSI layer model?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The data link layer is the second layer of the OSI model.

---

## 11. What is the main difference between full and half-duplex?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

In full-duplex, communication occurs from both sides, while in half-duplex communication occurs in one direction.

---

## 12. At which layer of OSI does frame relay technology work?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Frame relay work at the Data link layer OSI model

---

## 13. What is the passive topology in CCNA?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

When the topology enables the computers on the network only to simply listen and receive the signals, it is known as passive topology because they don’t amplify the signals anyway.

---

## 14. Can you assign IP on layer 2?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

No, you cannot assign IP addresses on layer 2.

---

## 15. What are the possible ways of data transmission in CCNA?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

These are the three possible ways of data transmission:

- Simplex
- Half-duplex
- Full-duplex

---

## 16. What is OSPF stand for?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Open Shortest Path First

---

## 17. What is the difference between RIP and IGRP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

RIP depends on the number of hops to determine the best route to the network while, IGRP considers many factors before deciding the best route to take i.e. bandwidth, reliability, MTU and hops count.

---

## 18. What is BootP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

BootP is a short form of the Boot Program. It is a protocol that is used to boot diskless workstations connected to the network. BootP is also used by diskless workstations to determine its own IP address and also the IP addresses of server PC.

---

## 19. What is Latency?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Latency is the amount of time delay. It is measured as the time difference between the point of time when a network receives the data and the time it is sent by another network.

---

## 20. What is PoE?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

PoE is said to be Power over Ethernet. It is used to pass an electric signal with data at a time.

---

## 21. What is the MAC address?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

MAC address stands for Media Access Control address. This is an address of a device that is identified as the Media Access Control Layer in the network architecture. The MAC address is unique and usually stored in ROM.

---

## 22. Can you use two different subnet IP’s on a WAN link?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Yes.

---

## 23. What is the difference between ARP and RARP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

ARP stands for Address Resolution Protocol. ARP is a protocol that is used to map an IP address to a physical machine address.

RAPR stands for Reverse Address Resolution Protocol. RARP is a protocol that is used to map a MAC address to an IP address.

---

## 24. What is the stub area?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

A stub area is an area that does not accept routing updates from outside its autonomous system.

---

## 25. What are the three sources of signal degradation on a data link?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The three sources of signal degradation on a data link are attenuation, interference, and distortion. Attenuation is a function of the resistance of the medium. Interference is a function of noise entering the medium. Distortion is a function of the reactive characteristics of the medium, which react differently to different frequency components of the signal.

---

## 26. What is Ping? What is the usage of Ping?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

PING stands for Packet Internet Groper. It is a computer network tool that is used to test whether a particular host is reachable across an IP address or not.

---

## 27. What are the different types of passwords used in securing a Cisco router?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

There are five types of passwords that can be set on a Cisco router:

- Consol
- Aux
- VTY
- Enable Password
- Enable Secret

---

## 28. Is HSRP is cisco proprietary or introduced by IEEE?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

HSRP is Cisco’s proprietary

---

## 29. What is the maximum value of administrative you can use?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

255

---

## 30. What does AAA stand for?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Authentication, authorization, and accounting

---

## 31. Which feature should a routing protocol have to support VLSM?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

It should include the subnet mask of each destination address.

---

## 32. What is Topology in CCNA?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Topology is an arrangement of various elements (links, nodes, etc.) of a computer network in a specific order. These are the different types of topology used in CCNA:

**Bus:**

- Bus topology is a network topology in which all the nodes are connected to a single cable known as a central cable or bus.
- It acts as a shared communication medium, i.e., if any device wants to send the data to other devices, then it will send the data over the bus which in turn sends the data to all the attached devices.
- Bus topology is useful for a small number of devices. As if the bus is damaged then the whole network fails.

**Star:**

- Star topology is a network topology in which all the nodes are connected to a single device known as a central device.
- Star topology requires more cable compared to other topologies. Therefore, it is more robust as a failure in one cable will only disconnect a specific computer connected to this cable.
- If the central device is damaged, then the whole network fails.
- Star topology is very easy to install, manage and troubleshoot.
- Star topology is commonly used in office and home networks.

**Ring:**

- Ring topology is a network topology in which nodes are exactly connected to two or more nodes and thus, forming a single continuous path for the transmission.
- It does not need any central server to control the connectivity among the nodes.
- If the single node is damaged, then the whole network fails.
- Ring topology is very rarely used as it is expensive, difficult to install and manage.
- Examples of Ring topology are SONET network, SDH network, etc.

**Mesh:**

- Mesh topology is a network topology in which all the nodes are individually connected to other nodes.
- It does not need any central switch or hub to control the connectivity among the nodes.
- Mesh topology is categorized into two parts:
- **Fully connected mesh topology**: In this topology, all the nodes are connected to each other.
- **Partially connected mesh topology**: In this topology, all the nodes are not connected to each other.
- It is a robust as a failure in one cable will only disconnect the specified computer connected to this cable.
- Mesh topology is rarely used as installation and configuration are difficult when connectivity gets more.
- Cabling cost is high as it requires bulk wiring.

**Tree:**

- Tree topology is a combination of star and bus topology. It is also known as the expanded star topology.
- In tree topology, all the star networks are connected to a single bus.
- Ethernet protocol is used in this topology.
- In this, the whole network is divided into segments known as star networks which can be easily maintained. If one segment is damaged, but there is no effect on other segments.
- Tree topology depends on the “main bus,” and if it breaks, then the whole network gets damaged.

**Hybrid:**

- A hybrid topology is a combination of different topologies to form a resulting topology.
- If star topology is connected with another star topology, then it remains star topology. If star topology is connected with different topology, then it becomes a Hybrid topology.
- It provides flexibility as it can be implemented in a different network environment.
- The weakness of a topology is ignored, and only strength will be taken into consideration.

---

## 33. What are the possible ways of data transmission ?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Simplex, half-duplex and full-duplex are the communication channels used to convey the information. Either the communication channel can be a physical medium or logical medium.

These are the three possible ways of data transmission:

**Simplex**

- The simplex communication channel sends the data only in one direction.
- Example of the simplex communication channel is a radio station. The radio station transmits the signal while the other receives the signal.
- In simplex mode, entire bandwidth can be utilized for the data transmission as a flow of data is in one direction.

**Half-duplex**

- The half-duplex communication channel sends the information in both the directions but not at the same time.
- Performance of half-duplex is better than the simplex communication channel as the data flows in both the directions.
- Example of the half-duplex communication channel is “walkie-talkie”. In “walkie-talkie”, both the transmitter and receiver can communicate with each other on the same channel.
- In half-duplex mode, entire bandwidth can be used by the transmitter when the message is sent over the communication channel.

**Full-duplex**

- The full-duplex communication channel can send the information in both the directions at the same time.
- Performance of full-duplex is better than the half-duplex communication channel as the data flows in both the direction at the same time.
- Example of a full-duplex communication channel is “telephone”. In the case of telephone, one can speak and hear at the same time. Therefore, this channel increases the efficiency of communication.

---

## 34. What are the different memories used in a CISCO router?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Three types of memories are used in a CISCO router:

- **NVRAM**
- NVRAM stands for Non-volatile random access memory.
- It is used to store the startup configuration file.
- NVRAM retains the configuration file even if the router shut down.
- **DRAM**
- DRAM stands for dynamic random access memory.
- It stores the configuration file that is being executed.
- DRAM is used by the processor to access the data directly rather than accessing it from scratch.
- DRAM is located near the processor that provides the faster access to the data than the storage media such as hard disk.
- Simple design, low cost, and high speed are the main features of DRAM memory.
- DRAM is a volatile memory.
- **Flash Memory**
- It is used to store the system IOS.
- Flash memory is used to store the ios images.
- Flash memory is erasable and reprogrammable ROM.
- The capacity of the flash memory is large enough to accommodate many different IOS versions.

---

## 35. What are the different types of the password used in securing a Cisco router?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

There are five types of passwords can be set on a Cisco router:

- Consol
- Aux
- VTY
- Enable Password
- Enable Secret

---

## 36. What are the different modes in a router?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

There are basically 3 different modes in a router which are:

1. **User Mode**:

The user-mode only allows us to do basic monitoring. Only limited show commands work in this mode and it is denoted by the “>” sign.

For ex: Enable, ping, traceroute, etc. Router>

1. **Privilege Mode**:

Only monitoring, verification, and troubleshooting commands work in this mode. It is denoted by “#”.

For ex: show, configure terminal, write, etc. Router#

1. **Global Configuration Mode**:

This mode affects the operations of the device. It is generally used to view all the configurations of the device and it is often used to perform high-level tasks on devices. It is denoted by “(config)#”.

For ex: Hostname, etc. Router(config)#

---

## 37. Q3 — What is the OSI Reference Model and what are its different layers?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

OSI stands for Open System Interconnect. The OSI Reference model explains how information and data communication occurs over a network, and it was developed by International Organization for standardization (ISO) in 1984.

It consists of 7 Layers which are:

**Application Layer:**

It’s responsible for providing an interface for users to interact with application services or network services.

**Presentation Layer:**

It’s responsible for defining a standard format for the data. Encoding and Decoding is the major function that takes place at this layer.

**Session Layer:**

This layer is responsible for establishing, maintaining, and terminating the sessions. The Session ID is used to identify a session or interaction.

**Transport Layer:**

It provides a data delivery mechanism between applications in the network. The Transport layer is the major function layer in the OSI model. It performs:

- Identifying service
- Multiplexing & De-multiplexing Segmentation
- Error correction
- flow control
- Transport layer protocols

The protocols which take care of data transport at the transport layer are TCP/UDP.

**Network Layer:**

It provides logical addressing path determination (routing). The protocols that work in this layer are: -Routed Protocol, Routing Protocol.

**Data Link Layer:**

It provides communication with the network layer. Mac (media access control) it provides reliable data transit across a physical link.

**Physical Layer:**

It defines the electrical and mechanical functional specification for communication between the network devices.

---

## 38. What are Broadcast Domain and Collision Domain?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

**Broadcast Domain** — Broadcast is a type of communication where the sending device sends a single copy of data. That copy of data gets delivered to every other device in the network segment.

**Collision Domain** — It is a network scenario where one device sends a packet on a network segment forcing every other device on that same segment to pay attention to it. At the same time, if a different device in that same segment to pay attention to it.

---

## 39. What is ARP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

ARP stands for [Address Resolution Protocol](https://www.pynetlabs.com/what-is-arp/). It is a network protocol used to map a network layer protocol address (IP address) to a data link layer hardware address (MAC address). ARP resolves the IP address to the corresponding MAC address.

---

## 40. What is the MAC Format?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

It is a 12 Digits 48 Bit(6byte) Hardware address written in Hexadecimal format. It consists of two parts: –

- IEEE assigns the first 24 Bits of OUI (Organizationally Unique Identifier).
- The last 24 Bits are Manufacturing-assigned Code

---

## 41. Can you explain what a VLAN is and its purpose?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

A VLAN (Virtual Local Area Network) is a logical grouping of devices within a single Ethernet network segment. It helps reduce the number of broadcast domains and network subnets, allowing multiple networks to share the same physical infrastructure without interference.

---

## 42. What is a trunk port, and why is it important in networking?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

A trunk port is configured to handle traffic from multiple VLANs by encapsulating the traffic with VLAN tags. This allows the simultaneous transmission of multiple VLANs over a single link between switches or network devices, optimizing the use of network resources.

PC-A and PC-C are members of VLAN-10. PC-B and PC-D are members of VLAN-20. S1 and S2 have a trunk connection.

---

## 43. How does the ARP (Address Resolution Protocol) work, and why is it necessary?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

ARP is used to map an IPv4 address to a MAC address (Media Access Control hardware address that uniquely identifies each device on a network). It helps devices on a local network discover each other’s hardware addresses, which is essential for communication within the same network segment.

For example, for Apple Mac users, if you run `ifconfig en0` , the **Ethernet Address (MAC Address)** is shown: `ether bc:d0:74:0a:d6:6f`. This is the MAC address of the `en0` interface, which is a unique identifier for the network interface card.

The inet `inet 10.100.102.130` is the IPv4 address assigned to the interface. Now, when printing the ARP Table using `arp -a` you’ll see the mapping between the MAC Address and IPv4 address.

---

## 44. Can you describe the OSI model and its layers?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The OSI (Open Systems Interconnection) model is a seven-layer framework that standardizes the functions of a network into layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application. Each layer has specific roles and responsibilities in the communication process.

From [https://en.wikipedia.org/wiki/OSI_model](https://en.wikipedia.org/wiki/OSI_model)

- **Which layer is the Application Layer, and what is its function?** The Application Layer is the topmost layer, providing network services directly to applications. It handles protocols and data that applications use to communicate over the network.
- **Which layers are considered the hardware or network support layers?** The Data Link Layer and Physical Layer are considered hardware or network support layers. They deal with the physical transmission of data and error detection/correction.

From [https://x.com/AccordionGuy/status/1496502151983792138](https://x.com/AccordionGuy/status/1496502151983792138)

---

## 45. What are some key differences between the OSI model and the TCP/IP model?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The TCP/IP model consists of four layers: Link, Internet, Transport, and Application. It differs from the OSI model in terms of layer functions and the number of layers but serves as the foundation for most modern networks.

From [https://www.educba.com/osi-model-vs-tcp-ip-model/](https://www.educba.com/osi-model-vs-tcp-ip-model/)

---

## 46. What is BGP, and how does it function in network routing?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

BGP (Border Gateway Protocol) is an inter-domain routing protocol used to exchange routing information between different autonomous systems (ASes) on the internet. It helps manage how data is routed across the internet.

**Example of How BGP Is Involved- Example with ‘traceroute app.lightrun.com’**

**Initial Hops** (1–6) — low latency, within my local network or my ISP network — 013 Netvision (Cellcom); **Intermediate Hops** (7–10) — higher latency, major global ISP in Cognet Communications, traveling through Cognet’s Infrastructure; **Final Hops** (from 12) — AWS Infrastructure. BGP was responsible to route the traffic between the different AS.

1. **From Your Network (ISP)**: Your ISP’s network (which is part of an AS) sends packets to a neighboring AS, which might be a larger backbone provider like Cogent.
2. **Cogent Communications**: Cogent receives the packets and uses BGP to determine the best route to the destination network.
3. **AWS Network**: Finally, the packets reach AWS’s network. AWS’s own internal routing, potentially influenced by BGP routes from different providers, directs the packets to the specific AWS service (like `app.lightrun.com`).

---

## 47. What kind of protocol is OSPF, and how does it differ from BGP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

OSPF (Open Shortest Path First) is a link-state routing protocol used within a single autonomous system. It uses Dijkstra’s algorithm to calculate the shortest path and is different from BGP in its scope and functionality.

---

## 48. How does BGP select the best path for routing?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

BGP uses various attributes, such as **AS path**, **next hop**, **local preference**, **MED** (Multi-Exit Discriminator), **Weight** (prefer the path with the highest weight. This is a value that is local to the router, and it’s Cisco proprietary. The default value is 0 for all routes not originated by the local router), to select the best path. It evaluates these attributes to determine the most efficient route for data:

From [https://networklessons.com/bgp/bgp-attributes-and-path-selection](https://networklessons.com/bgp/bgp-attributes-and-path-selection)

---

## 49. What is MPLS, and how does it enhance network performance?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

MPLS (Multi-protocol Label Switching) uses labels to make forwarding decisions, improving network efficiency and performance. The MPLS header is typically 32 bits long. It is used to manage traffic engineering and provide quality of service (QoS).

**Example: MPLS Label Assignment Process**

1. **Label Assignment: Router A** receives an IP packet and assigns an MPLS label to it. For example, Router A assigns the label `1001`.
2. **Label Forwarding:**
- **Router A** forwards the packet with the MPLS label `1001` to **Router B**.
- **Router B** receives the packet, looks up the MPLS label `1001`, and forwards the packet to **Router C** based on its label forwarding table.

3. **Label Removal: Router C** finally removes the MPLS label and forwards the original IP packet to its destination.

---

## 50. Can you explain subnetting and its importance in IP addressing?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Subnetting is a method used in IP networking to divide a larger network into smaller, more manageable sub-networks or subnets. Each subnet operates as a distinct network with its own range of IP addresses. This organization enhances network efficiency, security, and management.

**Importance of Subnetting:**

1. **Efficient IP Address Management:** By dividing a large network into smaller subnets, IP addresses can be used more efficiently. This helps in avoiding the wastage of IP addresses and ensures that each subnet gets an appropriate number of addresses based on its needs.
2. **Improved Network Performance:** Subnetting helps in reducing broadcast traffic by limiting the broadcast domain to a smaller subnet. This results in improved network performance and reduced network congestion.
3. **Enhanced Security:** Subnets can be used to isolate different segments of a network, improving security by controlling the flow of traffic between them. For instance, sensitive systems can be placed in separate subnets with strict access controls.
4. **Simplified Network Management:** Network management becomes easier when dealing with smaller subnets. It allows for better organization of network resources and more straightforward network troubleshooting and monitoring.

Created with [https://cidr-subnet.netlify.app/](https://cidr-subnet.netlify.app/)

The suffix /24 means that 2^(32–24)=256 addresses are available to use:

- **10.0.1.0** represents the subnet itself and cannot be assigned to individual device.
- First 254 addresses are available host addresses: **10.0.1.1–10.0.1.254.**
- **10.0.1.255 is** the 255th (last, counting from 0) address which is allocated for the **broadcast address** — The broadcast address is a special IP address used to send data packets to all devices on a network or subnet simultaneously. It allows a single message to be delivered to every device within the same network segment without needing to send individual packets to each device.

**Network Address + Usable Addresses + Broadcast Address:** 1 (Network) + 254 (Usable) + 1 (Broadcast) = 256

---

## 51. What are the key processes involved in DHCP?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

DHCP (Dynamic Host Configuration Protocol) automates IP address assignment and configuration. Key processes include discovery, offer, request, and acknowledgment.

---

## 52. What tools and approaches do you use for network troubleshooting?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Effective network troubleshooting involves using tools like traceroute, ping, and network analyzers. The approach includes isolating issues, identifying causes, and resolving problems systematically.

---

## 53. What is QoS (Quality of Service) in a network?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

QoS involves managing network traffic to ensure performance for high-priority applications. Techniques include:

- **Traffic Shaping:** Controls the rate of outbound traffic to smooth out bursts and maintain a steady flow.
- **Queuing:** Manages packets in different queues based on priority or traffic type, ensuring orderly processing.
- **Prioritization:** Assigns different priority levels to various types of traffic, ensuring that higher-priority traffic is processed first.

---

## 54. What technologies would you use to connect two remote offices, and what is inter-networking?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Technologies for connecting remote offices include VPN (Virtual Private Network): A VPN creates a secure, encrypted connection over the internet between remote offices. It allows remote sites to communicate as if they were on the same local network. Inter-networking refers to connecting multiple networks to allow them to function as a cohesive whole.

---

## 55. What happens when you register a new domain tal.com in AWS Route53?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

1. **Registering tal.com —** You register **tal.com** through AWS Route 53, you provide registration details and pay the registration fee.
2. **Updating WHOIS:** AWS Route 53 updates the WHOIS database with your registration information.

Example — Taken from the website who.is; showing Whois information like Registrar Info, Important Dates, Name Servers, Similar Domains, etc. WHOIS Database is owned by the ICANN — Internet Corportation for Assigned Names and Numbers — [https://www.icann.org/](https://www.icann.org/)

3. **Configuring Nameservers:** You specify AWS nameservers for **tal.com,** AWS Route 53 updates the domain registry with these nameservers.

4. **Propagation Process:** The domain registry notifies the root DNS servers about **tal.com** and its nameservers.

- Root servers update their records, followed by Top-level Domain servers (e.g., .com).
- Recursive resolvers around the world gradually receive and cache the updated DNS records.

DNS Hierarchical composed of Root DNS Servers, TLD Servers, etc…

**5. Domain Resolution:**

- Once propagation is complete (can take up to 48 hours), lightrun.com is resolvable globally.
- DNS queries for lightrun.com are directed to AWS Route 53 nameservers, which respond with the appropriate DNS records.

---

## 56. Explain the difference between a Name Server and a DNS Server.

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Let’s use the following example — Scenario: Resolving the Domain “lightrun.com”.

1. **User Query:** A user types “lightrun.com” into their browser.
2. **Recursive Resolver (DNS Server):** The user’s device sends a query to a recursive resolver (a DNS server) provided by their ISP or a public DNS service like Google Public DNS (8.8.8.8) or Cloudflare DNS (1.1.1.1).
3. **Root DNS Server:** The recursive resolver queries a root DNS server. The root DNS server doesn’t know the IP address of “lightrun.com” but knows which TLD DNS server to ask. It directs the resolver to the .com TLD DNS server.
4. **TLD DNS Server:** The recursive resolver then queries the .com TLD DNS server. The TLD server also doesn’t have the exact IP address but knows the authoritative nameservers for “lightrun.com.” It responds with the nameservers responsible for “lightrun.com”, such as [ainsley.ns.cloudflare.com](https://who.is/nameserver/ainsley.ns.cloudflare.com) and [art.ns.cloudflare.com](https://who.is/nameserver/art.ns.cloudflare.com).
5. **Authoritative Nameservers:** Finally, the recursive resolver queries one of the authoritative nameservers for “lightrun.com”. These nameservers are specifically designated to hold the DNS records for the domain “lightrun.com”. The authoritative nameserver responds with the IP address associated with “lightrun.com”.
6. **Response to User:** The recursive resolver sends the IP address back to the user’s device, which can now connect to the web server hosting “lightrun.com” using that IP address.

---

## 57. What is an IPv4 address? What are the different classes of IPv4?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

An IP address is a 32-bit dynamic address of a node in the network. An IPv4 address has 4 octets of 8-bit each with each number with a value up to 255.

IPv4 classes are differentiated based on the number of hosts it supports on the network. There are five types of IPv4 classes and are based on the first octet of IP addresses which are classified as Class A, B, C, D, or E.

| IPv4 Class | IPv4 Start Address | IPv4 End Address | Usage |
| --- | --- | --- | --- |
| A | 0.0.0.0 | 127.255.255.255 | Used for Large Network |
| B | 128.0.0.0 | 191.255.255.255 | Used for Medium Size Network |
| C | 192.0.0.0 | 223.255.255.255 | Used for Local Area Network |
| D | 224.0.0.0 | 239.255.255.255 | Reserved for Multicasting |
| E | 240.0.0.0 | 255.255.255.254 | Study and R&D |

Also, check out Scaler topics' Free [Computer Networks](https://www.scaler.com/topics/course/free-computer-networks-course/) course with certification to learn the fundamentals of computer networking.

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/desktop/study_plan-fb58ec94dd27940f470d62dee6d85c8161f6afc2b9dcbced18278212ce50b8b9.svg.gz)

**Create a free personalised study plan**

Get into your dream companies with expert guidance

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/code-99b8ddab28469d3e18187c7e7f62dcf921ece612e63043b7515547d441ea3ebb.svg.gz)

Real-Life Problems

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/suitcase-7129128344fb59d27c28914ce39a52b40df37b3da954c23330359726019a8fb7.svg.gz)

Prep for Target Roles

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/pencil-aaf6423aa93927b3965ae3006bc88653f14fee9586297e82fa1153ab475c8459.svg.gz)

Custom Plan Duration

[**Create My Plan**](https://www.interviewbit.com/interview-preparation-kit/)

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/arrow-right-54a813c1b9b6df712c72a314c89081e5a96674ee7ee6454dd7c063d0fe79bb1c.svg.gz)

---

## 58. Explain different types of networks.

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Below are few types of networks:

| Type | Description |
| --- | --- |
| PAN (Personal Area Network) | Let devices connect and communicate over the range of a person. E.g. connecting Bluetooth devices. |
| LAN (Local Area Network) | It is a privately owned network that operates within and nearby a single building like a home, office, or factory |
| MAN (Metropolitan Area Network) | It connects and covers the whole city. E.g. TV Cable connection over the city |
| WAN (Wide Area Network) | It spans a large geographical area, often a country or continent. The Internet is the largest WAN |
| GAN (Global Area Network) | It is also known as the Internet which connects the globe using satellites. The Internet is also called the Network of WANs. |

---

## 59. Explain LAN (Local Area Network)

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

LANs are widely used to connect computers/laptops and consumer electronics which enables them to share resources (e.g., printers, fax machines) and exchange information. When LANs are used by companies or organizations, they are called **enterprise networks**. There are two different types of LAN networks i.e. wireless LAN (no wires involved achieved using Wi-Fi) and wired LAN (achieved using LAN cable). Wireless LANs are very popular these days for places where installing wire is difficult. The below diagrams explain both wireless and wired LAN.

LAN (Local Area Network)

**You can download a PDF version of Networking Interview Questions.Download PDF**

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/download_v2-f7bcad529b2845c93dddc78cd31acf9ecb098c42854a1757f0f8949950377c02.svg.gz)

---

## 60. Tell me something about VPN (Virtual Private Network)

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

VPN or the Virtual Private Network is a private WAN (Wide Area Network) built on the internet. It allows the creation of a secured tunnel (protected network) between different networks using the internet (public network). By using the VPN, a client can connect to the organization’s network remotely. The below diagram shows an organizational WAN network over Australia created using VPN:

VPN (Virtual Private Network)

---

## 61. What are the advantages of using a VPN?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Below are few advantages of using VPN:

- VPN is used to connect offices in different geographical locations remotely and is cheaper when compared to WAN connections.
- VPN is used for secure transactions and confidential data transfer between multiple offices located in different geographical locations.
- VPN keeps an organization’s information secured against any potential threats or intrusions by using virtualization.
- VPN encrypts the internet traffic and disguises the online identity.

---

## 62. What are the different types of VPN?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Few types of VPN are:

- **Access VPN:** Access VPN is used to provide connectivity to remote mobile users and telecommuters. It serves as an alternative to dial-up connections or ISDN (Integrated Services Digital Network) connections. It is a low-cost solution and provides a wide range of connectivity.
- **Site-to-Site VPN:** A Site-to-Site or Router-to-Router VPN is commonly used in large companies having branches in different locations to connect the network of one office to another in different locations. There are 2 sub-categories as mentioned below:
- **Intranet VPN:** Intranet VPN is useful for connecting remote offices in different geographical locations using shared infrastructure (internet connectivity and servers) with the same accessibility policies as a private WAN (wide area network).
- **Extranet VPN:** Extranet VPN uses shared infrastructure over an intranet, suppliers, customers, partners, and other entities and connects them using dedicated connections.

---

## 63. What are nodes and links?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

**Node:** Any communicating device in a network is called a Node. Node is the point of intersection in a network. It can send/receive data and information within a network. Examples of the node can be computers, laptops, printers, servers, modems, etc.

**Link:** A link or edge refers to the connectivity between two nodes in the network. It includes the type of connectivity (wired or wireless) between the nodes and protocols used for one node to be able to communicate with the other.

Nodes and Links

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/desktop/moco-c7ebe9f8f47748ffae9ae0533cc6e71697ba1e8bb0df4c7c4f481b44b74c5d91.svg.gz)

Advance your career with  **Mock Assessments**

Real-world coding challenges for top company interviews

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/code-99b8ddab28469d3e18187c7e7f62dcf921ece612e63043b7515547d441ea3ebb.svg.gz)

Real-Life Problems

[](https://assets.interviewbit.com/assets/ibpp/interview_guides/assets/layout-alt-39a6b2a56b986dbae952a4e1a7fde9324f0bafeb365b03e4ecb507ff876531e0.svg.gz)

Detailed reports

**Attempt Now**

---

## 64. What is the network topology?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Network topology is a physical layout of the network, connecting the different nodes using the links. It depicts the connectivity between the computers, devices, cables, etc.

---

## 65. Define different types of network topology

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The different types of network topology are given below:

**Bus Topology:**

Bus Topology

- All the nodes are connected using the central link known as the bus.
- It is useful to connect a smaller number of devices.
- If the main cable gets damaged, it will damage the whole network.

**Star Topology:**

Star Topology

- All the nodes are connected to one single node known as the central node.
- It is more robust.
- If the central node fails the complete network is damaged.
- Easy to troubleshoot.
- Mainly used in home and office networks.

**Ring Topology:**

Ring Topology

- Each node is connected to exactly two nodes forming a ring structure
- If one of the nodes are damaged, it will damage the whole network
- It is used very rarely as it is expensive and hard to install and manage

**Mesh Topology:**

Mesh Topology

- Each node is connected to one or many nodes.
- It is robust as failure in one link only disconnects that node.
- It is rarely used and installation and management are difficult.

**Tree Topology:**

Tree Topology

- A combination of star and bus topology also know as an extended bus topology.
- All the smaller star networks are connected to a single bus.
- If the main bus fails, the whole network is damaged.

**Hybrid:**

- It is a combination of different topologies to form a new topology.
- It helps to ignore the drawback of a particular topology and helps to pick the strengths from other.

---

## 66. How are Network types classified?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Network types can be classified and divided based on the area of distribution of the network. The below diagram would help to understand the same:

Network Types

---

## 67. What are Private and Special IP addresses?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

**Private Address:** For each class, there are specific IPs that are reserved specifically for private use only. This IP address cannot be used for devices on the Internet as they are non-routable.

| IPv4 Class | Private IPv4 Start Address | Private IPv4 End Address |
| --- | --- | --- |
| A | 10.0.0.0 | 10.255.255.255 |
| B | 172.16.0.0 | 172.31.255.255 |
| C | 192.168.0.0 | 192.168.255.255 |

**Special Address:** IP Range from 127.0.0.1 to 127.255.255.255 are network testing addresses also known as loopback addresses are the special IP address.

---

## 68. What is the DNS?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

DNS is the Domain Name System. It is considered as the devices/services directory of the Internet. It is a decentralized and hierarchical naming system for devices/services connected to the Internet. It translates the domain names to their corresponding IPs. For e.g. interviewbit.com to 172.217.166.36. It uses port 53 by default.

Get Access to 250+ Guides with Scaler Mobile App!

Experience free learning content on the Scaler Mobile App

4.5

100K+

Play Store

---

## 69. What is the use of a router and how is it different from a gateway?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The router is a networking device used for connecting two or more network segments. It directs the traffic in the network. It transfers information and data like web pages, emails, images, videos, etc. from source to destination in the form of packets. It operates at the network layer. The gateways are also used to route and regulate the network traffic but, they can also send data between two dissimilar networks while a router can only send data to similar networks.

---

## 70. What is the SMTP protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

SMTP is the Simple Mail Transfer Protocol. SMTP sets the rule for communication between servers. This set of rules helps the software to transmit emails over the internet. It supports both End-to-End and Store-and-Forward methods. It is in always-listening mode on port 25.

SMTP Protocol

---

## 71. Describe the OSI Reference Model

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Open System Interconnections (OSI) is a network architecture model based on the ISO standards. It is called the OSI model as it deals with connecting the systems that are open for communication with other systems.

The OSI model has seven layers. The principles used to arrive at the seven layers can be summarized  briefly as below:

- Create a new layer if a different abstraction is needed.
- Each layer should have a well-defined function.
- The function of each layer is chosen based on internationally standardized protocols.

---

## 72. Define the 7 different layers of the OSI Reference Model

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Here the 7 layers of the OSI reference model:

Layers of OSI Model

| Layer | Unit Exchanged | Description |
| --- | --- | --- |
| Physical | Bit | • It is concerned with transmitting raw bits over a communication channel.
• Chooses which type of transmission mode is to be selected for the transmission. The available transmission modes are Simplex, Half Duplex and Full Duplex., |
| Data Link | Frame | • The main task of this layer is to transform a raw transmission facility into a line that appears free of undetected transmission errors.
• It also allows detecting damaged packets using the CRC (Cyclic Redundancy Check) error-detecting, code.
• When more than one node is connected to a shared link, Data Link Layer protocols are required to determine which device has control over the link at a given time.
• It is implemented by protocols like CSMA/CD, CSMA/CA, ALOHA, and Token Passing. |
| Network | Packet | • It controls the operation of the subnet.
• The network layer takes care of feedback messaging through ICMP messages. |
| Transport | TPDU - Transaction Protocol Data Unit | • The basic functionality of this layer is to accept data from the above layers, split it up into smaller units if needed, pass these to the network layer, and ensure that all the pieces arrive correctly at the other end.
• The Transport Layer takes care of Segmentation and Reassembly. |
| Session | SPDU - Session Protocol Data Unit | • The session layer allows users on different machines to establish sessions between them.
• Dialogue control is using the full-duplex link as half-duplex. It sends out dummy packets from the client to the server when the client is ideal. |
| Presentation | PPDU - Presentation Protocol Data Unit | • The presentation layer is concerned with the syntax and semantics of the information transmitted.
• It translates a message from a common form to the encoded format which will be understood by the receiver. |
| Application | APDU - Application Protocol Data Unit | • It contains a variety of protocols that are commonly needed by users.
• The application layer sends data of any size to the transport layer. |

---

## 73. Describe the TCP/IP Reference Model

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

It is a compressed version of the OSI model with only 4 layers. It was developed by the US Department of Defence (DoD) in the 1980s. The name of this model is based on 2 standard protocols used i.e. TCP (Transmission Control Protocol) and IP (Internet Protocol).

---

## 74. Define the 4 different layers of the TCP/IP Reference Model

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Layers of TCP/IPLayerDescriptionLinkDecides which links such as serial lines or classic Ethernet must be used to meet the needs of the connectionless internet layer.Internet
• The internet layer is the most important layer which holds the whole architecture together.
• It delivers the IP packets where they are supposed to be delivered.TransportIts functionality is almost the same as the OSI transport layer. It enables peer entities on the network to carry on a conversation.ApplicationIt contains all the higher-level protocols.

- • The internet layer is the most important layer which holds the whole architecture together.
- • It delivers the IP packets where they are supposed to be delivered.

---

## 75. Differentiate OSI Reference Model with TCP/IP Reference Model

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

OSI Vs TCP/IPOSI Reference ModelTCP/IP Reference Model7 layered architecture4 layered architectureFixed boundaries and functionality for each layerFlexible architecture with no strict boundaries between layersLow ReliabilityHigh ReliabilityVertical Layer ApproachHorizontal Layer Approach

---

## 76. What are the HTTP and the HTTPS protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

HTTP is the HyperText Transfer Protocol which defines the set of rules and standards on how the information can be transmitted on the World Wide Web (WWW).  It helps the web browsers and web servers for communication. It is a ‘stateless protocol’ where each command is independent with respect to the previous command. HTTP is an application layer protocol built upon the TCP. It uses port 80 by default.

HTTPS is the HyperText Transfer Protocol Secure or Secure HTTP. It is an advanced and secured version of HTTP. On top of HTTP, SSL/TLS protocol is used to provide security. It enables secure transactions by encrypting the communication and also helps identify network servers securely. It uses port 443 by default.

---

## 77. What is the FTP protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

FTP is a File Transfer Protocol. It is an application layer protocol used to transfer files and data reliably and efficiently between hosts. It can also be used to download files from remote servers to your computer. It uses port 27 by default.

---

## 78. What is the TCP protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

TCP or TCP/IP is the Transmission Control Protocol/Internet Protocol. It is a set of rules that decides how a computer connects to the Internet and how to transmit the data over the network. It creates a virtual network when more than one computer is connected to the network and uses the three ways handshake model to establish the connection which makes it more reliable.

---

## 79. What is the UDP protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

UDP is the User Datagram Protocol and is based on Datagrams. Mainly, it is used for multicasting and broadcasting. Its functionality is almost the same as TCP/IP Protocol except for the three ways of handshaking and error checking. It uses a simple transmission without any hand-shaking which makes it less reliable.

---

## 80. Compare between TCP and UDP

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

TCP/IPUDPConnection-Oriented ProtocolConnectionless ProtocolMore ReliableLess ReliableSlower TransmissionFaster TransmissionPackets order can be preserved or can be rearrangedPackets order is not fixed and packets are independent of each otherUses three ways handshake model for connectionNo handshake for establishing the connectionTCP packets are heavy-weightUDP packets are light-weightOffers error checking mechanismNo error checking mechanismProtocols like HTTP, FTP, Telnet, SMTP, HTTPS, etc use TCP at the transport layerProtocols like DNS, RIP, SNMP, RTP, BOOTP, TFTP, NIP, etc use UDP at the transport layerTCP VS UDP

---

## 81. What is the ICMP protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

ICMP is the Internet Control Message Protocol. It is a network layer protocol used for error handling. It is mainly used by network devices like routers for diagnosing the network connection issues and crucial for error reporting and testing if the data is reaching the preferred destination in time. It uses port 7 by default.

---

## 82. What do you mean by the DHCP Protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

DHCP is the Dynamic Host Configuration Protocol.

It is an application layer protocol used to auto-configure devices on IP networks enabling them to use the TCP and UDP-based protocols. The DHCP servers auto-assign the IPs and other network configurations to the devices individually which enables them to communicate over the IP network. It helps to get the subnet mask, IP address and helps to resolve the DNS. It uses port 67 by default.

---

## 83. What is the ARP protocol?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

ARP is Address Resolution Protocol. It is a network-level protocol used to convert the logical address i.e. IP address to the device's physical address i.e. MAC address. It can also be used to get the MAC address of devices when they are trying to communicate over the local network.

ARP Protocol

---

## 84. What is the MAC address and how is it related to NIC?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

MAC address is the Media Access Control address. It is a 48-bit or 64-bit unique identifier of devices in the network. It is also called the physical address embedded with Network Interface Card (NIC) used at the Data Link Layer. NIC is a hardware component in the networking device using which a device can connect to the network.

---

## 85. Differentiate the MAC address with the IP address

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The difference between MAC address and IP address are as follows:

| MAC Address | IP Address |
| --- | --- |
| Media Access Control Address | Internet Protocol Address |
| 6 or 8-byte hexadecimal number | 4 (IPv4) or 16 (IPv6) Byte address |
| It is embedded with NIC | It is obtained from the network |
| Physical Address | Logical Address |
| Operates at Data Link Layer | Operates at Network Layer. |
| Helps to identify the device | Helps to identify the device connectivity on the network. |

---

## 86. What is a subnet?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

A subnet is a network inside a network achieved by the process called subnetting which helps divide a network into subnets. It is used for getting a higher routing efficiency and enhances the security of the network. It reduces the time to extract the host address from the routing table.

Subnet

---

## 87. Compare the hub vs switch

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

HubSwitchOperates at Physical LayerOperates at Data Link LayerHalf-Duplex transmission modeFull-Duplex transmission modeEthernet devices can be connectedsendLAN devices can be connectedLess complex, less intelligent, and cheaperIntelligent and effectiveNo software support for the administrationAdministration software support is presentLess speed up to 100 MBPSSupports high speed in GBPSLess efficient as there is no way to avoid collisions when more than one nodes sends the packets at the same timeMore efficient as the collisions can be avoided or reduced as compared to Hub

---

## 88. What is the difference between the ipconfig and the ifconfig?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

ipconfigifconfigInternet Protocol ConfigurationInterface ConfigurationCommand used in Microsoft operating systems to view and configure network interfacesCommand used in MAC, Linux, UNIX operating systems to view and configure network interfacesUsed to get the TCP/IP summary and allows to changes the DHCP and DNS settings

---

## 89. What is the firewall?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

The firewall is a network security system that is used to monitor the incoming and outgoing traffic and blocks the same based on the firewall security policies. It acts as a wall between the internet (public network) and the networking devices (a private network). It is either a hardware device, software program, or a combination of both. It adds a layer of security to the network.

Firewall

---

## 90. What are Unicasting, Anycasting, Multicasting and Broadcasting?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

- **Unicasting:** If the message is sent to a single node from the source then it is known as unicasting. This is commonly used in networks to establish a new connection.
- **Anycasting:** If the message is sent to any of the nodes from the source then it is known as anycasting. It is mainly used to get the content from any of the servers in the Content Delivery System.
- **Multicasting:** If the message is sent to a subset of nodes from the source then it is known as multicasting. Used to send the same data to multiple receivers.
- **Broadcasting:** If the message is sent to all the nodes in a network from a source then it is known as broadcasting. DHCP and ARP in the local network use broadcasting.

---

## 91. What happens when you enter google.com in the web browser?

*Source: [`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

Below are the steps that are being followed:

- Check the browser cache first if the content is fresh and present in cache display the same.
- If not, the browser checks if the IP of the URL is present in the cache (browser and OS) if not then request the OS to do a DNS lookup using UDP to get the corresponding IP address of the URL from the DNS server to establish a new TCP connection.
- A new TCP connection is set between the browser and the server using three-way handshaking.
- An HTTP request is sent to the server using the TCP connection.
- The web servers running on the Servers handle the incoming HTTP request and send the HTTP response.
- The browser process the HTTP response sent by the server and may close the TCP connection or reuse the same for future requests.
- If the response data is cacheable then browsers cache the same.
- Browser decodes the response and renders the content.

1. **What is a Network, and why is it important?**

*This foundational question tests your understanding of networking and its significance.*

“A network is a collection of computers, servers, mainframes, network devices, and other devices connected to share data, resources, and applications. Networking enables seamless communication, data exchange, and resource sharing between devices. In modern organizations, networks are critical for maintaining connectivity, ensuring data security, and supporting business operations by allowing fast, reliable access to information.”

2. **What is an IP Address, and what are the differences between IPv4 and IPv6?**

*Interviewers may ask this question to check your understanding of IP addressing, a crucial concept in networking.*

“An IP (Internet Protocol) address is a unique identifier assigned to devices on a network, allowing them to communicate. IPv4 and IPv6 are two types of IP addressing protocols:

- **IPv4**: Uses a 32-bit address format, allowing for approximately 4.3 billion unique addresses (e.g., 192.168.0.1).
- **IPv6**: Uses a 128-bit address format, supporting around 340 undecillion unique addresses (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

IPv6 was developed to address the exhaustion of IPv4 addresses and supports features like auto-configuration and improved security.”

3. **What is the OSI Model, and can you describe its layers?**

*Understanding the OSI model is fundamental in networking, and interviewers want to see if you grasp its importance.*

“The **OSI (Open Systems Interconnection) Model** is a conceptual framework that standardizes networking functions into seven layers:

1. **Physical Layer**: Transmits raw data bits over physical hardware.
2. **Data Link Layer**: Handles error detection and data framing, establishing links between nodes.
3. **Network Layer**: Manages IP addressing, routing, and data packet forwarding.
4. **Transport Layer**: Ensures reliable data transfer via protocols like TCP and UDP.
5. **Session Layer**: Manages sessions and connections between applications.
6. **Presentation Layer**: Translates data formats, handling encryption and compression.
7. **Application Layer**: Enables end-user applications to access network services.

Each layer has specific functions, allowing for interoperability and standardization across different systems.”

4. **What is DNS, and how does it work?**

*This question tests your knowledge of DNS, a crucial service in internet networking.*

“The **Domain Name System (DNS)** translates human-readable domain names (like `www.example.com`) into IP addresses that computers use to identify each other on the network. When a user enters a domain, the DNS server checks if it has a cached IP address. If not, it queries other DNS servers to resolve the IP, enabling the browser to load the correct website. DNS is essential for simplifying access to online resources without needing to remember complex IP addresses."

5. **What is a subnet, and how does subnetting work?**

*Subnetting is a core concept in IP addressing, and interviewers want to see if you understand its purpose.*

“A **subnet** is a smaller network within a larger IP network. **Subnetting** involves dividing an IP network into smaller sub-networks to improve efficiency, enhance security, and reduce network congestion. It allows for better management of IP addresses by breaking a network into logically separated segments, typically defined by subnet masks. For instance, in the IP `192.168.1.0/24`, the `/24` indicates the network portion, leaving 8 bits for host addresses."

6. **What are the differences between TCP and UDP?**

*This question assesses your knowledge of two fundamental transport protocols.*

“**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** are transport layer protocols but differ in functionality:

- **TCP**: Connection-oriented, providing reliable data transmission with error checking, flow control, and acknowledgment of data packets. It’s used for applications needing high reliability, like web browsing and email.
- **UDP**: Connectionless and faster, but less reliable as it doesn’t guarantee data delivery. It’s used for time-sensitive applications like video streaming, where speed is more critical than reliability.

Choosing TCP or UDP depends on the application’s need for speed versus reliability.”

7. **What is NAT, and why is it used?**

*Network Address Translation (NAT) is essential for modern networking, and this question checks if you know its purpose.*

“**Network Address Translation (NAT)** is a process that modifies the IP addresses in data packets as they pass through a router, allowing multiple devices on a private network to share a single public IP address. NAT is commonly used to conserve IP addresses, improve security by hiding internal IPs, and enable devices within a local network to access the internet using a single public IP.”

8. **What is a VLAN, and why is it important?**

*This question assesses your understanding of VLANs and their benefits in network segmentation.*

“A **VLAN (Virtual Local Area Network)** is a logical grouping of devices on a network, allowing them to communicate as if they were on the same physical LAN, even if they’re not. VLANs enable network segmentation, enhancing security and efficiency by isolating different departments or groups within the same physical network. For instance, VLANs can separate traffic from finance, HR, and IT, reducing broadcast traffic and improving network performance.”

9. **What is a Firewall, and what are its main types?**

*This question tests your understanding of network security and firewall functionality.*

“A **Firewall** is a network security device that monitors and filters incoming and outgoing network traffic based on predefined security rules. Firewalls protect against unauthorized access, malicious attacks, and network intrusions. The main types of firewalls include:

- **Packet-Filtering Firewalls**: Check packets based on IP addresses, ports, and protocols.
- **Stateful Inspection Firewalls**: Track active connections and allow packets based on the connection state.
- **Proxy Firewalls**: Act as intermediaries, filtering requests between users and the internet.
- **Next-Generation Firewalls (NGFW)**: Integrate advanced features like application-level inspection and intrusion prevention.”

Firewalls are essential for network security, safeguarding data and preventing unauthorized access.”

10. **What are some best practices for securing a network?**

*This question assesses your understanding of network security best practices.*

“Best practices for securing a network include:

- **Use firewalls**: Implement firewalls to control incoming and outgoing traffic based on security rules.
- **Enable encryption**: Use protocols like SSL/TLS and VPNs to encrypt data and protect it during transmission.
- **Regular updates and patches**: Keep network devices and software up to date to prevent exploitation of vulnerabilities.
- **Implement strong access

*…(truncated — see the source note for the full answer)*

---

## Question bank (no recorded answers)

Prompts collected from the notes that have no written answer yet:

- What is the difference between switch and hub? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is the difference between Switch and Router? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- Explain the difference between HTTP, HTTPs, TCP, UDP and gRPC. — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- Which layer is the Application Layer, and what is its function? The Application Layer is the topmost layer, providing network services directly to applications. It handles protocols and data that applications use to communicate over the network. — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- Which layers are considered the hardware or network support layers? The Data Link Layer and Physical Layer are considered hardware or network support layers. They deal with the physical transmission of data and error detection/correction. — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is a Network, and why is it important? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is an IP Address, and what are the differences between IPv4 and IPv6? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is the OSI Model, and can you describe its layers? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is DNS, and how does it work? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is a subnet, and how does subnetting work? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What are the differences between TCP and UDP? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is NAT, and why is it used? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is a VLAN, and why is it important? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What is a Firewall, and what are its main types? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*
- What are some best practices for securing a network? — *[`04-networking/networking-interview-questions.md`](../04-networking/networking-interview-questions.md)*

