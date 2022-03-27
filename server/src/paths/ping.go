package paths

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func PingHandler(ctx *gin.Context) {
	
	ctx.JSON(http.StatusOK, gin.H{"message" : "ping",})

}