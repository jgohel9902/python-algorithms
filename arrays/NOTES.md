# Arrays

## Two Sum
- **Approach:** Hash map to store complement lookup
- **Time:** O(n) — single pass
- **Space:** O(n) — hash map storage
- **Key insight:** For each number, check if `target - num` was already seen

## Best Time to Buy and Sell Stock
- **Approach:** Single pass, track min price and max profit
- **Time:** O(n) — one iteration
- **Space:** O(1) — no extra data structures
- **Key insight:** At each price, ask "is this the lowest I've seen?" and "is selling here the best profit?"

## Contains Duplicate
- **Approach:** Hash set to track seen numbers
- **Time:** O(n) — single pass
- **Space:** O(n) — set storage
- **Key insight:** If a number is already in the set, we found a duplicate immediately