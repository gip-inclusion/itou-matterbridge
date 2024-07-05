unzip matterbridge.zip
mv matterbridge-v1.26.0-51-gd16645c9-linux-amd64 matterbridge

chmod +x matterbridge
supervisord -c $APP_HOME/supervisord.conf


