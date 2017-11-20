package main

import (
	"net/url"
	"path"
	"fmt"
)

func main() {
	u, _ := url.Parse("http://www.baidu.com")
	u.Path = path.Join(u.Path, "bar")
	s := u.String()

	fmt.Println(s)
}
