package main;
/*
* auther yeling
* 
* 
*/
import "fmt";

func arraySign(nums []int) int {
	isAdd := true;
	//for i := 0; i < len(nums); i++ {
	for _, item := range nums{
		if(item < 0) {
			isAdd = !isAdd;
		} else if(item == 0) {
			return 0;
			break;
		}
	}
	if(isAdd) {
		return 1;
	} else {
		return -1;
	}
}

func main() {
	nums := []int{-1,-2,3}
	ret := arraySign(nums)
	fmt.Printf("ret %d\n", ret);
}
