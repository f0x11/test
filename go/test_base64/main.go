package main

import (
	"encoding/base64"
	"fmt"
)

func main() {
	//msg := "Hello, 世界"
	//encoded := base64.StdEncoding.EncodeToString([]byte(msg))
	//fmt.Println(encoded)
	encoded := "L2FhcHAvc2Rmc2Q="
	decoded, err := base64.StdEncoding.DecodeString(encoded)
	if err != nil {
		fmt.Println("decode error:", err)
		return
	}
	fmt.Println(string(decoded))
}
