function solution(my_string, queries) {
    let newStr = my_string
    for (const [n,m] of queries){
        const str1 = my_string.slice(n,m+1).split('').reverse().join("")
        newStr = my_string.slice(0,n) + str1 + my_string.slice(m+1,)
        my_string = newStr
    }
    return newStr
}