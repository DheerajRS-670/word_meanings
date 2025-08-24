This program finds out the combined single digit number representing
 a given word. Each word has a meaning, and this program helps identify the
 meaning of a word. The meaning of the word can be identified by reducing the word
 to a single digit number (may be multiple digits later) which has a specific
 meaning

Below are the meanings of single digit numbers that I have identified based on classification
 of words:

```
1: soul
2: separate
3: how nature works
4: incomplete
5: nature, satisfaction, mind
6: challenge, intensify, realize
7: unending, learn, detect, innovate, inspire
8: complete
9: dark, immature, death
```

In the program two types of values are given to the alphabets for identifying the class of words:

    1. Normal allocation ('a' -> 1, 'b' -> 2, 'c' -> 3 and so on)
    2. Chaldean system of allocation of numbers

Some good things to know:
    1. There are nearly the same number of words of each "type" in the english dictionary

```bash
$ pwd
/word_meanings/arranged/chaldean
$ for file in *
> do
> echo "${file} -> `cat ${file} | wc -l`"
> done
1.txt ->     8076
2.txt ->     8215
3.txt ->     8080
4.txt ->     8043
5.txt ->     8065
6.txt ->     8167
7.txt ->     8056
8.txt ->     8028
9.txt ->     8048
```

    2. Mathematically too, it is possible to classify numbers:

        For example, the number 1 will always maintain the uniqueness of a person. When you multiply
         any number with 1, you will get the same number as the result

        When a number is multiplied with 9, and the digits of the result are added together,
         it will always sum to 9
    
However, we don't notice this even distribution when checking with words starting with specific letters though:

```bash
$ cat words | grep -i "^a.*$" | wc -l
    5895
$ cat words | grep -i "^b.*$" | wc -l
    6068
$ cat words | grep -i "^c.*$" | wc -l
    9521
$ cat words | grep -i "^d.*$" | wc -l
    5823
$ cat words | grep -i "^z.*$" | wc -l
     281
$ cat words | grep -i "^y.*$" | wc -l
     421
$ cat words | grep -i "^x.*$" | wc -l
      53
$ cat words | grep -i "^n.*$" | wc -l
    2018
```
