package main

import (
	"sccreeper/bcc-cache-server/src/paths"

	"github.com/gin-gonic/gin"
)

func main() {

	println("Starting server...")

	r := gin.Default()

	r.GET("/ping", paths.PingHandler)
	r.POST("/login", paths.LoginHandler)

	r.Run()

}
