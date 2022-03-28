package shared

import (
	"net/http"
)

type UserInfo struct {

	Cookies []*http.Cookie
	ClasschartsSessionID string
	OwnSessionID string

	StudentID string
	StudentDOB string

}

var LoggedInUsers = make(map[string]UserInfo)


