exports.creditCheck = function(param) {

    accountIdentifier = param.split('');
    summedDigitsOverTen = [];
    count = 0;
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

    let sum = summedDigitsOverTen.reduce((agg, num) => agg + num);

    if(sum%10 == 0) {
        return "The number is valid!"
    } else {
        return "The number is invalid!"
    }
}

// console.log(exports.creditCheck('5541808923795240'));