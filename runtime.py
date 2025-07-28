
#region ERRORS

class Error:
    def __init__(self, position_start, position_end, error_name, details):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        return f"""{self.error_name}: {self.details}
File: {self.position_start.file_name}
Line {self.position_start.line + 1}, character {self.position_start.column + 1}"""
    
    def __repr__(self) -> str:
        return self.as_string()
    
class IllegalCharacterError(Error):
    def __init__(self, position_start, position_end, details):
        super().__init__(position_start, position_end, 'Illegal Character', details)

#endregion

#region POSITION

class Position:
    def __init__(self, index, line, column, file_name = None, file_text = None):
        self.index = index
        self.line = line
        self.column = column
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_character=None):
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

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_ADD = "ADD"
TT_SUBTRACT = "SUBTRACT"
TT_MULIPLY = "MULTIPLY"
TT_DIVIDE = "DIVIDE"
TT_OPEN_PARENTHESIS = "OPEN_PARENTHESIS"
TT_CLOSE_PARENTHESIS = "CLOSE_PARENTHESIS"

class Token:
    def __init__(self, type_, value = None):
        self.type = type_
        self.value = value

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
                tokens.append(Token(TT_ADD))
            elif self.current_character == '-':
                tokens.append(Token(TT_SUBTRACT))
            elif self.current_character == '*':
                tokens.append(Token(TT_MULIPLY))
            elif self.current_character == '/':
                tokens.append(Token(TT_DIVIDE))
            elif self.current_character == '(':
                tokens.append(Token(TT_OPEN_PARENTHESIS))
            elif self.current_character == ')':
                tokens.append(Token(TT_CLOSE_PARENTHESIS))
            else:
                character = self.current_character

                position_start = self.position.copy()
                self.advance()
                position_end = self.position.copy()

                return [], IllegalCharacterError(position_start, position_end, character)

            self.advance()

        return tokens, None
    
    def make_number(self):
        number_string = ''
        dot_count = 0

        while self.current_character != None and self.current_character in DIGITS + '.':
            if self.current_character == '.':
                if dot_count == 1: break

                dot_count += 1
                number_string += '.'
            else:
                number_string += self.current_character

            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(number_string))
        else:
            return Token(TT_FLOAT, float(number_string))
        
#endregion

#region RUN

def run(file_name, text):
    lexer = Lexer(file_name, text)
    tokens, error = lexer.make_tokens()

    return tokens, error

#endregion






