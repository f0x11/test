package main

import (
	"time"
	"fmt"
	"encoding/json"
)

type Catalog struct {
	ID          uint      `json:"id" gorm:"primary_key"`
	CreatedAt   time.Time `json:"createdAt"`
	UpdatedAt   time.Time `json:"updatedAt"`
	Name        string    `json:"name" gorm:"size:255"`
	Json        string    `json:"json" gorm:"type:text"`
	IconData    string    `json:"iconData" gorm:"type:text"`
	Desc        string    `json:"desc" gorm:"type:text"`
	IsPublic    bool      `json:"-" gorm:"type:bool"`
	GroupId     uint64    `json:"groupId" gorm:"index"`
	GroupName   string    `json:"groupName" gorm:"-"`
	AccountId   uint64    `json:"accountId" gorm:"index"`
	AccountName string    `json:"userName" gorm:"-"`
}

func main() {
	a := Catalog{}
	b, _ := json.Marshal(a)
	fmt.Println(string(b))
}
