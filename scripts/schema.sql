CREATE TABLE organizations (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    plan TEXT NOT NULL
);

CREATE TABLE api_keys (
    key TEXT PRIMARY KEY,
    org_id UUID REFERENCES organizations(id)
);

CREATE TABLE usage (
    org_id UUID,
    metric TEXT,
    count INT,
    PRIMARY KEY (org_id, metric)
);
