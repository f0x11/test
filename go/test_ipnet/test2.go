package main

import (
	"net"
	"encoding/binary"
	"fmt"
)

func Ip2Int(ip net.IP) uint32 {
	if len(ip) == 16 {
		return binary.BigEndian.Uint32(ip[12:16])
	}
	return binary.BigEndian.Uint32(ip)
}

func Int2Ip(nn uint32) net.IP {
	ip := make(net.IP, 4)
	binary.BigEndian.PutUint32(ip, nn)
	return ip
}

func main() {
	fmt.Println(Ip2Int(net.ParseIP("192.168.1.1")))
	fmt.Println(Ip2Int(net.ParseIP("192.168.1.3")))
	fmt.Println(Int2Ip(168493055))
	fmt.Println(Int2Ip(Ip2Int(net.ParseIP("192.168.1.1"))).String())
}
