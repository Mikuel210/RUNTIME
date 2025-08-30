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

-   **Statements**: NEW_LINE* Expression? (NEW_LINE+ Expression)* NEW_LINE*

-   **Expression**: IfExpression
                  : Variable EQUALS Expression
                  : ComparaisonExpression ((KEYWORD:and|or) ComparaisonExpression)*

-   **ComparaisonExpression**: not ComparaisonExpression
                             : ArithmeticExpression ((EE|LT|GT|LTE|GTE) ArithmeticExpression)*

-   **ArithmeticExpression**: Term ((ADD|SUBTRACT) Term)*

-   **IfExpression**: KEYWORD:if OPEN_PARENTHESIS Expression CLOSE_PARENTHESIS Atom

-   **Variable**: (LT Expression | KEYWORD:global GT)? VARIABLE (IDENTIFIER|KEYWORD|BaseAtom)
                : (LT Expression | KEYWORD:global GT)? IDENTIFIER

-   **Term**: Factor ((MULTIPLY|DIVIDE) Factor)*

-   **Factor**: (ADD|SUBTRACT) Factor
              : Power

-   **Power**: Atom (POWER Factor)

-   **Atom**: BaseAtom (Postfix)*

-   **BaseAtom**: Variable | Number | Text
            : OPEN_PARENTHESIS Expression CLOSE_PARENTHESIS
            : ListExpression

-   **ListExpression**: OPEN_BRACKETS (Expression (COMMA Expression)*)? CLOSE_BRACKETS

-   **Postfix** : (OPEN_PARENTHESIS (Expression (COMMA Expression)*)? CLOSE_PARENTHESIS)?
                : (OPEN_BRACKETS Expression CLOSE_BRACKETS)?