//生成随机数据
let size = 100;
let n = Math.floor(Math.random() * size);
console.log(n);
let nums = []
for(let i = 0; i < n; i++) {
    nums.push(i + 1);
}
for(let i = 0; i < n; i++) {
    let ran = Math.floor(Math.random() * n);
    let temp = nums[0];
    nums[0] = nums[ran];
    nums[ran] = temp;
}
console.log(nums.join(' '));

