function solution(arr, queries) {
  let answer = [];
  for (const [a, b, c] of queries) {
    let biggerThanK = [];
    for (let i = a; i <= b; i++) {
      if (arr[i] > c) {
        biggerThanK = biggerThanK.concat(arr[i]);
      }
    }
    if (biggerThanK.length > 0) {
      answer = answer.concat(Math.min(...biggerThanK));
    } else {
      answer = answer.concat(-1);
    }
  }
  return answer;
}