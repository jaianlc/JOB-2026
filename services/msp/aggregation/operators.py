class AggregationOperators:

    @staticmethod
    def count(events):
        return len(events)

    @staticmethod
    def min(values):
        return min(values)

    @staticmethod
    def max(values):
        return max(values)

    @staticmethod
    def avg(values):
        return sum(values) / len(values) if values else 0.0

    @staticmethod
    def delta(values):
        if len(values) < 2:
            return 0.0
        return values[-1] - values[0]