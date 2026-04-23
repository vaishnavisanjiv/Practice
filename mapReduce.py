log_data = [
    "INFO User logged in",
    "ERROR File not found",
    "WARNING Low memory",
    "ERROR Timeout",
    "INFO Request processed"
]

mapped = []
for line in log_data:
    log_type = line.split()[0]
    mapped.append((log_type, 1))

print("Mapped:", mapped)

result = {}

for key, value in mapped:
    result[key] = result.get(key, 0) + value

print("Reduced Output:", result)