package main

import (
	"fmt"
)

type app struct {
	Env map[string]string
}

func UniqueSlice(slice *[]uint64) {
	found := make(map[uint64]bool)
	total := 0
	for i, val := range *slice {
		if _, ok := found[val]; !ok {
			found[val] = true
			(*slice)[total] = (*slice)[i]
			total++
		}
	}

	*slice = (*slice)[:total]
}

func main() {
	a := []uint64{1,2,3,3,4,5}
	UniqueSlice(&a)

	fmt.Println(a)
}
