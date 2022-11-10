from ansible.errors import AnsibleFilterError
import subprocess

SYSTEMD_ESCAPE = 'systemd-escape'

def systemd_escape(s,
        suffix=None,
        template=None,
        path=False,
        mangle=False):

    cmd = [SYSTEMD_ESCAPE]

    # If any two options are truthy.
    if suffix and (template or mangle) or (template and mangle):
        raise AnsibleFilterError("Options suffix, template, and mangle are mutually exclusive.")

    if suffix:
        cmd += ["--suffix='{}'".format(suffix)]
    elif template:
        cmd += "--template='{}'".format(template)
    elif mangle:
        cmd += ["--mangle"]

    if path:
        cmd += ["--path"]

    cmd += [s]

    try:
        res = subprocess.check_call(cmd)
    except Exception as e:
        raise AnsibleFilterError('Error in subprocess.check_call in systemd_escape filter plugin:\n%s' % e)

    return res

def systemd_unescape(s,
        path=False):

    cmd = [SYSTEMD_ESCAPE]

    if path:
        cmd += ["--path"]

    cmd += [s]

    try:
        res = subprocess.check_call(cmd)
    except Exception as e:
        raise AnsibleFilterError('Error in subprocess.check_call in systemd_escape filter plugin:\n%s' % e)

    return res

class FilterModule(object):
    def filters(self):
        return {
            'systemd_escape': systemd_escape,
            'systemd_unescape': systemd_unescape
        }
