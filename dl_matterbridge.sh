unzip matterbridge.zip
mv matterbridge-v1.26.0-33-g89b0d362-linux-amd64 matterbridge

chmod +x matterbridge
supervisord -c $APP_HOME/supervisord.conf


