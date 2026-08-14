from sqlalchemy import Column, Date, String, ForeignKey, Integer, Float, DateTime, check, UniqueConstraint
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
import uuid


Base = declarative_base()

class swing(Base):
    __tablename__ = "swing"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, nullable=False)
    notes = Column(String)

class clip(Base):
    __tablename__ = "clip"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    swing_id = Column(UUID(as_uuid=True), ForeignKey("swing.id"), primary_key=True, nullable=False)
    angle = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    fps = Column(Integer)
    status = Column(String, nullable=False, default="uploaded")

class PoseFrames(Base):
    __tablename__ = "PoseFrames"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    clip_id = Column(UUID(as_uuid=True), ForeignKey("clip.id"), nullable=False)
    frame_number = Column(Integer, nullable=False)
    timestamp = Column(Float, nullable=False)
    keypoints = Column(JSONB, nullable=False)

class SwingMetrics(Base):
    __tablename__ = "SwingMetrics"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    swing_id = Column(UUID(as_uuid=True), ForeignKey("swing.id"), nullable=False)
    metric_name = Column(String, nullable=False)
    metric_value = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
