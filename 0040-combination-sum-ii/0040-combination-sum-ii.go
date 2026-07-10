import "sort"

func combinationSum2(c []int,t int)(r [][]int){
	sort.Ints(c)
	var p []int
	var f func(int,int)
	f=func(i,s int){
		if s==0{r=append(r,append([]int{},p...));return}
		for j:=i;j<len(c)&&c[j]<=s;j++{
			if j>i&&c[j]==c[j-1]{continue}
			p=append(p,c[j])
			f(j+1,s-c[j])
			p=p[:len(p)-1]
		}
	}
	f(0,t)
	return
}