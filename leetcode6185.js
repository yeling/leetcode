/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} players
 * @param {number[]} trainers
 * @return {number}
 */
var matchPlayersAndTrainers = function(players, trainers) {
    players.sort((a,b) => a - b);
    trainers.sort((a,b) => a - b);
    let sum = 0;
    for(let i = 0, j = 0; i < players.length && j < trainers.length;) {
        if(players[i] <= trainers[j]) {
            sum++;
            i++;
            j++;
        } else {
            j++;
        }
    }
    return sum;
};

players = [4,7,9], trainers = [8,2,5,8]
players = [1,1,1], trainers = [10]
console.log(matchPlayersAndTrainers(players,trainers));