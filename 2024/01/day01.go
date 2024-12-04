package main

import (
	"bufio"
	"fmt"
	"io"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func GetLists(r io.Reader) (left, right []int) {
	left = make([]int, 0)
	right = make([]int, 0)

	scanner := bufio.NewScanner(r)

	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		leftInt, err := strconv.Atoi(fields[0])
		if err != nil {
			fmt.Printf("Error parsing %s as int", fields[0])
		}
		left = append(left, leftInt)

		rightInt, err := strconv.Atoi(fields[1])
		if err != nil {
			fmt.Printf("Error parsing %s as int", fields[1])
		}
		right = append(right, rightInt)
	}

	return left, right
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error reading file")
	}
	defer file.Close()

	left, right := GetLists(file)
	_sortFunc := func(a, b int) int { return a - b }
	slices.SortFunc(left, _sortFunc)
	slices.SortFunc(right, _sortFunc)

	dst := 0
	sim := 0
	appearances := make(map[int]int)
	for i, vl := range left {
		dst += int(math.Abs(float64(left[i] - right[i])))

		if _, ok := appearances[vl]; !ok {
			for _, vr := range right {
				if vl == vr {
					appearances[vl] += 1
				}
			}
		}

		sim += vl * appearances[vl]
	}

	fmt.Printf("Distance: %v\n", dst)
	fmt.Printf("Similarity: %v", sim)
}
