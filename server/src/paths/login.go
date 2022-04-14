// Login path to validate user and add them to the hashmap in memory.
package paths

import (
	"encoding/json"
	"net/http"
	"sccreeper/bcc-cache-server/src/shared"

	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

type LoginData struct {

	ID string `json:"id"`
	Name string `json:"name"`
	
}

type LoginMeta struct {
	SessionID string `json:"session_id"`
}

type LoginResponse struct {

	Success int `json:"success"`
	Data LoginData `json:"data"`
	Meta LoginMeta `json:"meta"`

}

type HasCodeResponse struct {
	Success int `json:"success"`
	Data HasCodeResponseData `json:"data"`
}

type HasCodeResponseData struct {
	HasDob bool `json:"has_dob"`
}

type OwnLoginResponse struct {

	Success int `json:"success"`

	Data OwnLoginResponseData `json:"data"`

}

type OwnLoginResponseData struct {
	SessionID string `json:"session_id"`
}

func LoginHandler(ctx *gin.Context) {

	code := ctx.PostForm("code")
	dob := ctx.PostForm("dob")
		
		//Return user session ID

		serverSessionID := uuid.New()

		shared.LoggedInUsers[serverSessionID.String()] = shared.UserInfo{

			OwnSessionID: serverSessionID.String(),

			StudentCode: code,
			StudentDOB: dob,

		}

		clientResponse := OwnLoginResponse {

			Success: 1,
			Data: OwnLoginResponseData{
				SessionID: serverSessionID.String(),
			},
		}

		respJSON, _ := json.Marshal(clientResponse)

		ctx.Data(http.StatusOK, "application/json", respJSON)

}