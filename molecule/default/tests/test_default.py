"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "directory", [{"path": "/var/cyhy/code-gov-update", "mode": "0o755"}]
)
def test_packages(host, directory):
    """Test that the appropriate directories were created."""
    assert host.file(directory["path"]).exists
    assert host.file(directory["path"]).is_directory
    assert oct(host.file(directory["path"]).mode) == directory["mode"]


@pytest.mark.parametrize(
    "file", [{"path": "/var/cyhy/code-gov-update/docker-compose.yml", "mode": "0o644"}]
)
def test_command(host, file):
    """Test that appropriate files exist."""
    assert host.file(file["path"]).exists
    assert host.file(file["path"]).is_file
    assert oct(host.file(file["path"]).mode) == file["mode"]
