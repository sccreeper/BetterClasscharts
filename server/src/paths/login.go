// Login path to validate user and add them to the hashmap in memory.
package paths

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"sccreeper/bcc-cache-server/src/endpoints"
	"sccreeper/bcc-cache-server/src/shared"
	"strings"

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

	Data OwnLoginResponseData

}

type OwnLoginResponseData struct {
	Response string `json:"response"`
}

func LoginHandler(ctx *gin.Context) {

	client := http.Client{}

	code := ctx.PostForm("code")
	dob := ctx.PostForm("dob")

	// See if code is valid on ClassCharts

	checkCodeRequest, _ := http.NewRequest("GET", fmt.Sprintf("%s%s%s", endpoints.Domain, endpoints.CheckCode, code), nil)
	checkCodeRequest.Header.Set("User-Agent", "Mozilla/5.0")

	resp, _ := client.Do(checkCodeRequest)

	var codeResp HasCodeResponse

	body, _ := io.ReadAll(resp.Body)

	json.Unmarshal([]byte(body), &codeResp)

	println(codeResp.Data.HasDob)

	if codeResp.Data.HasDob{
		
		//Set POST request to cc-servers to get session token.

		loginForm := url.Values{}

		loginForm.Add("_method", "POST")
		loginForm.Add("code", code)
		loginForm.Add("dob", dob)
		loginForm.Add("remember_me", "1")
		loginForm.Add("recaptcha-token", "no-token-available")

		loginReq, _ := http.NewRequest("POST", fmt.Sprintf("%s%s", endpoints.Domain, endpoints.Login), strings.NewReader(loginForm.Encode()))
		loginReq.Header.Add("User-Agent", "Mozilla/5.0")
		loginReq.Header.Add("Content-Type", "application/x-www-form-urlencoded")

		resp, _ := client.Do(loginReq)

		var loginResp LoginResponse

		body, _ := io.ReadAll(resp.Body)

		json.Unmarshal([]byte(body), &loginResp)

		serverSessionID := uuid.New()

		shared.LoggedInUsers[serverSessionID.String()] = shared.UserInfo{

			Cookies: resp.Cookies(),
			ClasschartsSessionID: loginResp.Meta.SessionID,
			OwnSessionID: serverSessionID.String(),

			StudentID: loginResp.Data.ID,
			StudentDOB: dob,

		}

		clientResponse := OwnLoginResponse {

			Success: 1,
			Data: OwnLoginResponseData{
				Response: serverSessionID.String(),
			},
		}

		respJSON, _ := json.Marshal(clientResponse)

		ctx.Data(http.StatusOK, "application/json", respJSON)

	} else {

		ctx.String(http.StatusInternalServerError, "cc-error")

	}


}