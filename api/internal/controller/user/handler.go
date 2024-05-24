package user

import "github.com/gin-gonic/gin"

type UserHandler struct{}

// GetUsers godoc
// @summary Get Users
// @Tags GetUsers
// @Accept json
// @produce json
// @Success 200 {object} []ResponseUser
// @Router /v1/users [get]

func (h *UserHandler) GetUsers(ctx *gin.Context) {}

// GetUserById godoc
// @Summary Get User Info
// @Tags GetUserById
// @Accept json
// @Produce json
// @Param request path string ture "ユーザーID"
// @Success 200 {object} ResponseUser
// @Router /v1/users/:id [get]
func (h *UserHandler) GetUserById(ctx *gin.Context) {}

// EditUser godoc
// @Summary Edit User Info
// @Tags User
// @Accept json
// @Produce json
// @Param request body RequestUserParam ture "ユーザー情報"
// @Success 200 {object} Response
// @Router /v1/users [post]
func (h *UserHandler) EditUser(ctx *gin.Context) {}

// DeleteUser godoc
// @Summary ユーザー情報を削除
// @Tags Delete User
// @Accept json
// @Produce json
// @Param request path string ture "ユーザーID"
// @Success 200 {object} Response
// @Router /v1/users [delete]
func (h *UserHandler) DeleteUser(ctx *gin.Context) {}

func NewUserHandler() *UserHandler {
	return &UserHandler{}
}
