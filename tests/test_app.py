"""Tests for app-level helpers."""

import socket

from claude_transcript_collector.app import _find_free_port


def test_find_free_port_skips_occupied():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen()
    occupied = s.getsockname()[1]
    try:
        port = _find_free_port(occupied, tries=50)
        assert port is not None and port != occupied
        # the returned port is actually bindable
        probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        probe.bind(("127.0.0.1", port))
        probe.close()
    finally:
        s.close()


def test_find_free_port_returns_start_when_free():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    free = s.getsockname()[1]
    s.close()  # now free
    assert _find_free_port(free, tries=5) == free
