
from abc import ABC, abstractmethod


#region ERRORS

class Error:
    def __init__(self, start_position, end_position, error_name, details):
        self.start_position = start_position
        self.end_position = end_position
        self.error_name = error_name
        self.details = details

    def as_string(self):
        return f"""{self.error_name}: {self.details}
File: {self.start_position.file_name}
From: Line {self.start_position.line + 1}, character {self.start_position.column + 1}
To: Line {self.end_position.line + 1}, character {self.end_position.column + 1}"""
    
    def __repr__(self) -> str:
        return self.as_string()
    
class IllegalCharacterError(Error):
    def __init__(self, start_position, end_position, details):
        super().__init__(start_position, end_position, 'Illegal Character', details)

class InvalidSyntaxError(Error):
    def __init__(self, start_position, end_position, details):
        super().__init__(start_position, end_position, 'Invalid Syntax', details)

class RuntimeError(Error):
    def __init__(self, start_position, end_position, details, context):
        super().__init__(start_position, end_position, 'Runtime Error', details)
        self.context = context

    def as_string(self) -> str:
        output = super().as_string()
        output += "\n\n" + self.generate_traceback()

        return output
    
    def generate_traceback(self) -> str:
        output = ''
        position = self.start_position.copy()
        context = self.context

        while context:
            output = f'\nFile: {position.file_name}. Line {position.line + 1}, in {context.display_name}' + output
            position = context.parent_entry_position
            context = context.parent

        return 'Traceback:' + output

#endregion



#region POSITION

class Position:
    def __init__(self, index, line, column, file_name = None, file_text = None):
        self.index = index
        self.line = line
        self.column = column
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_character = None):
        self.index += 1
        self.column += 1

        if current_character == '\n':
            self.line += 1
            self.column = 0

        return self
    
    def copy(self):
        return Position(self.index, self.line, self.column, self.file_name, self.file_text)
    
    def __repr__(self) -> str:
        return f'Index: {self.index}, Line: {self.line}, Column: {self.column}'

#endregion

#region TOKENS

TT_NUMBER = "NUMBER"
TT_ADD = "ADD"
TT_SUBTRACT = "SUBTRACT"
TT_MULIPLY = "MULTIPLY"
TT_DIVIDE = "DIVIDE"
TT_OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
TT_CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"

TT_EOF = "EOF"

class Token:
    def __init__(self, type_, value = None, start_position: Position | None = None, end_position: Position | None = None):
        self.type = type_
        self.value = value
        self.start_position = start_position.copy() if start_position else None
        self.end_position = end_position.copy() if end_position else None

        if self.start_position and not self.end_position:
            self.end_position = self.start_position.copy()
            self.end_position.advance()

    def __repr__(self):
        return self.type + (f": {self.value}" if self.value else "")
    
#endregion

#region LEXER

DIGITS = '0123456789'

class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.position = Position(0, 0, 0, file_name, text)
        self.solve_current_character()

    def solve_current_character(self):
        if self.position.index < len(self.text):
            self.current_character = self.text[self.position.index]
        else:
            self.current_character = None

    def advance(self):
        self.position.advance(self.current_character)
        self.solve_current_character()

    def make_tokens(self):
        tokens = []

        while self.current_character != None:
            if self.current_character in ' \t':
                pass
            elif self.current_character in DIGITS:
                tokens.append(self.make_number())
                continue
            elif self.current_character == '+':
                tokens.append(Token(TT_ADD, start_position = self.position))
            elif self.current_character == '-':
                tokens.append(Token(TT_SUBTRACT, start_position = self.position))
            elif self.current_character == '*':
                tokens.append(Token(TT_MULIPLY, start_position = self.position))
            elif self.current_character == '/':
                tokens.append(Token(TT_DIVIDE, start_position = self.position))
            elif self.current_character == '(':
                tokens.append(Token(TT_OPEN_PARENTHESIS, start_position = self.position))
            elif self.current_character == ')':
                tokens.append(Token(TT_CLOSE_PARENTHESIS, start_position = self.position))
            else:
                character = self.current_character

                start_position = self.position.copy()
                self.advance()
                end_position = self.position.copy()

                return [], IllegalCharacterError(start_position, end_position, character)

            self.advance()

        tokens.append(Token(TT_EOF))
        return tokens, None
    
    def make_number(self):
        number_string = ''
        has_dot = False
        start_position = self.position.copy()

        while self.current_character != None and self.current_character in DIGITS + '.':
            if self.current_character == '.':
                if has_dot: break

                has_dot = True
                number_string += '.'
            else:
                number_string += self.current_character

            self.advance()

        return Token(TT_NUMBER, float(number_string), start_position, self.position.copy())
        
