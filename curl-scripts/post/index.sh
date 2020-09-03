#!/bin/bash

curl "http://localhost:8000/post" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
