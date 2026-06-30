import json

from benchmark_metrics import BenchmarkMetrics

metrics = BenchmarkMetrics().summarize()

print(json.dumps(metrics, indent=4))

with open(
    "reports/benchmark-summary.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(metrics, f, indent=4)
