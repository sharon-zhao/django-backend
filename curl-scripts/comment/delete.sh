#!/bin/bash

curl "http://localhost:8000/comment/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
