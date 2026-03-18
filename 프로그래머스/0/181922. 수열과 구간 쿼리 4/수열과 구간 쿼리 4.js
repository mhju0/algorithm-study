function solution(arr, queries) {
    for (const [s,e,k] of queries){
        for (i=s; i<=e; i++){
            if (i % k === 0 || k === 0){
                arr[i] = arr[i] +1;
            }
        }
    }
    return arr
}