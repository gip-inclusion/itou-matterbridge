from werkzeug.wrappers import Request, Response


@Request.application
def application(request):
    return Response('Hello, World!')

# Development server.
if __name__ == '__main__':
    from werkzeug.serving import run_simple

    # TODO: use extra_files option to watch the configuration file.
    run_simple('localhost', 4000, application)
