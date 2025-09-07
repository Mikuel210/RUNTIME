# RUNTIME DOCUMENTATION

This document describes how everything works in RUNTIME. For a general overview of the language, see [GUIDE.md](https://github.com/Mikuel210/RUNTIME/blob/main/GUIDE.md).

## Navigation

- [Core Types](#core-types)
    - [Text](#text)
    - [Numbers](#numbers)
    - [Lists](#lists)
    - [Dictionaries](#dictionaries)
    - [Null](#null)
    - [Built-in Functions](#built-in-functions)
- [Operators](#operators)
    - [Addition](#addition-)
    - [Subtraction](#subtraction--)
    - [Multiplication](#multiplication-)
    - [Division](#division-)
    - [Power](#power-)
- [Default Scope](#default-scope)
    - [Default variables](#default-variables)
    - [Default dictionaries](#default-dictionaries)
    - [Default built-ins](#default-built-ins)
    - [Default methods](#default-methods)

## Core Types

### Text

- #### Constructors

    | Constructor            | Description                                                                                          |
    | ---------------------- | ---------------------------------------------------------------------------------------------------- |
    | `Text(object: object)` | Constructs a new text object from the provided value.                                                |

- #### Literals

    | Literal    | Description                                                      |
    | ---------- | ---------------------------------------------------------------- |
    | `"Text"`   | Single-line text literal.                                        |
    | `{ Text }` | Multiline text literal. Multiline text using `{}` can be nested. |

- #### Syntax

    - `text()`: Executes the code stored in the `text` variable.

### Numbers

- #### Constructors

    | Constructor              | Description                                             |
    | ------------------------ | ------------------------------------------------------- |
    | `Number(object: object)` | Constructs a new number object from the provided value. |

- #### Literals

    - `3.14`, `42`

### Lists

- #### Constructors

    | Constructor              | Description                                                                                                  |
    | ------------------------ | ------------------------------------------------------------------------------------------------------------ |
    | `List(*objects: object)` | Constructs a new list from the provided elements.                                                            |

- #### Literals

    | Literal           | Description                                                              |
    | ----------------- | ------------------------------------------------------------------------ |
    | `[]`, `[1, 2, 3]` | List literal using comma-separated values encapsulated between brackets. |

- #### Syntax

    - `$list[i]`: Reads the value of element `i` in the list.
    - `$list[i] = value`: Assigns `value` to element `i` in the list.

#### Example

```javascript
list = [1, 2, 3]
list[0] = 42
print(list[0]) // > 42
```

### Dictionaries

- #### Constructors

    | Constructor                            | Description                                                    |
    | -------------------------------------- | -------------------------------------------------------------- |
    | `Dictionary(keys: List, values: List)` | Constructs a new dictionary from the provided keys and values. |

- #### Literals

    | Literal                      | Description                                                                          |
    | ---------------------------- | ------------------------------------------------------------------------------------ |
    | `\|\|`, `\|"a": 1, "b": 2\|` | Dictionary literal using comma-separated key-value pairs encapsulated between pipes. |

- #### Syntax

    - `$dictionary["key"]`: Reads the value stored in `"key"` in the dictionary.
    - `$dictionary["key"] = "value"`: Assigns `"value"` to key `"key"` in the dictionary.
    - `$dictionary.key`: Reads or assigns to `dictionary["key"]`, except if shadowed by a method with the same name.

#### Example

```javascript
dictionary = |
    "a": 1,
    "b": 2,
    "c": 3
|

dictionary["a"] = 42
print(dictionary["a"]) // > 42
```

### Null

- #### Constructors

    | Constructor | Description                   |
    | ----------- | ----------------------------- |
    | `Null()`    | Constructs a new null object. |

### Built-in functions

- #### Constructors

    | Constructor           | Description                                                                          |
    | --------------------- | ------------------------------------------------------------------------------------ |
    | `BuiltIn(name: Text)` | Returns the default value of a [default built-in](#default-built-ins) from its name. |

- #### Syntax

    - `input()`: Executes the built-in function stored in the `input` default variable.

#### Example

```javascript
print("Hello World!") // > Hello World!

print = {
    BuiltIn("print")("You have been hijacked")
}

print("Hello World!") // > You have been hijacked

print = BuiltIn("print")
print("Hello World!") // > Hello World!
```

## Operators

### Addition (`+`)

| ↓ `+` →    | Text | Number | List | Dictionary | Null | Built-in |
| ---------- | ---- | ------ | ---- | ---------- | ---- | -------- |
| Text       | Concatenates the text objects | Appends the number as text | Appends the list as text | Appends the dictionary as text | Appends the null object as text | |
| Number     | Prepends the number as text | Adds the numbers | | | | |
| List       | Prepends the list as text | | Concatenates the lists | | | |
| Dictionary | Prepends the dictionary as text | | | Merges the dictionaries | | |
| Null       | Prepends the null object as text | | | | | |
| Built-in   | | | | | | |

### Subtraction (`-`)

| ↓ `-` →    | Text | Number | List | Dictionary | Null | Built-in |
| ---------- | ---- | ------ | ---- | ---------- | ---- | -------- |
| Text       | Removes a suffix, if present | | | | | |
| Number     | | Subtracts the numbers | | | | |
| List       | | | | | | |
| Dictionary | | | | Performs dictionary difference | | |
| Null       | | | | | | |
| Built-in   | | | | | | |

### Multiplication (`*`)

| ↓ `*` →    | Text | Number | List | Dictionary | Null | Built-in |
| ---------- | ---- | ------ | ---- | ---------- | ---- | -------- |
| Text       | | Repeats the string `n` times | | | | |
| Number     | | Multiplies the numbers | | | | |
| List       | | Repeats the list `n` times | | | | |
| Dictionary | | | | | | |
| Null       | | | | | | |
| Built-in   | | | | | | |

### Division (`/`)

| ↓ `/` →    | Text | Number | List | Dictionary | Null | Built-in |
| ---------- | ---- | ------ | ---- | ---------- | ---- | -------- |
| Text       | | | | | | |
| Number     | | Divides the numbers | | | | |
| List       | | | | | | |
| Dictionary | | | | | | |
| Null       | | | | | | |
| Built-in   | | | | | | |

### Power (`^`)

| ↓ `^` →    | Text | Number | List | Dictionary | Null | Built-in |
| ---------- | ---- | ------ | ---- | ---------- | ---- | -------- |
| Text       | | | | | | |
| Number     | | Raises the first number to the power of the second | | | | |
| List       | | | | | | |
| Dictionary | | | | | | |
| Null       | | | | | | |
| Built-in   | | | | | | |

## Default Scope

### Default variables

| Variable | Type     | Default value | 
| -------- | -------- | ------------- |
| `true`   | `Number` | `1`           |
| `false`  | `Number` | `0`           |
| `null `  | `Null`   | `null`        |

### Default dictionaries

- `ai`
    | Key          | Value type | Parameters     | Description                                         | Return type |
    | ------------ | ---------- | -------------- | --------------------------------------------------- | ----------- |
    | `"prompt"`   | `BuiltIn`  | `prompt: Text` | Returns the response of an AI to your prompt.       | `Text`      |
    | `"vibecode"` | `BuiltIn`  | `prompt: Text` | Returns valid RUNTIME code fulfilling your prompt.  | `Text`      |

- `math`
    | Key                | Value type | Parameters                             | Description                                           | Return type |
    | ------------------ | ---------- | -------------------------------------- | ----------------------------------------------------- | ----------- |
    | `"pi"`             | `Number`   | —                                      | Constant π: 3.1415926535...                           | —           |
    | `"e"`              | `Number`   | —                                      | Constant e: 2.7182818284...                           | —           |
    | `"ceiling"`        | `BuiltIn`  | `number: Number`                       | Rounds the number up to the nearest integer.          | `Number`    |
    | `"floor"`          | `BuiltIn`  | `number: Number`                       | Rounds the number down to the nearest integer.        | `Number`    |
    | `"round"`          | `BuiltIn`  | `number: Number`                       | Rounds the number to the nearest integer.             | `Number`    |
    | `"absolute_value"` | `BuiltIn`  | `number: Number`                       | Returns the the absolute value of `number`.           | `Number`    |
    | `"square"`         | `BuiltIn`  | `number: Number`                       | Returns `number` squared.                             | `Number`    |
    | `"cube"`           | `BuiltIn`  | `number: Number`                       | Returns `number` cubed.                               | `Number`    |
    | `"power"`          | `BuiltIn`  | `base: Number, exponent: Number`       | Raises the ``base`` to the power of the ``exponent``. | `Number`    |
    | `"square_root"`    | `BuiltIn`  | `number: Number`                       | Returns the square root of `number`.                  | `Number`    |
    | `"cubic_root"`     | `BuiltIn`  | `number: Number`                       | Returns the cubic root of `number`.                   | `Number`    |
    | `"root"`           | `BuiltIn`  | `value: Number, degree: Number`        | Returns the `degree`-th root of `value`.              | `Number`    |
    | `"logarithm"`      | `BuiltIn`  | `value: Number, base: Number = math.e` | Returns the logarithm of `value` from a given `base`. | `Number`    |
    | `"factorial"`      | `BuiltIn`  | `number: Number`                       | Returns the factorial of `number`.                    | `Number`    |
    | `"random"`         | `BuiltIn`  | `min: Number = 0, max: Number = 1`     | Returns a random number in the provided range.        | `Number`    |

### Default built-ins

| Function     | Parameters          | Description                                                                       | Return type |
| ------------ | ------------------- | --------------------------------------------------------------------------------- | ----------- |
| `print`      | `*objects: object`  | Prints one or more objects to the console.                                        | `Null`      |
| `input`      | `message?: object`  | Returns the user input from the console and displays an optional message.         | `Text`      |
| `length`     | `object: object`    | Returns the length of the provided object.                                        | `Number`    |
| `wait`       | `seconds: Number`   | Interrupts the thread for the provided amount of seconds.                         | `Null`      |
| `type`       | `object: object`    | Returns the name of the type of the provided object.                              | `Text`      |
| `is_defined` | `name: object`      | Returns `1` if a variable with the provided name is defined, and `0` if it isn't. | `Number`    |

> **NOTE:** Constructors are built-in functions in the default scope (see [core types](#core-types)).

### Default methods

#### Lists

| Function            | Parameters                       | Description                                                                       | Return type |
| ------------------- | -------------------------------- | --------------------------------------------------------------------------------- | ----------- |
| `List.append`       | `element: object`                | Adds the `element` to the end of the list.                                        | `List`      |
| `List.extend`       | `other: List`                    | Adds all elements in `other` to the end of the list.                              | `List`      |
| `List.remove`       | `element: object`                | Removes the first occurence of `element` from the list.                           | `List`      |
| `List.remove_all`   | `element: object`                | Removes all occurrences of `elements` from the list.                              | `List`      |
| `List.subtract`     | `other: List`                    | Removes the first occurence of each element in `other` from the list.             | `List`      |
| `List.subtract_all` | `other: List`                    | Removes all occurences of each element in `other` from the list.                  | `List`      |
| `List.contains`     | `element: object`                | Returns `1` if the list contains the `element`, and `0` if it doesn't.            | `Number`    |
| `List.index_of`     | `element: object`                | Returns the index of the first ocurrence of `element` in the list.                | `Number`    |
| `List.insert`       | `index: Number, element: object` | Adds the `element` at the provided `index`.                                       | `List`      |
| `List.pop`          | `index: Number`                  | Removes the element found at the provided `index`.                                | `List`      |
| `List.count`        | `element: object`                | Returns the number of occurences of `element` in the list.                        | `Number`    |
| `List.slice`        | `start: Number, end: Number`     | Returns a sublist from `start` (inclusive) to `end` (exclusive).                  | `List`      |

#### Dictionaries

| Function                 | Parameters                   | Description                                                                       | Return type  |
| ------------------------ | ---------------------------- | --------------------------------------------------------------------------------- | ------------ |
| `Dictionary.merge`       | `other: Dictionary`          | Merges the dictionaries. Identical keys will be overwritten by values in `other`. | `Dictionary` |
| `Dictionary.difference`  | `other: Dictionary`          | Removes identical key-value pairs from the dictionary.                            | `Dictionary` |
| `Dictionary.add`         | `key: object, value: object` | Adds a pair from the provided `key` and `value`                                   | `Dictionary` |
| `Dictionary.remove`      | `key: object`                | Removes a key-value pair from its `key`.                                          | `Dictionary` |
| `Dictionary.remove_many` | `keys: List`                 | Removes key-value pairs from their `keys`.                                        | `Dictionary` |
| `Dictionary.keys`        |                              | Returns a list of all keys in the dictionary.                                     | `List`       |
| `Dictionary.values`      |                              | Returns a list of all values in the dictionary.                                   | `List`       |

#### Text

| Function             | Parameters     | Description                                          | Return type |
| -------------------- | -------------- | ---------------------------------------------------- | ----------- |
| `Text.to_lowercase`  |                | Returns the lowercase equivalent of the text object. | `Text`      |
| `Text.to_uppercase`  |                | Returns the upper equivalent of the text object.     | `Text`      |
| `Text.add_prefix`    | `prefix: Text` | Adds a `prefix` to the text object.                  | `Text`      |
| `Text.remove_prefix` | `prefix: Text` | Removes a `prefix` from the text object, if present. | `Text`      |
| `Text.add_suffix`    | `suffix: Text` | Adds a `suffix` to the text object.                  | `Text`      |
| `Text.remove_suffix` | `suffix: Text` | Removes a `suffix` from the text object, if present. | `Text`      |