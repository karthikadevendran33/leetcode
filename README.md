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


