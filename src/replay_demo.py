from replay_verifier import ReplayVerifier
import json

with open("reports/SIL-001-report.json") as f:
    run1 = json.load(f)

with open("reports/SIL-001-report.json") as f:
    run2 = json.load(f)

result = ReplayVerifier().verify(run1, run2)

print()

print("Replay Verification")

print("-------------------")

print(result)
