package main;
/*
* auther yeling
* 
* 
*/
import (
	"fmt"
)

//TLE 78 / 87 个通过的测试用例
func sumSubarrayMins2(arr []int) int {
	var MOD int = 1e9 + 7
	sum := 0
	min := 0
	for i, item := range arr{
		min = item;
		for j := i; j < len(arr); j++ {
			if min > arr[j] {
				min = arr[j]
			}
			//fmt.Printf("min %d sum %d\n", min, sum);
			sum =  (sum + min)%MOD
		}
	}
	return sum
}

func sumSubarrayMins(arr []int) int {
	var MOD int = 1e9 + 7
	sum := 0
	min := 0
	for i, item := range arr{
		min = item;
		for j := i; j < len(arr); j++ {
			if min > arr[j] {
				min = arr[j]
			}
			fmt.Printf("min %d sum %d\n", min, sum);
			sum =  (sum + min)%MOD
		}
	}
	return sum
}

func main() {
	nums := []int{3,1,2,4}
	// nums = []int{11,81,94,43,3}
	ret := sumSubarrayMins(nums)
	fmt.Printf("ret %d\n", ret)
}
