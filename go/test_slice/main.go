package main

import "fmt"

func main() {
	a := "dfsdf"
	fmt.Println(a[:3])

	b := append([]int{1,2,3}, 4)

	c := b

	b[3] =5

	fmt.Println(c)

	if("" == "") {
		fmt.Println("true")
	}
}
