package paths

// Route for seeing if server is up

import (
	"encoding/json"
	"net/http"

	"github.com/gin-gonic/gin"
)

type PingResponse struct {

	Success int `json:"success"`

}

func PingHandler(ctx *gin.Context) {

	resp := PingResponse {
		Success: 1,
	}

	respJSON, _ := json.Marshal(resp)

	ctx.Data(http.StatusOK, "application/json", respJSON)

}