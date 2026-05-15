# ==========================================================
# PYTHON STRING SLICING (EASY VERSION FOR BEGINNERS)
# ==========================================================
# Bhai simple samajh:
# String slicing ka matlab hota hai string ke andar se
# kuch part nikalna using index (position)

# Syntax:
# string[start : end]
# IMPORTANT: end wala index include nahi hota

# ==========================================================
# BASIC EXAMPLE
# ==========================================================

text = "GulabJamun"

print(text[0:5])
# 0 se start hoga, 5th index tak jayega BUT 5 include nahi hoga
# Output: Gulab

print(text[:9])
# start empty hai => matlab 0 se start karo
# Output: GulabJamu

print(text[5:])
# end empty hai => matlab last tak jao
# Output: Jamun

print(text[5:10])
# 5 se start, 10 tak (but 10 include nahi hoga)
# Output: Jamun


# ==========================================================
# PRACTICE QUESTION (REAL USE CASE)
# ==========================================================
# User se favourite food input lo
# aur uska:
# 1. Middle 3 characters
# 2. Last 2 characters print karo

food = input("Enter your favourite food name: ")

# -------------------------
# STEP 1: Middle 3 characters
# -------------------------

length = len(food)
# len() ka matlab hota hai string ki total length (kitne letters hain)

mid = length // 2
# middle index nikal rahe hain
# // ka matlab integer division (decimal ignore)

print(food[mid - 1 : mid + 2])
#  middle se 1 left, middle, aur 1 right = total 3 characters


# -------------------------
# STEP 2: Last 2 characters
# -------------------------

print(food[-2:])
# -2 ka matlab last se 2 characters
# Python me negative index ka matlab end se count karna hota hai

# Example:
# food = "milkcake"
# Output: ke