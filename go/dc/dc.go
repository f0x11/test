package main

import "fmt"

type Slave struct {
	name string
	Attributes map[string]string `json:"attributes"`
}

func main() {
	data := []Slave{
		{
			name : "3333",
			Attributes: map[string]string{"label": "2"},
		},
		{
			name: "5555",
			Attributes: map[string]string{"la2bel": "3"},
		},
	}

	slaves := make([]*Slave, 0)

	for i := range data {
		slaves = append(slaves, &(data[i]))
	}

	fmt.Println(slaves[0])
		fmt.Println(slaves[1])
}
