from datetime import datetime
from uuid import uuid4
from .contracts import MCPContextSnapshot, MSPDataset
from .operators import AggregationOperators
from .registry import AGGREGATION_REGISTRY


class AggregationEngine:

    def aggregate(self, snapshots, metric_key, subscriber_id):
        metric = AGGREGATION_REGISTRY[metric_key]
        operator_name = metric["operator"]

        operator = getattr(AggregationOperators, operator_name)

        values = [
            s.payload.get("value")
            for s in snapshots
            if "value" in s.payload
        ]

        result = operator(values)

        return MSPDataset(
            dataset_id=uuid4(),
            metric_key=metric_key,
            metric_version=metric["version"],
            subscriber_id=subscriber_id,
            time_window={
                "from": snapshots[0].timestamp,
                "to": snapshots[-1].timestamp
            },
            data={"result": result},
            generated_at=datetime.utcnow()
        )