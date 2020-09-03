#!/bin/bash

curl "http://localhost:8000/comment/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
