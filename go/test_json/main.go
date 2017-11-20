package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	type User struct {
		ID                         string               `json:"id,omitempty"`
	}
	user := User{ID: ""}
	b, _ := json.Marshal(user)
	fmt.Println(string(b))
}
