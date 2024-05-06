cat <<EOF > auth.py
url="${SERVER_URL}"

auth_token = "${AUTH_TOKEN}"
user_id = "${USER_ID}"

days_iddle = "${DAYS_IDDLE}"
EOF
cat auth.py
python3 rocketchat_block_iddle.py