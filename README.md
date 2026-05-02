# The Affine Cipher

This cipher works similarly to the Caesar Shift Cipher. However, instead of just using modular addition, we now move to multiplicative addition. Let's start by taking our alphabet group:

$$\mathbb{A} = {a,b,c,...,x,y,z}$$

and it's corresponding modular space:

$$\mathbb{Z}_{26} = {0,1,2,...,23,24,25}$$

Instead of just one integer in the modular space, the affine key will take two numbers: $\alpha$ and $\beta$. We will perform modular multiplication with $\alpha$ whereas $\beta$ will be modular addition. Then, if we have a message 'p', our encrypted affine cipher will be $c \equiv \alpha * x + \beta$ (mod 26). Note, if we chose $\alpha = 1$, we just have a simple Caesar Shift cipher.

However, before we can encrypt our first message, there are some important restrictions that we need to discuss when choosing $`\alpha \in ℤ_{26}`$. You may recall in the Caesar cipher that in order to decrypt our message, we needed an inverse to our key. In modular addition, an inverse b to a would satisfy a + b = 0. However, in modular multiplication, the inverse b to a would need to satisfy a * b = 1. Since we're using modular arithmetic, this really means $a * b \equiv 1$ (mod 26). That is, if we were to divide a*b by 26, we could get remainder 1. 

Suppose we chose $\alpha = 2$ as our affine key. How would we decrypt this? Is there any number that can be multiplied to 2 so that when you divide by 26, you get remainder 1? If we multiply 2 by every number up to 12, we get {0,2,4,6,...,20,22,24}. Once we get to 13, we get back to 0. This list comprises every possible remainder of 2*x/26 for any integer x, and is called a subgroup of $ℤ_{26}$. Note that 1 is nowhere to be found. Thus 2 has no inverse and cannot be a valid affine key. It is for this same reason, that we say $ℤ_{26}$ is not a true group under multiplication as not every element has an inverse.

The question now becomes: which integers are valid keys? Since we've shown 2 to be invalid, we can start by throwing out all the even numbers, including 0. Recall that 2*13 = 0. This means that 13 does not have a valid inverse either. In general, if a*b = 0, then neither a nor b are invertible. This leaves us with $ℤ^{*}_{26}$={1,3,5,7,9,11,15,17,19,21,23,25}. Can you spot what makes these integers unique? 

Answer: for all x in $ℤ^{*}_{26}$, gcd(26, x) = 1.

Here's a challenge, which numbers would be valid if we only have 10 characters?

## How the program works:
1. User is asked for two keys: alpha and beta, which are the multiplicative and additive keys respectively.
2. The program ensures that the alpha given is a valid key with an inverse. If not, the user is asked to chose a different key.
3. The user is asked whether they want to encrypt or decrypt.
