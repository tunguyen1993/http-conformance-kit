"""Zero-dependency HTTP status & JSON key conformance checker."""
from typing import Any, Dict, Iterable, List


def check_required_keys(payload: Dict[str, Any], required: Iterable[str]) -> List[str]:
    """Return missing or null keys from a parsed JSON object."""
    return [k for k in required if k not in payload or payload[k] is None]


if __name__ == '__main__':
    assert check_required_keys({'ok': True, 'count': 3}, ['ok', 'count']) == []
    assert check_required_keys({'ok': True}, ['ok', 'missing']) == ['missing']
    print('PASS conformance_check')
