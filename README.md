# Binscript
*A simple scriptting language for buffer overflow exploitation*

# Why?
While doing stuff like buffer overflow, I find myself in python terminal, translating strings to hexedecimal, creating long strings
and all of that. So I decided to create an simple scriptting language for this kind of stuff.

Don't get me wrong, this scriptting language is kinda hard to use but it was simple to create it. So you may be better off with the
python.

# Install
```
pip install -U https://github.com/ngn13/binscript/archive/refs/heads/main.zip
```

# Usage
To get an interactive prompt, just run: `binscript`. To run a file, run: `binscript FILENAME_HERE`
Here is all the instructions that you can use:

##### `ext`
Exit, example usage:
```
bsc >>> ext
(Program exits)
```

##### `out`
Print something out, example usage:
```
bsc >>> out.Hello world!
Hello world!
```
To toggle (disable/enable) the output of other instructions, run:
```
bsc >>> out.!
(No output)
```
By default its enabled.

##### `hts`
Hex-to-string, example usage:
```
bsc >>> hts.0x41
A
```

##### `sth`
String-to-hex, example usage:
```
bsc >>> sth.A
0x41
```

##### `stx`
Do string times X, example usage:
```
bsc >>> stx.A.20
AAAAAAAAAAAAAAAAAAAA
```

##### `add`
Add two hex values, example usage:
```
bsc >>> add.0x12.0xF
0x21
```

##### `sub`
Subtract two hex values, example usage:
```
bsc >>> sub.0xF.0xA
0x5
```

##### `cmb`
Combine stuff, example usage:
```
bsc >>> cmb.AAAAAAA.EEEEEEEE
AAAAAAAEEEEEEEE
```

##### `set`
Set a variable, example usage:
```
bsc >>> set.ch.A
(No output)
```
To use the variable, add "$" before an argument:
```
bsc >>> out.$ch
A
```
You can get output of the previous instruction with the "pre" variable,
whihc is setted by the parser:
```
bsc >>> hts.0x41
A
bsc >>> out.$pre
A
```

## Example
Here's a "simple" example, lines starting with `!` are comments and they won't be parsed.
```
! Disable the ouput
out.!

! Set "chr" to "A"
set.chr.A

! Do "chr" variable times 20
stx.$chr.10

! Store the output of previous instruction in "lots_of_chr"
set.lots_of_chr.$pre

! Convert "lots_of_chr" to bytes
sth.$lots_of_chr

! Enable printing
out.!

! Print the output of the previous instruction - its not "out.!" because 
! it doesn't generate any output
out.$pre
```
You can save this file as "example.bsc" and run it:
```
binscript example.bsc
```

# Should I use it?
Probably not.

# License
This project is under IDC offical license, just kidding its MIT.
Check LICENSE.txt for more details.