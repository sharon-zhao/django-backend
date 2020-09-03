#!/bin/bash

curl "http://localhost:8000/comment" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
