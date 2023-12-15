package main;
/*
* auther yeling
* 
* 
*/
import "fmt";

func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	sum := 0;
	index := 0;
	switch ruleKey {
	case "type":
		index = 0
	case "color":
		index = 1
	case "name":
		index = 2;
	}
	for _,item := range items {
		if item[index] == ruleValue {
			sum++
		}
	}
	return sum
}

var d = map[string]int{"type": 0, "color": 1, "name": 2}

func countMatches2(items [][]string, ruleKey, ruleValue string) (ans int) {
    index := d[ruleKey]
    for _, item := range items {
        if item[index] == ruleValue {
            ans++
        }
    }
    return
}


func main() {
	fmt.Printf("ret %d\n", 10)
}
