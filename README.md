#Farm
----------------------



##Introduction

[Website](http://farmlang.herokuapp.com/)

The Farm language is a minimal syntax language that uses a series of commands to assemble patterns of characters to form an output. These commands, can also be looped. Overall, Farm only has 8 symbols it uses to compute everything!

Farm can be considered a pseudo-low level language. The compiler is written in Python, so the output isn't truly close to machine language instruction, but the massive freedom in syntax and structure gives it the utility of a low level language.

The language uses two containers, one for alphabet characters, the other for numeric and symbolic characters. There are two pointers, which can reference values from these containers, which are 0 indexed. The alphabet container is intially set to `a`, while the num_sym(numerical and symbolic) container is set to `0`.

##Commands

The command symbols in Farm have one of three roles:

> Move either of the pointers across the container:

 The `<` and `>` commands move the alphabet pointer back one index, or forward one index respectively. The `-` and `+` commands move the num_sym container back one index or forward one index, respectively.

> Add the current value the pointer is set on to the output expression:

The `,` command prints out the value the alphabet pointer is set on. The `.` command prints out the value the num_sym pointer is currently set on.

> To loop back across previous commands:

The `!x` command, where x is an integer between and including 1 to 9, repeats the previous x commands in the code. If a `!` is directly followed by anything except an integer 1-9, it will be ignored. You cannot repeat more than 9 previous commands. `!15` will only repeat one previous command, not 15.

The `?xy` command, where both x and y are integers between and including 1 through 9, repeats the previous x commands in the code, in y cycles. This is essentially a very shorthand way of repeating the `!x` command over again several times. Similarly, if anything in the x or y position is not an integer 1-9, the `?` command is ignored.

Additionally, anything not one of these command symbols is ignored by the compiler, and considered a comment, as Farm code can be easily annotated this way. This also gives the language very easily manipulatable syntax, as new lines or tabs do not affect the code.

####Infinite Lists

The containers in Farm for both the alphabet and num_sym sets are housed in objects called infinite lists. Essentially, they prevent errors by always doing the following:

* If backward commands cause a negative index on the container, it simply returns the 0 index.

```
>,<<<,

ba
```
Here, even though the 3 `<` commands push the pointer to a -2 index, the compiler corrects that and resets the index to 0 again, printing the `a` character.

* If forward commands cause an index greater than the size of the list, the index is set to the remainder of the size of the list, so it restarts at the beginning again.

```
>>>>>>>>>>>>>>>>>>>>>>>>>>,>,
ab
```
In this Farm program, we input 26 forward commands on the alphabet pointer. Technically, the alphabet container ends at index 25 with the value `z`. However, if the index is greater, the index is divided by the length of the list, and the remainder of that is reset as the index, which puts it back at 0. This is particularly useful because if one wanted to print the word `pizza`, after printing z, one can just go one index forward to print the a, instead of going 25 commands back to print a.

##Examples

Let's try printing a simple word, like `bat`:

```
>,<,>>>>>>>>>>>>>>>>>>>,
bat
```
Now, that is an awful lot of forward commands we used. We can shorten those with looping commands:

```
>,<,>>>>>>>>>>!9,
bat
```
So we shortened our expression, but it's still a bit long and easy to lose track of how many commands there are. We can further shorten our expression by used the `?` loop.

```
>,<,>>>?28,
bat
```
Here, the `?` loop is used to repeat the expression `>>` 8 times, for a total of 16 `>` commands. Let's try printing a number now, like 6500.

```
++++++.-.-----..
6500
```
Just like before, we can shorten our expression with loops:

```
+?15.-.-?13..
6500
```
Now, lets try assembling some code in a different programming language! In this example, the Farm program will print `var x = 5`. The program will be spaced out and annotated to make it more readable.

```
>>>?29,>?15,<<<<<!5,++?24.>>>!3,.+++++?37.-----?37.---!2.

var x = 5

```

`>>>?29,` sets the alpha pointer at index 23, and prints v.

`>?15,`sets the alpha pointer 6 indexes forward, and prints a into the expression.

`<<<<<!5,` moves the alpha pointer back 10 indexes and prints r.

`++?24.` now, this expression moves the num_sym pointer 10 indexes up to print the white space character.

`>>>!3,` moves the alpha pointer 6 spaces up to print x.

`.` simply prints another space character. No movements are neccesary since the pointer is already set on the space.

`+++++?37.` moves the num_sym pointer up many indexes to reach the equals character and prints it.

`-----?37.` moves the num_sym pointer backwards the same number of indexes to print another space character.

`--!2.` The final command prints a 5, and the program ends.
