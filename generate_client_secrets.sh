#!/bin/sh
if [ ! -f "client_secrets.json" ] 
then
	echo "client_secrets.json not found, generating..."
 	curl --request POST --header "Content-Type: application/json" --data '{"redirect_uris": ["http://localhost:8000/oidc/callback/"], "application_type": 
"native","token_endpoint_auth_method": "client_secret_post"}' https://iddev.fedorainfracloud.org/openidc/Registration -o client_secrets.json
fi
