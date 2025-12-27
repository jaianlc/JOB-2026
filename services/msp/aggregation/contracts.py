from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict
from uuid import UUID


@dataclass(frozen=True)
class MCPContextSnapshot:
    context_id: UUID
    mcp_version: str
    timestamp: datetime
    source: str
    payload: Dict[str, Any]


@dataclass
class MSPDataset:
    dataset_id: UUID
    metric_key: str
    metric_version: str
    subscriber_id: UUID
    time_window: Dict[str, datetime]
    data: Dict[str, Any]
    generated_at: datetime