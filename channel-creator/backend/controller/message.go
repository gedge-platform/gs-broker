package controller

import (
	"net/http"
)

type MessageInfo struct {
}

func GetMessages(w http.ResponseWriter, r *http.Request) {
}

func SendMessage(w http.ResponseWriter, r *http.Request) {
}

func DeleteMessage(w http.ResponseWriter, r *http.Request) {
}

func pubMsg(c Cluster, mInfo MessageInfo, jsonData []byte) error {
	return nil
}

func queueMsg(c Cluster, mInfo MessageInfo, jsonData []byte) error {
	return nil
}

func queryMsg(c Cluster, mInfo MessageInfo, jsonData []byte) error {
	return nil
}

func commandMsg(c Cluster, mInfo MessageInfo, jsonData []byte) error {
	return nil
}
