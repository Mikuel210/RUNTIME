() = Priority
* = 0 or more of the previous term

## Math expressions

-   **Expression**: Variable EQUALS Expression
                  : Term ((ADD|SUBTRACT) Term)*

-   **Variable**: VARIABLE (IDENTIFIER|KEYWORD|Expression)
                : IDENTIFIER

-   **Term**: Factor ((MULTIPLY|DIVIDE) Factor)*

-   **Factor**: (ADD|SUBTRACT) Factor
              : Power

-   **Power**: Atom (POWER Factor)

-   **Atom**: Variable | Number
            : OPEN_PARENTHESIS Expression CLOSE_PARENTHESIS