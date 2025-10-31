() = Priority

* = 0 or more
+ = 1 or more
? = 0 or 1

## Syntax
 
- **Expression**: ArithmeticExpression
   
- **ArithmeticExpression**: Term ((ADD|SUBTRACT) Term)*
   
- **Term**: Factor ((MULTIPLY|DIVIDE) Factor)*
  
- **Factor**: (ADD|SUBTRACT)? Factor
    Atom
 
- **Atom**: BaseAtom
 
- **BaseAtom**: Number
    OPEN_PARENTHESIS Expression CLOSE_PARENTHESIS