package main

import (
	"context"

	"github.com/ichipro-hcu/ichipro-api/api/internal/presenter"
)

// @title Ichipro API
// @version v0.0.1
// @description User Service API
// @host localhost:8080

func main() {
	srv := presenter.NewServer()
	if err := srv.Run(context.Background()); err != nil {
		panic(err)
	}
}
