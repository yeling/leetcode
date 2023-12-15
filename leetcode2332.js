/*
* auther yeling
* 2332. 坐上公交的最晚时间
* 找出最后一辆有座位的BUS，坐上去，记录每辆公交的乘客
*/
//38 / 63
//56 / 63
var latestTimeCatchTheBus = function(buses, passengers, capacity) {
    buses.sort((a,b) => {
        return a - b;
    })
    passengers.sort((a,b)=> {
        return a -b;
    })
    console.log(buses);
    console.log(passengers);
    let i = 0, j = 0, ret = 0 ,ca = 0;
    while(i < buses.length ) {
        //还有乘客
        if(j < passengers.length) {
            if(passengers[j] <= buses[i]) {
                if(j > 0 && passengers[j] - passengers[j -1] > 1) {
                    ret = passengers[j] - 1;
                } else if(j == 0) {
                    ret = passengers[j] - 1;
                }
                j++;
                ca++;
                if(ca == capacity) {
                    i++;
                    ca = 0;
                }
            } else {
                if(j > 0 && buses[i] - passengers[j -1] > 0) {
                    ret = buses[i];
                } else if(j == 0) {
                    ret = buses[i];
                }
                i++;
                ca = 0;
            }
        } else {
            //没有乘客
            if(passengers[passengers.length - 1] != buses[i]) {
                ret = buses[i];
            }
            i++;
        }
    }
    return ret;
};

buses = [20,10], passengers = [2,17,18,19,21], capacity = 3
passengers = [2,19,20,22]

buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2

buses = [2], passengers = [2], capacity = 2

console.log(`${buses} ${passengers} ${capacity}`)

console.log(`${latestTimeCatchTheBus(buses,passengers,capacity)}`)
