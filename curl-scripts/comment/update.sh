#!/bin/bash

curl "http://localhost:8000/comment/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "comment": {
      "body": "'"${BODY}"'"
    }
  }'

echo
