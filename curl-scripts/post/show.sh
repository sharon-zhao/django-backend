#!/bin/bash

curl "http://localhost:8000/post/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
