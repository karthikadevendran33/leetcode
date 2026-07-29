# leetcode
# LeetCode Solutions

This repository contains my solutions to LeetCode problems. It serves as a record of my learning journey and consistent practice in Data Structures and Algorithms.

## Objectives

- Improve problem-solving skills.
- Strengthen understanding of Data Structures and Algorithms.
- Write clean and efficient code.
- Prepare for coding interviews through consistent practice.

## Language

- Python

## Notes

Each solution is written with a focus on readability and correctness. As I continue solving problems, this repository will be updated with new solutions and, where applicable, more optimized approaches.

Day 2 - Palindrome Number
## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome number is a number that reads the same forward and backward.

## Approach

The solution uses a mathematical approach to reverse the given integer without converting it into a string.

### Algorithm

1. Store the original value of `x`.
2. Extract each digit from the number using the modulo operator (`%`).
3. Build the reversed number by multiplying the current reverse value by 10 and adding the extracted digit.
4. Compare the reversed number with the original number.
5. Return `true` if both values are equal; otherwise, return `false`.

Day 3 - Roman To Intege
## Problem

This program converts a Roman numeral into its corresponding integer value.

The idea is simple:

1. Store the value of each Roman symbol in a dictionary.
2. Check each character in the string one by one.
3. If a smaller value comes before a larger value, subtract it.
4. Otherwise, add the value.
5. Return the final answer.

## Complexity

**Time Complexity:** O(n)  
- We go through the Roman numeral once.

**Space Complexity:** O(1)  
- The dictionary contains only a fixed number of symbols.

Day 4 - Longest Common Prefix
## Problem
Find the longest common prefix string among an array of strings.  
Return `""` if no common prefix exists.


## Approach
- Compare characters of the first string with all other strings.
- Stop when a mismatch is found.
- Return the matched prefix.

## Complexity

- Time Complexity: `O(n * m)`
- Space Complexity: `O(1)`

## Language
Python 3

Day 5 - Valid Parentheses
## Problem
Given a string containing only the characters `(`, `)`, `{`, `}`, `[` and `]`, check whether the brackets are valid.

A string is valid when:

- Every opening bracket has a matching closing bracket.
- Brackets are closed in the correct order.
- Each closing bracket matches the same type of opening bracket.

## Approach
I used a **stack** to solve this problem.

- When I find an opening bracket, I store it in the stack.
- When I find a closing bracket, I check the last bracket in the stack.
- If the brackets match, I remove it from the stack.
- If they do not match, the string is invalid.
- At the end, the stack should be empty for a valid string.

Day 6 - Merge Two Sorted List

# Merge Two Sorted Lists
## Problem 

Given the heads of two sorted linked lists, merge them into a single sorted linked list and return its head.

## Approach

The solution uses an **iterative method** with a **dummy node**.

1. Create a dummy node to act as the starting point.
2. Compare the current nodes of both linked lists.
3. Attach the smaller node to the merged list.
4. Move the corresponding pointer forward.
5. Continue until one list becomes empty.
6. Attach the remaining nodes from the other list.

## Time Complexity

- **Time:** O(n + m)
- **Space:** O(1)

where:
- `n` = number of nodes in the first list
- `m` = number of nodes in the second list

Day 7 - Remove Duplicates from Sorted Array

##Problem
Given a sorted integer array `nums`, remove the duplicate elements **in-place** such that each unique element appears only once. The relative order of the elements must remain unchanged.Return the number of unique elements (`k`). After the function executes, the first `k` positions of the array should contain the unique elements in sorted order.

## How It Works

- A pointer named `pos` keeps track of the position where the next unique element should be stored.
- Traverse the array using a loop.
- Compare the current element with the element at the `pos` index.
- When a new unique element is found:
  - Increment `pos`.
  - Copy the unique element to `nums[pos]`.
- After completing the traversal, the first `pos + 1` elements contain all unique values.

## Algorithm

1. Initialize `pos` to `0`.
2. Iterate through the array from the first element to the last.
3. Compare the current element with `nums[pos]`.
4. If they are different:
   - Increment `pos`.
   - Store the current element at `nums[pos]`.
5. Return `pos + 1`, which represents the number of unique elements.

Day 8 - Remove Duplicate Sorted array

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** so that each unique element appears only once.

The relative order of the elements should remain the same.

Return the number of unique elements `k`. The first `k` elements of `nums` should contain the unique values in sorted order. The remaining elements can be ignored.

## Approach: Two Pointer Technique

This solution uses the **two-pointer approach**.
- `read` pointer is used to scan through the entire array.
- `write` pointer keeps track of the position where the next unique element should be placed.

Since the array is already sorted:
- Duplicate elements will always be next to each other.
- We only need to compare the current element with the previous element.
- When a new unique element is found, it is placed at the `write` position.
## Key Concepts

- Arrays
- Two Pointer Technique
- In-place Modification
- Sorted Array Traversal

Day 9 - Remove Element

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` from `nums` **in-place**.
The order of the remaining elements may be changed.
Return the number of elements `k` that are not equal to `val`.
After removing the elements:
- The first `k` elements of `nums` should contain the values that are not equal to `val`.
- The remaining elements of the array do not matter.

## Approach

This solution uses an additional list to store the elements that should remain.

### Steps:
1. Create an empty list called `answer`.
2. Traverse through the original array.
3. Add only the elements that are different from `val` into `answer`.
4. Copy the elements from `answer` back into the original `nums` array.
5. Return the length of `answer`, which represents the number of remaining elements.
