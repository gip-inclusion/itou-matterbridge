import logging
import os
import signal
import subprocess

from werkzeug.wrappers import Request, Response

logger = logging.getLogger('werkzeug.main')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def ping_supervisor_for(process_name: str):
    process = subprocess.run([f"supervisorctl status {process_name}"], check=False, env=None, capture_output=True, shell=True)

    process_stdout = process.stdout.decode("utf-8")
    process_is_down = process.returncode == 4
    if process_is_down:
        logger.error(process_stdout)
    else:
        logger.info(process_stdout)
    return not process_is_down


@Request.application
def application(_):
    process_up = ping_supervisor_for("matterbridge")
    response = Response("OK")
    if not process_up:
        response = Response("Unavailable process", status=500)
        os.kill(os.getppid(), signal.SIGINT)

    return response


# Development server.
if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 4000, application, use_reloader=True)
