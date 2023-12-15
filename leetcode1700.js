/*
* auther yeling
* 
* 
*/

/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    let find = true;
    while(find) {
        find = false;
        let count = students.length;
        while(count > 0&& students.length > 0 && sandwiches.length > 0) {
            if(students[0] == sandwiches[0]) {
                find = true;
                students.shift();
                sandwiches.shift();
            } else {
                let head = students.shift();
                students.push(head);
            }
            count--;
        }
    }
    return students.length;
};

students = [1,1,0,0], sandwiches = [0,1,0,1];
students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1];

console.log(countStudents(students, sandwiches));

