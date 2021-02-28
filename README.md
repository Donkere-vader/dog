# Dog

simple project management.  
Inspired by ``npm run COMMAND``

## Installation

clone the repo

```bash
git clone https://www.github.com/donkere-vader/dog.git
```

Place the dogmodule somewhere logical

```bash
cd dog
mv dogmodule ~/bin
```

Either add an alias to your .bash_aliases

```bash
alias dog="python3 ~/bin/dogmodule"
```

Or make a shell script to launch the file
**~/bin/dog**

```sh
#!/bin/bash
python3 ~/bin/dogmodule $@
```

## Usage

There are two options. Just one simple file. Or if you want to use some more advanced scripts to run a folder

### File structure

project structure in the case of a file:

```files
# -- snip --
dog.json
```

project structure in the case of a folder:

```files
# -- snip --
dog/
    dog.json
    customscript1.sh  # example
    customscript2.sh  # example
```

### JSON strucutre

This is an example of a config file in the case of a file:
**dog.json**

```json
{
    "commands": {
        "example": "echo test"
    }
}
```

This is an example of a config file in the case of a folder:  
**dog/dog.json**

```json
{
    "commands": {
        "example": {"file": "customscript1.sh"}
    }
}
```

### Run command

```bash
dog example
```

### Flags

The flags for the dog command

#### File & folder

If you want to use another file than "dog.json" or another folder than "dog" that is possible wit the --file (-f) and the --folder flags.

```bash
dog example --file other.json --folder other
```

Will look for the example command in other/other.json

## Why "dog"?

Well if people can name there unix commands after animals: [cat](https://en.wikipedia.org/wiki/Cat_(Unix)). Then I want to name mine after a dog. Because dogs are the best

(I know the cat from the cat command doesn't stand for the animal)
