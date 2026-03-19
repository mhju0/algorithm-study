function solution(a, b, c, d) {
  const counts = {};
  for (const n of [a, b, c, d]) {
    counts[n] = (counts[n] || 0) + 1;
  }

  const size = new Set([a, b, c, d]).size;
  const diceVals = Object.values(counts);
  const diceKeys = Object.keys(counts).map(Number);

  if (size === 1) {
    return 1111 * a;
  }
  if (size === 4) {
    return Math.min(a, b, c, d);
  }
  if (size === 2 && diceVals.includes(3)) {
    const p = diceKeys.find((x) => counts[x] === 3);
    const q = diceKeys.find((x) => counts[x] === 1);
    return (10 * p + q) ** 2;
  }
  if (size === 2) {
    const [p, q] = diceKeys.filter((x) => counts[x] === 2);
    return (p + q) * Math.abs(p - q);
  }

  if (size === 3) {
    const p = diceKeys.find((x) => counts[x] === 2);
    const [q, r] = diceKeys.filter((x) => counts[x] === 1);
    return q * r;
  }
}