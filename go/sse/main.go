package main

import (
 	"github.com/gin-gonic/gin"
	"time"
)

func main() {
	router := gin.Default()
	router.POST("/post", func(c *gin.Context) {
		for {
			c.SSEvent("test", time.Now().Second())
			time.Sleep(time.Second)
		}
	})
	router.Run(":8080")
}
