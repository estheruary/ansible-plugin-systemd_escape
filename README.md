# Ansible Collection - estheruary.systemd_escape

An Ansible filter plug-in which uses `systemd-escape` to manipulate strings for use in systemd units.

## Requirements

You'll need to have a recent-ish version of systemd on the host where the filer will be running.

## Example Playbook
```yaml
---
  - hosts: all
    tasks:
      - debug:
          msg: "{{ "Hello, World!" | estheruary.systemd_escape.systemd_escape(path=True, suffix='mount' }}"
```

## License

GPLv3

## Author Information

* Estelle Poulin <dev@inspiredby.es>
