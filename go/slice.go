package main

import "fmt"

func test1() {
	d := []int{1, 2, 3, 4}
	e := d[2:]
	f := e
	fmt.Println("d1 =", d)
	fmt.Println("e1 =", e)
	fmt.Println("f1 =", f)
	e = append(e, 5, 6)
	e[1] = 7
	fmt.Println("d2 =", d)
	fmt.Println("e2 =", e)
	fmt.Println("f2 =", f)
}

func test2() {
	var slice []int

	fmt.Println("nil len =", len(slice))
	fmt.Println("nil cap =", cap(slice))

	newSlice := append(slice, 5, 99)

	fmt.Println("newSlice len =", len(newSlice))
	fmt.Println("newSlice cap =", cap(newSlice))

	newSlice = append(newSlice, 6)

	fmt.Println("newSlice len =", len(newSlice))
	fmt.Println("newSlice cap =", cap(newSlice))

	newSlice = append(newSlice, 7)

	fmt.Println("newSlice len =", len(newSlice))
	fmt.Println("newSlice cap =", cap(newSlice))
}

func main() {
	test2()
}
