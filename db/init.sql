CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE swings(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    date DATE NOT NULL,
    notes TEXT
);

CREATE TABLE clips(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    swing_id UUID NOT NULL REFERENCES swings(id),
    angle TEXT NOT NULL CHECK (angle IN ('faceon', 'sideon')),
    filepath TEXT NOT NULL,
    fps INTEGER,
    status TEXT NOT NULL DEFAULT 'uploaded'
        CHECK (status IN ('uploaded', 'pose_processing', 'pose_complete', 'metrics_complete', 'failed'))
);

CREATE TABLE pose_frames(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    swing_id UUID NOT NULL REFERENCES swings(id),
    metric_name TEXT NOT NULL,
    value FLOAT NOT NULL,
    computed_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE swing_metrics(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
    swing_id UUID NOT NULL REFERENCES swings(id),
    metric_name TEXT NOT NULL,
    value FLOAT NOT NULL,
    computed_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE INDEX idx_pose_frames_swing_id ON pose_frames(swing_id);
CREATE INDEX idx_swing_metrics_swing_id ON swing_metrics(swing_id);