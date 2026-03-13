function solution(a, b) {
    var answer = 0;
    let aPlusb = a.toString() + b.toString();
    let bPlusa = b.toString() + a.toString();
    if (aPlusb < bPlusa){
        return Number(bPlusa);
    }else{
        return Number(aPlusb);
    }
}