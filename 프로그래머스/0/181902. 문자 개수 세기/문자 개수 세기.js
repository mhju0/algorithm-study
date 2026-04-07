function solution(my_string) {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    
    const result = new Array(52).fill(0);
    
    my_string.split("").forEach((char)=> {
        const index = alphabet.indexOf(char);
        
        if (index !== -1){
            result[index] += 1;
        }
    });
    
    return result
}