import requests

shards = [
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_0",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_1",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_2",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_3",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_4",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_5",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_6",
    "https://raw.githubusercontent.com/Adam-gewely/wikipedia/refs/heads/main/shard_7",
]


def get_wikipedia(verbose: bool = False) -> str:
    _shards = []

    if verbose:
        print("Downloading shards...")

    for i, v in enumerate(shards):
        if verbose:
            print(f"{i + 1}/8 shards downloading...")

        _shards.append(requests.get(v).text)

    if verbose:
        print("Joining shards...")

    return "".join(_shards)
