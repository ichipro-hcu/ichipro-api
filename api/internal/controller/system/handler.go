package system

import "github.com/gin-gonic/gin"

type SystemHandler struct{}

// HealthCheck godoc
// @summary HealthCheck
// @Tags healthcheck
// @Accept json
// @produce json
// @Success 200 {object} Response
// @Router /v1/health [get]

func (h *SystemHandler) Health(ctx *gin.Context) {
	ctx.JSON(200, gin.H{
		"Success": true,
	})
}

func NewSystemHandler() *SystemHandler {
	return &SystemHandler{}
}
