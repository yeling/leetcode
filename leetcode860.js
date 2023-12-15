/*
*860. 柠檬水找零
*
*/
/**
 * @param {number[]} bills
 * @return {boolean}
 */

var lemonadeChange = function(bills) {
    let five = 0, ten = 0;
    for(let i = 0; i < bills.length; i++) {
        if(bills[i] == 5) {
            five++;
        }else if(bills[i] == 10) {
            if(five >= 1) {
                five--;
                ten++;
            } else {
                return false;
            }
        } else if(bills[i] == 20) {
            let left = 15;
            if(ten >= 1) {
                ten--;
                left-=10;
            }
            if(left == 15 && five >= 3) {
                five-=3;
                left = 0;
            } else if(left == 5 && five >= 1) {
                five--;
                left = 0;
            } else {
                return false;
            }
        }
    }
    return true;

};

let bills = [5,5,5,10,20];
bills = [5,5,10,10,20];
console.log(bills);
console.log(lemonadeChange(bills));

