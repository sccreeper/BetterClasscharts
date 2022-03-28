FROM golang:alpine

WORKDIR /usr/src/app
EXPOSE 80

COPY . .

#RUN go install .
RUN go build -ldflags "-s -w" ./src/main.go

CMD [ "./main" ]


