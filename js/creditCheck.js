exports.creditCheck = function(param) {

    accountIdentifier = param.split('');    // Split the string into an array of numbers
    summedDigitsOverTen = [];
    count = 0;

    // Loops through array. Every other number is doubled. If the doubled number is a double digit,
    // replace it with the sum of its digits instead. push all of those numbers to a new array:
    // summedDigitsOverTen.
    for(let n of accountIdentifier) {
        if(count%2 == 0){
            if(String(((+n)*2)).length > 1) {
                let num = String(((+n)*2));
                summedDigitsOverTen.push(+num[0]+ +num[1]);
             } else {
                 summedDigitsOverTen.push(+n*2);
             }
        } else {
            summedDigitsOverTen.push(+n);
        }
        count++;
    }

    // Using the reduce, we can get the sum of all of the numbers in the array
    let sum = summedDigitsOverTen.reduce((agg, num) => agg + num);

    if(sum%10 == 0) {
        return "The number is valid!"
    } else {
        return "The number is invalid!"
    }
}