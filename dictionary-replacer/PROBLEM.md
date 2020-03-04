# String Replacement Dictionary
#### Time-limit : 5-10 minutes

> `int printf ( const char * format, ... )`
> 
> **Print formatted data to `stdout`**
>
> Writes the C string pointed by *format* to the standard output.
> If *format* includes *format specifiers* (sub-sequences beginning with `%`), the additional arguments following *format* are formatted and inserted in the resulting string replacing their respective specifiers.
>
> [`printf()` Documentation (cplusplus.com)](https://cplusplus.com/reference/cstdio/printf/)

## Minimum Condition
Most languages have some implementation of the `printf` (or similarly capable function).
Given a particular string, this function is capable of producing dynamic replacements based on external values.

The challenge is to implement a simple string replacement function/method which can update a string's values based on a lookup dictionary.
Values to be replaced will be surrounded by angle brackets in the original string.
For example, given the lookup dictionary `{ 'friend_name' : 'Dave' } `, the string `'Hello, <friend_name>!'` would be replaced with `'Hello, Dave!'`.


## Implementations
- [python3](./python3)
