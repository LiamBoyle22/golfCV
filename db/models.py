from sqlalchemy import Column, Date, String, ForeignKey, Integer, Float, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
import uuid


Base = declarative_base()

class Swings(Base):
    __tablename__ = "swings"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, nullable=False)
    notes = Column(String)

class Clips(Base):
    __tablename__ = "clips"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    swing_id = Column(UUID(as_uuid=True), ForeignKey("swings.id"), nullable=False)
    angle = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    fps = Column(Integer)
    status = Column(String, nullable=False, default="uploaded")

class Pose_frames(Base):
    __tablename__ = "pose_frames"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    clip_id = Column(UUID(as_uuid=True), ForeignKey("clips.id"), nullable=False)
    frame_number = Column(Integer, nullable=False)
    timestamp = Column(Float, nullable=False)
    keypoints = Column(JSONB, nullable=False)

class Swing_metrics(Base):
    __tablename__ = "swing_metrics"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    swing_id = Column(UUID(as_uuid=True), ForeignKey("swings.id"), nullable=False)
    metric_name = Column(String, nullable=False)
    metric_value = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
