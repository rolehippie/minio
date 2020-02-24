import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_running_and_enabled(host):
    svc = host.service("minio")
    assert svc.is_running
    assert svc.is_enabled


def test_server_socket(host):
    assert host.socket("tcp://127.0.0.1:9000").is_listening


def test_client_file(host):
    file = host.file("/usr/local/bin/mc")
    assert file.exists


def test_client_exec(host):
    cmd = host.run("mc --help")
    assert cmd.succeeded
