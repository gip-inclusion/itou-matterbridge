FROM 42wim/matterbridge:stable

COPY ./matterbridge.toml /etc/matterbridge/matterbridge.toml

# Required by Clever Cloud.
# listen on HTTP port 8080 by default (you can set your own port using CC_DOCKER_EXPOSED_HTTP_PORT=<port> environment variable).
EXPOSE 8080

ENTRYPOINT ["/bin/matterbridge", "-conf", "/etc/matterbridge/matterbridge.toml"]
