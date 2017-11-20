package main

import (
	"net"
	"fmt"
	"strings"
	"strconv"
)

func main() {
	ip, ipnet, err := net.ParseCIDR("192.168.100.1/24")
	fmt.Println(ip, ipnet.IP.To4(), ipnet.Mask, err)
	fmt.Println(ipnet.Mask.Size())
	fmt.Println(strings.Count(string(ipnet.Mask.String()), "0"))
	//fmt.Println(net.ParseIP("56.3.4.12").Mask(net.IPMask("ff000000")))
	mask, max := ipnet.Mask.Size()
	a := 1 << uint(max - mask)
	fmt.Println(len(strconv.Itoa(a)))
	fmt.Println(string(byte(49) + 49))
}
