#!/bin/bash

curl "http://localhost:8000/comment" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "comment": {
      "body": "'"${BODY}"'",
      "post": "'"${POST}"'"
    }
  }'

echo
