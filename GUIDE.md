# RUNTIME GUIDE

This document is an overview of the features and syntax of RUNTIME. For an in-depth view of how everything works, see [DOCUMENTATION.md](https://github.com/Mikuel210/RUNTIME/blob/main/DOCUMENTATION.md).

> **DISCLAIMER:** RUNTIME is in active development. Expect stuff to break.

## Navigation

- [Core Types](#core-types)
- [Variables](#variables)
    - [Variable syntax](#variable-syntax)
    - [Reading and assignment](#reading-and-assignment)
    - [Example](#example)
- [Comments](#comments)
- [Functions](#functions)
    - [Example](#example-1)
- [Methods](#methods)
    - [Example](#example-2)
- [Lists](#lists)
    - [Example](#example-3)
- [Dictionaries](#dictionaries)
    - [Example](#example-4)
- [Scopes](#scopes)
    - [Default scope](#default-scope)
        - [Default variables](#default-variables)
        - [Default built-ins](#default-built-ins)
        - [Default dictionaries](#default-dictionaries)
        - [Default methods](#default-methods)
- [Flow control](#flow-control)
    - [Conditions](#conditions)
    - [Branching](#branching)
    - [Loops](#loops)

## Core Types

| Type                  | Syntax                           | Description                                                                                                                    |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Text**              | `"Single line"`, `{ Multiline }` | Text is just text. No `char`, no `StringBuilder`. All text is executable via `()`. Multiline text using `{}` can be nested. |
| **Number**            | `3.14`, `42`                     | Numbers are just numbers. No `int`, `float`, `byte` or `double`, just one numeric type for all.                                |
| **List**              | `[1, 2, 3]`                      | Lists are just lists. No `stack`, `queue`, `array` or `tuple`. Just a single, flexible, ordered container.                     |
| **Dictionary**        | `\|"a": 1, "b": 2\|`               | No `HashMap` or `object`. Just a single unit of key-value mappings.                                                            |
| **Null**              | `Null()`                         | No `()`, `void` or `unit`. Just a single unit of nothingness.                                                                  |
| **Built-in function** | `BuiltIn("print")`               | Built-ins are functions that perform low-level operations, meaning you can't access their code.                                |

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

## Comments

- **Single line:** `// Comment`
- **Multiline:** `/* Comment */`

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
## Methods

- Methods are functions that can be executed using the `object.method()` syntax.
- Methods are functions that follow `Type~method` naming convention.
- All functions following the naming convetion can be used as methods.
- When a method is called, the first argument passed to the function is the object it's being called on.

### Example

```javascript
// List~append is a default method
list = [1, 2, 3]
list = list.append(4)
print(list) // > [1, 2, 3, 4]

// Overwrite the append method to remove elements instead
List~append = {
    list = arguments[0]
    element = arguments[1]
    list.remove(element)
}

print(list.append(4)) // > [1, 2, 3]

// Declare a custom method
Text~shout = {
    text = arguments[0]
    text.to_uppercase() + "!!!"
}

print("runtime".shout()) // > RUNTIME!!!
```

## Lists

- Lists are defined with comma-separated values encapsulated between brackets. 
- To read an element, use `$list[i]`.
- To overwrite an element, use `$list[i] = "value"`.

### Example

```javascript
list = [1, 2, 3]
list[0] = 42
print(list[0]) // > 42
```

## Dictionaries

- Dictionaries are defined with comma-separated key-value pairs encapsulated between pipes.
- To read a value from its key, use `$dictionary["key"]`.
- To assign a value to a key, use `$dictionary["key"] = "value"`.
- `$dictionary.key` reads a key, as long as it isn't shadowed by a method.
- `$dictionary.key = "value"` assigns to a key.

### Example

```javascript
dictionary = |
    "a": 1,
    "b": 2,
    "c": 3
|

dictionary["a"] = 42
print(dictionary["a"]) // > 42
```

## Scopes

When a text object is executed, a new scope is created for its variables. Variables in parent scopes are visible by default, as long as they aren't shadowed by variables with the same name in children scopes.

- To access a variable in the current scope that has been shadowed by parent scopes, use `[0]$var`
- To access a variable in the parent scope that has been shadowed in the current one, use `[1]$var`
- To access a shadowed variable two levels up in the hierarchy, use `[2]$var`, and so on
- To access a variable in the global scope, use `[global]$var`
- To access a default variable that has been overwritten, use `[default]$var`

### Default scope

#### Default variables

| Variable | Type     | Default value | 
| -------- | -------- | ------------- |
| `true`   | `Number` | `1`           |
| `false`  | `Number` | `0`           |
| `null `  | `Null`   | `null`        |

#### Default built-ins

| Function     | Parameters          | Description                                                                       | Return type |
| ------------ | ------------------- | --------------------------------------------------------------------------------- | ----------- |
| `print`      | `*objects: object`  | Prints one or more objects to the console.                                        | `Null`      |
| `input`      | `message?: object`  | Returns the user input from the console and displays an optional message.         | `Text`      |
| `length`     | `object: object`    | Returns the length of the provided object.                                        | `Number`    |
| `wait`       | `seconds: Number`   | Interrupts the thread for the provided amount of seconds.                         | `Null`      |
| `type`       | `object: object`    | Returns the name of the type of the provided object.                              | `Text`      |
| `is_defined` | `name: object`      | Returns `1` if a variable with the provided name is defined, and `0` if it isn't. | `Number`    |

> **NOTE:** Constructors are default built-in functions (see [core types](https://github.com/Mikuel210/RUNTIME/blob/main/DOCUMENTATION.md#core-types))

#### Default dictionaries

- `ai`
- `math`

> See [default dictionaries](https://github.com/Mikuel210/RUNTIME/blob/main/DOCUMENTATION.md#default-dictionaries)

#### Default methods

> See [default methods](https://github.com/Mikuel210/RUNTIME/blob/main/DOCUMENTATION.md#default-methods)

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
        i = i + 1
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