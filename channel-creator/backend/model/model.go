package model

import (
	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

var db *sql.DB

func DBInit() *sql.DB {
	return nil
}

func AppInit() {
}

func DBConn() *sql.DB {
	return nil
}
