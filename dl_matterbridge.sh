wget https://github.com/42wim/matterbridge/releases/download/v1.25.2/matterbridge-1.25.2-linux-64bit -O matterbridge
chmod +x matterbridge
supervisord -c $APP_HOME/supervisord.conf
