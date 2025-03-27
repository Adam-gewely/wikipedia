"".join([requests.get(v).text for v in [f"https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_{i}" for i in range(8)]])
