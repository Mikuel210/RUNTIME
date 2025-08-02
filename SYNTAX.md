() = Priority

* = 0 or more
+ = 1 or more
? = 0 or 1

EE = DOUBLE EQUALS
LT = LESS THAN
GT = GREATER THAN
LTE = LESS THAN OR EQUALS
GTE = GREATER THAN OR EQUALS

## Syntax

-   **Statements**: NEW_LINE* Expression (NEW_LINE+ Expression) NEW_LINE*

-   **Expression**: Variable EQUALS Expression
                  : ComparaisonExpression ((KEYWORD:and|or) ComparaisonExpression)*

-   **ComparaisonExpression**: not ComparaisonExpression
                             : ArithmeticExpression ((EE|LT|GT|LTE|GTE) ArithmeticExpression)*

-   **ArithmeticExpression**: Term ((ADD|SUBTRACT) Term)*

-   **Variable**: VARIABLE (IDENTIFIER|KEYWORD|Expression)
                : IDENTIFIER

-   **Term**: Factor ((MULTIPLY|DIVIDE) Factor)*

-   **Factor**: (ADD|SUBTRACT) Factor
              : Power

-   **Power**: Call (POWER Factor)

-   **Call**: Index (OPEN_PARENTHESIS (Expression (COMMA Expression)*)? CLOSE_PARENTHESIS)?

-   **Index**: Atom (OPEN_BRACKETS Expression CLOSE_BRACKETS)?

-   **Atom**: Variable | Number | String
            : OPEN_PARENTHESIS Expression CLOSE_PARENTHESIS
            : ListExpression

-   **ListExpression**: OPEN_BRACKETS (Expression (COMMA Expression)*)? CLOSE_BRACKETS