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
