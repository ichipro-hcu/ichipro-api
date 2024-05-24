package presenter

import (
	"context"

	"github.com/gin-gonic/gin"
	"github.com/ichipro-hcu/ichipro-api/api/internal/controller/system"
	"github.com/ichipro-hcu/ichipro-api/api/internal/controller/user"
)

const latest = "/v1"

type Server struct{}

func (s *Server) Run(ctx context.Context) error {
	r := gin.Default()
	v1 := r.Group(latest)

	// HeartBeat
	{
		systemHandler := system.NewSystemHandler()
		v1.GET("/health", systemHandler.Health)
	}

	{
		userHandler := user.NewUserHandler()
		v1.GET("users", userHandler.GetUsers)
		v1.GET("/users/:id", userHandler.GetUserById)
		v1.POST("users", userHandler.EditUser)
		v1.DELETE("/users/:id", userHandler.DeleteUser)
	}

	err := r.Run()
	if err != nil {
		return err
	}

	return nil
}

func NewServer() *Server {
	return &Server{}
}
