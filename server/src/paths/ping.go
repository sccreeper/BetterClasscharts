package paths

// Route for seeing if server is up

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func PingHandler(ctx *gin.Context) {
	
	ctx.JSON(http.StatusOK, "OK")

}