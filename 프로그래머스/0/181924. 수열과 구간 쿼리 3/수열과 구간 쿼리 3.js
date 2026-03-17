function solution(arr, queries) {
    for (const n of queries){
        [arr[n[1]], arr[n[0]]] = [arr[n[0]], arr[n[1]]];
    }
    return arr
}