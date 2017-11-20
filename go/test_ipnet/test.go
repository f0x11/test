package main

import (
	"fmt"
	"strconv"
	"math"
)

func main() {
	fmt.Println(string([]byte(strconv.Itoa(2))[0]+ 49))
	fmt.Println(string(byte(string(2)[0]) + 49))
	fmt.Println(string(byte(2) + 49))
	fmt.Println(strconv.Itoa(int(math.Pow10(2))))
}
