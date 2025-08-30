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

Tuples, arrays, lists, stacks, queues... WHY? RUNTIME gives you just 7 types. No bloat. No confusion. No distractions. Still, all the tools you need to ACTUALLY bring your projects to life.

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
| **Number**            | `3.14`, `42`                     | Numbers are just numbers. No `int`, `float`, `byte` or `double`, just one numeric type for all. `true` and `false` are variables with the default values of 1 and 0 respectively.                                                                                                                |
| **List**              | `[1, 2, 3]`                      | Lists are just lists. No `stack`, `queue`, `array` or `tuple`. Just a single, flexible, ordered container.                                                                                                 |
| **Dictionary**        | `["x": 1, "y": 2]`               | A list of key-value mappings. Syntax automatically detects colons to distinguish them from lists.                                                                                                          |
| **Error**             | `Error("Title", "Message")`      | Errors are just values. Your program keeps going. Inspect them, ignore them or react to them.                                                                                                              |
| **Built-in function** | `BuiltIn("print")`               | Built-ins perform low-level operations, meaning you can't access their code. They're stored in variables which you can overwrite. To get the default value for a built-in function, use `BuiltIn(name)`. |
| **Null** | `Null()` | A single unit of nothingness. `null` is a default variable that holds a null object. |

### Variables

#### Variable syntax

| Syntax   | Meaning                                       |
| -------- | --------------------------------------------- |
| `$var`   | Get the value or assign to `"var"`                      |
| `$(...)` | Get the value or assign to a variable from a dynamic name     |

#### Reading and assignment

To read variables, use `$var`. To assign them, use `$var = "value"`. For non-conflicting variable names, you can skip the `$`.

```runtime
$var = "Hello World!"
$print($var) // > Hello World!

// Non-conflicting names can skip the $
print(var) // > Hello World!
```

#### Scopes

When a function is called, a new scope is created for its variables. Variables in parent scopes are visible by default, as long as they aren't shadowed by variables with the same name in children scopes. All variable assignments affect the current scope by default.

To access or assign variables in the immediate parent scope, use `[1]$var`. To access variables two levels up in the hierarchy, use `[2]$var`, and so on. To access variables in the global scope, you can use the `global` keyword: `[global]$var`.

### Functions

Functions are made by defining text variables. Any text is executable via `()`.

```runtime
say_hello = {
    print("Hello World!")
}

say_hello() // > Hello World!
```

You can get arguments from the `arguments` default variable. The last expression on a function will be returned by default.

```runtime
get_input = {
    input("INPUT: " + arguments[0])
}

name = get_input("Enter your name") // > INPUT: Enter your name
print("Your name is " + name) // > Your name is <name>
```

### Lists

You can define lists with comma-separated values encapsulated between brackets. To read a value, use `$list[i]` and to overwrite it, use `$list[i] = "value"`.

```runtime
list = [1, 2, 3]
list[0] = 42
print(list[0]) // > 42
```

### Dictionaries

TODO

### Built-in functions

Built-in functions are stored in default variables that can be overwritten. To get the default value for a built-in function, use `BuiltIn("name")`.

```runtime
print("Hello World!") // > Hello World!

print = {
    input("INPUT: " + args[0])
}

print("Hello World!") // > INPUT: Hello World!

print = BuiltIn("print")
print("Hello World!") // > Hello World!
```

| Function | Description | Return value |
| `print(*objects)` | Prints one or more objects to the console. | `Null` |
| `input(message?)` | Gets the user input from the console and displays an optional input message. | `Text` |
| `length(value)` | Gets the length of the provided object. | `Number` |
| `wait(seconds)` | Interrupts the thread for the provided amount of seconds. | `Null` |
| `type(object)` | Returns the name of the type of the provided object. | `Text` |
| `Number(object)` | Constructs a number object from an object of any type. | `Number` |
| `Text(object)` | Constructs a text object from an object of any type. | `Text` |
| `List(*objects)` | Constructs a list from the provided objects. | `List` |
| `BuiltIn(name)` | Gets a built-in function from its name. | `BuiltIn` |
| `Boolean(object)` | Constructs a number object with a value of either `0` or `1` from an object of any type. | `Number` |
| `Null()` | Constructs a null object. | `Null` |

### Errors

TODO

### Flow control

#### Conditions

-   `true` and `false` are variables with the default values of 1 and 0 respectivelly
-   **Boolean operators:** `and`, `or`, `not`
-   **Comparison operators:** `>`, `<`, `>=`, `<=`, `==`, `!=`

#### Branching

-   **If**: Executes the provided object if the provided condition is met

    ```runtime
    if (true) {
        print("Hello World!")
    }
    ```

-   **Unless**: Executes the provided object if the provided condition isn't met

    ```runtime
    unless (true) {
        print("This won't run")
    }
    ```

#### Loops

-   **While**: If the provided condition is met, the provided object is executed and the code block repeats.

```runtime
i = 0

while (i < 3) {
    [1]i = i + 1
    print("Loop " + i)
}

print("Loop ended")

// > Loop 1
// > Loop 2
// > Loop 3
// > Loop ended
```

---

RUNTIME isn't just a new language.

**It's a new way to think.**

---

> RUNTIME is a work in progress and limited functionality is available. Stay tuned for updates.

> DISCLAIMER: I have used AI to rewrite some parts of this README. I haven't used AI for anything else in this project.
