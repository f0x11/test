package main

import (
	"strconv"
	"fmt"
)

func main() {
	a, err := strconv.ParseUint("", 10, 64)
	fmt.Println(a, err)
}
