![RUNTIME banner](images/banner.png)

**RUNTIME is a complete reimagining of what a programming language could and should be.**

RUNTIME is a heavily opinionated, dynamic interpreted language built for flexibility and adaptability.
No type cages. No compile-time errors. No bloat. Just you, your ideas and a blank canvas.

# PHILOSOPHY - The 6 Core Pillars of RUNTIME

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

# USE CASES

-   **Self-modifying programs**: AI written on-demand features? Self-evolving code? You can do that and much more.
-   **Self-debugging code**: Instead of crashing on errors, your program can patch itself and keep going.
-   **Hot-swappable features**: Replace entire functions and modules at runtime. No restarts required.
-   **Safety-critical software**: No don't do that.

# DOCUMENTATION

> **NOTE:** RUNTIME is in active development and not all features from the Philosophy are implemented.

## Navigation

TODO

## Core types

| Type                  | Syntax                           | Description                                                                                                                    |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Text**              | `"Single line"`, `{ Multiline }` | Text is just text. No `char`, no `StringBuilder`. All text is executable via `()`. Multiline text using `{}` can be nested. |
| **Number**            | `3.14`, `42`                     | Numbers are just numbers. No `int`, `float`, `byte` or `double`, just one numeric type for all.                                |
| **List**              | `[1, 2, 3]`                      | Lists are just lists. No `stack`, `queue`, `array` or `tuple`. Just a single, flexible, ordered container.                     |
| **Dictionary**        | `\|"a": 1, "b": 2\|`               | No `HashMap` or `object`. Just a single unit of key-value mappings.                                                            |
| **Null**              | `Null()`                         | No `()`, `void` or `unit`. Just a single unit of nothingness.                                                                  |
| **Built-in function** | `BuiltIn("print")`               | Built-ins are functions that perform low-level operations, meaning you can't access their code.                                |

## Comments

- **Single line:** `// Comment`
- **Multiline:** `/* Comment */`

## Variables

### Variable syntax

- `$var`: Gets the value or assigns to `"var"`. Non-conflicting variable names can skip the `$` symbol.
- `$(...)`: Gets the value or assigns to a variable from a dynamic name

### Reading and assignment

- `$var`: Reads the value of a variable
- `$var = "value"`: Assigns a value to a variable

### Example

```javascript
$var = "Hello World!"
$print($var) // > Hello World!

// Non-conflicting names can skip the $ symbol
print(var) // > Hello World!
```

## Scopes

When a text object is executed, a new scope is created for its variables. Variables in parent scopes are visible by default, as long as they aren't shadowed by variables with the same name in children scopes.

- To access a variable in the parent scope that has been shadowed in the current one, use `[1]$var`
- To access a shadowed variable two levels up in the hierarchy, use `[2]$var`, and so on
- To access a variable in the global scope, use `[global]$var`
- To access a default variable that has been overwritten, use `[default]$var`

### Default scope

- #### Default variables

    | Variable | Type     | Default value | 
    | -------- | -------- | ------------- |
    | `true`   | `Number` | `1`           |
    | `false`  | `Number` | `0`           |
    | `null `  | `Null`   | `null`        |

- #### Default built-ins

    | Function | Parameters          | Description                                                                  | Return type |
    | -------- | ------------------- | ---------------------------------------------------------------------------- | ----------- |
    | `print`  | `*objects: object`  | Prints one or more objects to the console.                                   | `Null`      |
    | `input`  | `message?: object`  | Returns the user input from the console and displays an optional message.    | `Text`      |
    | `length` | `object: object`    | Returns the length of the provided object.                                   | `Number`    |
    | `wait`   | `seconds: Number`   | Interrupts the thread for the provided amount of seconds.                    | `Null`      |
    | `type`   | `object: object`    | Returns the name of the type of the provided object.                         | `Text`      |

    - Constructors are default built-in functions as well.

- #### Default dictionaries

    - ``ai``
        | Key          | Value type | Parameters     | Description                                         | Return type |
        | ------------ | ---------- | -------------- | --------------------------------------------------- | ----------- |
        | `"prompt"`   | `BuiltIn`  | `prompt: Text` | Returns the response of an AI to your prompt.       | `Text`      |
        | `"vibecode"` | `BuiltIn`  | `prompt: Text` | Returns valid RUNTIME code fulfilling your prompt.  | `Text`      |

## Functions

- Functions are declared by defining text variables. Any text is executable via `()`.
- You can get the arguments passed to the function from the `arguments` default variable.
- The last expression on a function will be returned by default.

### Example

```javascript
get_input = {
    input("INPUT: " + arguments[0])
}

name = get_input("Enter your name") // > INPUT: Enter your name
print("Your name is " + name) // > Your name is <name>
```

## Flow control

### Conditions

-   `true` and `false` are variables with the default values of 1 and 0 respectivelly
-   **Boolean operators:** `and`, `or`, `not`
-   **Comparison operators:** `>`, `<`, `>=`, `<=`, `==`, `!=`

### Branching

-   **If**: Executes the provided object if the provided condition is met

    ```javascript
    if (true) {
        print("Hello World!")
    }
    ```

-   **Else**: Executes the provided object or if statement in case the condition of the previous if statement wasn't met

    ```javascript
    number = Number(input())

    if (number == 1) {
        print("Number is 1")
    } else if (number == 2) {
        print("Number is 2")
    } else {
        print("Number is 3 or more")
    }
    ```

### Loops

-   **While**: If the provided condition is met, the provided object is executed and the code block repeats.

```javascript
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

TODO: ABOUT AI USAGE
