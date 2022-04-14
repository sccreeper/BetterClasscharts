package shared

type UserInfo struct {


	OwnSessionID string

	StudentCode string
	StudentDOB string

}

var LoggedInUsers = make(map[string]UserInfo)


