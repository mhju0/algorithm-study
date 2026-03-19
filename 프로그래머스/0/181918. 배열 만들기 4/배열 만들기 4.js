function solution(arr) {
    const stk = [];
    let i = 0;
    while (i < arr.length){
        if (stk.length === 0) {
            stk.push(arr[i]);
            i++;
        }else if (stk.length !== 0 && stk.slice(-1) < arr[i]){
            stk.push(arr[i]);
            i++;
        }else if (stk.length !== 0 && stk.slice(-1) >= arr[i]){
            stk.pop();
        }
    }
    return stk
    
}