#endregion



#region NODES

class Node:
    def __init__(self, start_position: Position | None = None, end_position: Position | None = None):
        self.start_position = start_position
        self.end_position = end_position

class NumberNode(Node):
    def __init__(self, token: Token):
        super().__init__(token.start_position, token.end_position)
        
        self.token = token

    def __repr__(self):
        return f'({self.token})'

class BinaryOperationNode(Node):
    def __init__(self, left_node: Node, operator_token: Token, right_node: Node):
        super().__init__(left_node.start_position, right_node.end_position)
        
        self.left_node = left_node
        self.operator_token = operator_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node} {self.operator_token} {self.right_node})'

class UnaryOperationNode(Node):
    def __init__(self, operation_token: Token, node: Node):
        super().__init__(operation_token.start_position, node.end_position)

        self.operation_token = operation_token
        self.node = node

    def __repr__(self) -> str:
        return f'({self.operation_token}, {self.node})'

#endregion

#region PARSE RESULT

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None

    def register(self, result):
        if isinstance(result, ParseResult):
            if result.error: self.error = result.error
            return result.node

        return result
    
    def success(self, node):
        self.node = node
        return self
    
    def failure(self, error):
        self.error = error
        return self

#endregion

#region PARSER

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current_token_index = 0
        self.solve_current_token()

    def solve_current_token(self):
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
        
    def advance(self):
        self.current_token_index += 1
        self.solve_current_token()

        return self.current_token
    
    def parse(self):
        result = self.expression()
        token = self.current_token

        if not result.error and token.type != TT_EOF:
            return result.failure(InvalidSyntaxError(
                token.start_position,
                token.end_position,
                "Expected '+', '-', '*' or '/'"
            ))

        return result

    ## Binary Operations

    def factor(self):
        result = ParseResult()
        token = self.current_token

        if token.type in (TT_ADD, TT_SUBTRACT):
            result.register(self.advance())
            factor = result.register(self.factor())

            if result.error: return result            
            return result.success(UnaryOperationNode(token, factor))
        elif token.type == TT_NUMBER:
            result.register(self.advance())
            return result.success(NumberNode(token))
        elif token.type == TT_OPEN_PARENTHESIS:
            result.register(self.advance())
            expression = result.register(self.expression())

            if result.error: return result

            if self.current_token.type == TT_CLOSE_PARENTHESIS:
                result.register(self.advance())
                return result.success(expression)
            else:
                return result.failure(InvalidSyntaxError(
                    self.current_token.start_position,
                    self.current_token.end_position,
                    "Expected ')'"
                ))
        
        return result.failure(InvalidSyntaxError(
            token.start_position, 
            token.end_position, 
            "Expected a number"
        ))

    def term(self):
        return self.binary_operation(self.factor, (TT_MULIPLY, TT_DIVIDE))

    def expression(self):
        return self.binary_operation(self.term, (TT_ADD, TT_SUBTRACT))
    
    def binary_operation(self, function, operation_tokens: tuple):
        result = ParseResult()
        left = result.register(function())

        if result.error: return result

        while self.current_token.type in operation_tokens:
            token = self.current_token
            result.register(self.advance())

            right = result.register(function())
            if result.error: return result

            left = BinaryOperationNode(left, token, right) # type: ignore

        return result.success(left)

#endregion



#region RUNTIME RESULT

class RuntimeResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, result):
        if result.error: self.error = result.error
        return result.value
    
    def success(self, value):
        self.value = value
        return self
    
    def failure(self, error):
        self.error = error
        return self

#endregion

#region RUNTIME OBJECTS

class RuntimeObject(ABC):
    def __init__(self):
        self.set_position()
        self.set_context()

    def set_position(self, start_position = None, end_position = None):
        self.start_position = start_position
        self.end_position = end_position

        return self
    
    def set_context(self, context = None):
        self.context = context
        return self
    
    ## Binary Operations

    @abstractmethod
    def added_to(self, other) -> tuple[object | None, RuntimeError | None]:
        pass
    
    @abstractmethod
    def subtracted_by(self, other) -> tuple[object | None, RuntimeError | None]:
        pass

    @abstractmethod
    def multiplied_by(self, other) -> tuple[object | None, RuntimeError | None]:
        pass

    @abstractmethod
    def divided_by(self, other) -> tuple[object | None, RuntimeError | None]:
        pass

