/*
* auther yeling
* 
* 
*/

/**
 * @param {number} initialEnergy
 * @param {number} initialExperience
 * @param {number[]} energy
 * @param {number[]} experience
 * @return {number}
 */
var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
    let n = energy.length;
    let needEnergy = 0;
    let needExper = 0;
    let currEnergy = initialEnergy;
    let currExper = initialExperience;
    for(let i = 0; i < n; i++) {
        if(currEnergy <= energy[i]) {
            needEnergy += energy[i] + 1 - currEnergy; 
            currEnergy = energy[i] + 1;
        }
        currEnergy = currEnergy - energy[i];
        if(currExper <= experience[i]) {
            needExper += experience[i] + 1 - currExper;
            currExper = experience[i] + 1;
        }
        currExper = currExper + experience[i];
    }
    return needEnergy + needExper;
};


initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]
initialEnergy = 5, initialExperience = 3, energy = [1,4], experience = [2,5]

console.log(minNumberOfHours(initialEnergy,initialExperience,energy,experience));

