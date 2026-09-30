"""
KV Cache Memory Budget (easy) · patterns: capacity-math, memory-estimate

While a transformer generates text, it keeps a key vector and a value vector
for every earlier token, in every layer and every key-value head, so that
each new token does not have to recompute them. Given the number of layers,
key-value heads, the size of each head, the number of cached tokens, the
batch size and the bytes per stored number, return the memory the cache
needs in MiB (2^20 bytes). Serving capacity is planned from exactly this
number, since it grows with every token of every conversation in the batch.

Examples:

    Input:  layers = 32, kv_heads = 32, head_dim = 128, tokens = 4096, batch = 1, 2 bytes per number
    Output: 2048.0
    Why:    512 KiB per token, times 4,096 tokens

    Input:  layers = 32, kv_heads = 8, head_dim = 128, tokens = 4096, batch = 1, 2 bytes per number
    Output: 512.0
    Why:    sharing each key-value head across 4 query heads cuts the cache by 4

    Input:  layers = 32, kv_heads = 8, head_dim = 128, tokens = 0
    Output: 0.0
    Why:    edge case, an empty prompt has nothing cached yet

Approach:
    Each cached token costs one key and one value per layer and per
    key-value head, each of head_dim numbers, so the per-token cost is 2 ×
    layers × kv_heads × head_dim × bytes, and the whole cache is that times
    the tokens and the batch. The formula makes the usual levers visible:
    fewer key-value heads, as in grouped-query attention, cut it
    proportionally, a smaller number format such as 8-bit halves it again,
    and a bigger batch or a longer context multiplies it. That is why long
    contexts are limited by memory before they are limited by compute. Time
    and space are O(1).

The lesson behind it: The KV Cache
    https://bytepatterns.com/learn/ai-ml/the-kv-cache
    python ai-ml/24-the-kv-cache.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/kv-cache-memory-budget

Run it:  python problems/ai-ml/02-kv-cache-memory-budget.py
"""


def kv_cache_mib(layers, kv_heads, head_dim, tokens, batch=1, bytes_per_value=2):
    per_token = 2 * layers * kv_heads * head_dim * bytes_per_value   # one key and one value
    return per_token * tokens * batch / 2 ** 20


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(kv_cache_mib(32, 32, 128, 4096), 2048.0)
    check(kv_cache_mib(32, 8, 128, 4096), 512.0)
    check(kv_cache_mib(32, 8, 128, 0), 0.0)
    check(kv_cache_mib(32, 8, 128, 4096, batch=16, bytes_per_value=1), 4096.0)