class Number(RuntimeObject):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def set_position(self, start_position = None, end_position = None):
        return super().set_position(start_position, end_position)
    
    def set_context(self, context=None):
        return super().set_context(context)
    
    ## Binary Operations

    def added_to(self, other: RuntimeObject) -> tuple[RuntimeObject | None, RuntimeError | None]:
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        
        return (None, RuntimeError(
            self.start_position, other.end_position,
            f"An object of type {__class__.__name__} can't be added to an object of type {type(other).__name__}",
            self.context
        ))
        
    def subtracted_by(self, other: RuntimeObject) -> tuple[RuntimeObject | None, RuntimeError | None]:
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None

        return (None, RuntimeError(
            self.start_position, other.end_position,
            f"An object of type {__class__.__name__} can't be subtracted by an object of type {type(other).__name__}",
            self.context
        ))
        
    def multiplied_by(self, other: RuntimeObject) -> tuple[RuntimeObject | None, RuntimeError | None]:
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

        return (None, RuntimeError(
            self.start_position, other.end_position,
            f"An object of type {__class__.__name__} can't be multiplied by an object of type {type(other).__name__}",
            self.context
        ))
        
    def divided_by(self, other: RuntimeObject) -> tuple[RuntimeObject | None, RuntimeError | None]:
        if isinstance(other, Number):
            if other.value == 0:
                return None, RuntimeError(
                    self.start_position,
                    other.end_position,
                    'Attempted to divide by zero',
                    self.context
                )
            
            return Number(self.value / other.value).set_context(self.context), None

        return (None, RuntimeError(
            self.start_position, other.end_position,
            f"An object of type {__class__.__name__} can't be multiplied by an object of type {type(other).__name__}",
            self.context
        ))

    def __repr__(self) -> str:
        return str(self.value)

#endregion

#region CONTEXT

class Context:
    def __init__(self, display_name, parent = None, parent_entry_position = None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_position = parent_entry_position

#endregion

#region INTERPRETER

class Interpreter():
    def visit(self, node, context: Context):
        method_name = f'visit_{type(node).__name__}'

        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)
    
    def no_visit_method(self, node, context: Context):
        raise NotImplementedError(f'No visit method was defined for {type(node).__name__}.')
    
    ## Visit Methods

    def visit_NumberNode(self, node: NumberNode, context: Context):
        return RuntimeResult().success(
            Number(node.token.value)
                .set_context(context)
                .set_position(node.start_position, node.end_position)
        )

    def visit_BinaryOperationNode(self, node: BinaryOperationNode, context: Context):
        result = RuntimeResult()

        left = result.register(self.visit(node.left_node, context))
        if result.error: return result

        right = result.register(self.visit(node.right_node, context))
        if result.error: return result

        if node.operator_token.type == TT_ADD:
            output, error = left.added_to(right)
        elif node.operator_token.type == TT_SUBTRACT:
            output, error = left.subtracted_by(right)
        elif node.operator_token.type == TT_MULIPLY:
            output, error = left.multiplied_by(right)
        elif node.operator_token.type == TT_DIVIDE:
            output, error = left.divided_by(right)

        if error: return result.failure(error) # type: ignore
        
        return result.success(output # type: ignore
            .set_context(context)
            .set_position(node.start_position, node.end_position
        ))
    
    def visit_UnaryOperationNode(self, node: UnaryOperationNode, context: Context):
        result = RuntimeResult()

        number = result.register(self.visit(node.node, context))
        if result.error: return result

        if node.operation_token.type == TT_SUBTRACT:
            number, error = number.multiplied_by(Number(-1))
        
        if error: return result.failure(error) # type: ignore
        
        return result.success(number
            .set_context(context)
            .set_position(node.start_position, node.end_position
        ))

#endregion

#region RUN

def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()

    if error: return tokens, error

    # Generate Abstract Syntax Tree
    parser = Parser(tokens)
    ast = parser.parse()

    if ast.error: return None, ast.error

    # Interpret AST
    interpreter = Interpreter()
    context = Context('Program')
    result = interpreter.visit(ast.node, context)

    return result.value, result.error

#endregion






