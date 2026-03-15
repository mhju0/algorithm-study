function solution(a, b, c) {
    let mySet = new Set([a,b,c]);
    if (mySet.size === 1){
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3);
    }else if (mySet.size === 2){
        return (a+b+c)*(a**2+b**2+c**2);
    }else{
        return (a+b+c);
    }
}