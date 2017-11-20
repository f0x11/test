package main

import (
	"fmt"
	"strings"
)

func main() {
	//if "" {
	//	fmt.Println("t")
	//} else {
	//	fmt.Println("f")
	//}
	//fmt.Println(""||"5")
a:= "oink oink oink"
	b:= "3333"
	c := b[0:3]
	fmt.Println(c + "sdsf")
	fmt.Println(strings.Replace(a, "k", "ky", 2))
	fmt.Println(a)

	f:="go gopher"
	fmt.Println(strings.Index("go gopher", "go"))
	rIdx := strings.LastIndex(f, "go")
	e:= f[:rIdx]
	fmt.Println(f[rIdx + len("go"):])
	fmt.Println(e + "sdfds")
	fmt.Println(strings.LastIndex("go gopher", "rodent"))

}
