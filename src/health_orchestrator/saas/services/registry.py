import uuid

_SERVICES = {}

def register_service(org_id: str, name: str):
    service_id = str(uuid.uuid4())
    _SERVICES[service_id] = {
        "id": service_id,
        "org_id": org_id,
        "name": name
    }
    return _SERVICES[service_id]

def get_services_for_org(org_id: str):
    return [s for s in _SERVICES.values() if s["org_id"] == org_id]
