wget --header "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/repos/42wim/matterbridge/actions/artifacts/634227033/zip -O matterbridge.zip
unzip matterbridge.zip
mv matterbridge-v1.26.0-33-g89b0d362-linux-amd64 matterbridge

chmod +x matterbridge
supervisord -c $APP_HOME/supervisord.conf
