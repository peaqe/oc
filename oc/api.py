"""OpenShift CLI (oc) thin wrapper."""

import logging
import pexpect


logger = logging.getLogger(__name__)


def oc(params):
    """Run oc with params.

    May raise `RuntimeError` on error.
    """
    cmd = f'oc {params}'
    logger.debug(cmd)
    output = pexpect.run(cmd).decode('utf-8')
    if output.startswith('error:') or output.startswith('Error:'):
        raise RuntimeError(output)
    logger.debug(output)
    return output


def parse(output):
    """Parse (normalize) output and return a list of lines."""
    output = output.split('\r\n')
    output = [line for line in output if line]
    return output


def login(openshift_url, token):
    """Log in on openshift_url with Bearer token."""
    cmd = f'login {openshift_url} --token={token}'
    return parse(oc(cmd))


def whoami():
    """Get my username."""
    cmd = f'whoami'
    return parse(oc(cmd))


def logout():
    """Log out from OpenShift."""
    cmd = 'logout'
    return parse(oc(cmd))


def get_projects():
    """Get all projects."""
    cmd = 'projects -q'
    return parse(oc(cmd))


def get_project():
    """Get current project."""
    cmd = 'project'
    return parse(oc(cmd))


def set_project(name):
    """Select project by name."""
    cmd = f'project {name}'
    return parse(oc(cmd))


def get_pods():
    """Get all pods."""
    cmd = 'get pods'
    return parse(oc(cmd))


def logs(pod, since=None, tail=None, timestamps=None):
    """Get logs from pod.

    Provides flags for the `since`, `tail`, and `timestamps` flags.
    """
    cmd = f'logs {pod}'
    if since:
        cmd = cmd + f' --since={since}'
    if tail:
        cmd = cmd + f' --tail={tail}'
    if timestamps:
        cmd = cmd + f' --timestamps={timestamps}'
    return parse(oc(cmd))


def exec(pod, command):
    """Execute command in pod."""
    cmd = f'exec {pod} -- {command}'
    return parse(oc(cmd))


def rsh(pod, command):
    """Open remote shell in pod and execute a command."""
    cmd = f'rsh {pod} {command}'
    return parse(oc(cmd))
