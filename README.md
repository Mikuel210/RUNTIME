![RUNTIME banner](images/banner.png)

**RUNTIME is a complete reimagining of what a programming language could and should be.**

RUNTIME is a heavily opinionated, dynamic interpreted language built for flexibility and adaptability.
No type cages. No compile-time errors. No bloat. Just you, your ideas and a blank canvas.

## Philosophy - The 6 Core Pillars of RUNTIME

### Typed languages are cages

Typed, compiled languages promise "safety", but all they do is get in your way. Type mismatches, rigid syntax and compile-time errors kill your ideas before they even start. In RUNTIME, stuff just RUNS. With no rules and no types, you can focus on ACTUALLY CODING and bringing your raw, unfiltered ideas to life.

### Variables are memory entries

Variables and functions are just named memory entries. So why do most languages treat them like sacred artifacts? In RUNTIME, names are flexible. You can construct them, change them or pass them around, just like ANY OTHER VALUE.

### Code is text

When you're writing code, you're writing text. So why do most languages act like code and text are completely separate worlds? In RUNTIME, they're the same thing. Code is data and data is code. Want to store functions in plain text? Generate logic on the fly? Rewrite your code while it runs? Go for it.

### Programs should evolve

Other languages treat your program like a dead script: once it runs, it’s frozen. But that’s not how humans think. With RUNTIME, your program is alive. You can interact with the interpreter, redefine built-ins, and mutate your logic while it runs. Handle bugs. Inject new features. Adapt and evolve.

### Errors are values

Make one typo and your whole app explodes? That's a JOKE. In RUNTIME, errors are values. They don’t crash your program, they just show up, like ANY OTHER RESULT. You can inspect them, log them, ignore them, or react to them. Your code keeps going.

### Simplicity is key

> **An idiot admires complexity, a genius admires simplicity**
>
> — Terry Davis, creator of TempleOS

Tuples, arrays, lists, stacks, queues... WHY? RUNTIME gives you just 6 types. No bloat. No confusion. No distractions. Still, all the tools you need to ACTUALLY bring your projects to life.

## Use cases

-   **Self-modifying programs**: AI written on-demand features? Self-evolving code? You can do that and much more.
-   **Self-debugging code**: Instead of crashing on errors, your program can patch itself and keep going.
-   **Hot-swappable features**: Replace entire functions and modules at runtime. No restarts required.
-   **Safety-critical software**: No don't do that.

## Language design

### Core types

| Type                  | Syntax                           | Description                                                                                                                                                                                                |
| --------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Text**              | `"Single line"`, `{ Multiline }` | All text is executable via `()`. Multiline strings using `{}` can be nested.                                                                                                                               |
| **Number**            | `3.14`, `42`                     | Numbers are just numbers. No `int`, `float`, `byte` or `double`. One numeric type for all.                                                                                                                 |
| **List**              | `[1, 2, 3]`                      | Lists are just lists. No `stack`, `queue`, `array` or `tuple`. Just a single, flexible, ordered container.                                                                                                 |
| **Dictionary**        | `["x": 1, "y": 2]`               | A list of key-value mappings. Syntax automatically detects colons to distinguish them from lists.                                                                                                          |
| **Error**             | `error("Title", "Message")`      | Errors are just values. Your program keeps going. Inspect them, ignore them or react to them.                                                                                                              |
| **Built-in function** | `builtin("print")`               | Built-ins perform low-level operations, meaning you can't access their code. They're stored in variables which you can overwrite. To get the default value for a built-in function, use `builtin("name")`. |

### Variable syntax

| Syntax   | Meaning                                       |
| -------- | --------------------------------------------- |
| `$var`   | Get the value of `"var"`                      |
| `#var`   | Get the reference to `"var"`                  |
| `$(...)` | Get the value for a dynamic variable name     |
| `#(...)` | Get the reference for a dynamic variable name |

#### Assigning and reading variables

To assign variables, use `#var = "value"`. To read them, use `$var`. For non-conflicting variable names, you can skip the `$` for getting its value.

```runtime
#var = "Hello World!"
$print($var) // > Hello World!

// Non-conflicting names can skip the $
print(var) // > Hello World!
```

### Functions

Functions are text variables. Any text is executable via `()`.

```runtime
#say_hello = {
    print("Hello World!")
}

say_hello() // > Hello World!
```

You can get arguments with the `args` keyword and pass back values with the `return` keyword:

```runtime
#get_input = {
    return(input("INPUT: " + args[0]))
}

get_input("Enter your name") // > INPUT: Enter your name
```

### Lists

You can define lists with comma-separated values encapsulated between brackets. To read a value, use `$list[i]` and to overwrite it, use `#list[i] = "value"`.

```runtime
#list = [1, 2, 3]
#list[0] = 42
print($list[0])    // > 42


```

### Dictionaries

You can define lists with comma-separated key-value pairs encapsulated between brackets. Each key-value pair is defined with a key object, a colon and a value object. To read a value, use `$dict[key]` and to overwrite it, use `#dict[key] = "value"`.

```runtime
#dict = [
    "name": "Duna",
    "age": 42
]

#dict["age"] = 49
print(dict["age"]) //  > 49
```

### Built-in functions

Built in functions are stored in variables, but you can restore them in any time with `builtin("name")`.

```runtime
print("Hello World!") // > Hello World!

#print = {
    return(input("INPUT: " + args[0]))
}

print("Hello World!") // > INPUT: Hello World!

#print = builtin("print")
print("Hello World!") // > Hello World!
```

### Errors

Errors are values you can inspect and react to.

```runtime
#x = "Not callable!"
#result = x()

print($result) // > Syntax Error

if ($result is error) {
    print("Caught: " + $result.message)
}
```

### Flow control

#### Conditions

-   `true`, `false`
-   `and`, `or`, `not`
-   `>`, `<`, `>=`, `<=`, `==`, `!=`

#### Branching

-   **If**: Executes the provided text object if the provided condition is met

    ```runtime
    if (true) {
        print("Hello World!")
    }
    ```

-   **Unless**: Executes the provided text object if the provided condition isn't met

    ```runtime
    unless (true) {
        print("This won't run")
    }
    ```

#### Loops

-   **While**: If the provided condition is met, the provided text object is executed and the code block repeats.

```runtime
#i = 3

while ($i > 0) {
    print($i + " loop(s) left!")
    $i = $i - 1
}

// > 3 loop(s) left!
// > 2 loop(s) left!
// > 1 loop(s) left!
```

---

RUNTIME isn't just a new language.

It's a new way to think.

> RUNTIME is a work in progress. Stay tuned for updates.

> DISCLAIMER: I have used AI to rewrite some parts of this README. I haven't used AI for anything else in this project.
