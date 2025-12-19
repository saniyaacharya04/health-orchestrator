_USAGE = {}

def record_usage(org_id: str, metric: str):
    _USAGE.setdefault(org_id, {})
    _USAGE[org_id][metric] = _USAGE[org_id].get(metric, 0) + 1

def get_usage(org_id: str):
    return _USAGE.get(org_id, {})
