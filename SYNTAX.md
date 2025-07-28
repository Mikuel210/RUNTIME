## Math expressions

-   **Expression**: Term ((ADD|SUBTRACT) Term ...)
-   **Term**: Factor ((MULTIPLY|DIVIDE) Factor ...)
-   **Factor**: Number
    : ((ADD|SUBTRACT) Factor)
    : OPEN_PARENTHESIS Expression CLOSE_PARENTHESIS
    : Factor POWER Factor