
## Min Stack
- **Approach:** each stack entry stores (value, min so far), so the minimum is read from the top entry.
- **Time:** O(1) for push, pop, top and get_min.
- **Space:** O(n), one extra int per element.
- **Key insight:** the minimum only changes when you push or pop, so cache it per entry instead of scanning.