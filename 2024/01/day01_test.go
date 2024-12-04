package main

import (
	"slices"
	"strings"
	"testing"
)

func TestGetLists(t *testing.T) {
	// Arrange
	testList := `1   2
4   3
5   6`
	testReader := strings.NewReader(testList)

	wantLeft := []int{1, 4, 5}
	wantRight := []int{2, 3, 6}

	// Act
	gotLeft, gotRight := GetLists(testReader)

	// Assert
	if !slices.Equal(gotLeft, wantLeft) {
		t.Errorf("Mismatched left list: got %v, want %v", gotLeft, wantLeft)
	}
	if !slices.Equal(gotRight, wantRight) {
		t.Errorf("Mismatched right list: got %v, want %v", gotRight, wantRight)
	}
}
