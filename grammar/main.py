from antlr4 import *
from DallasLexer import DallasLexer
from DallasParser import DallasParser
from LLVMActions import LLVMActions

def main():
    input_stream = FileStream("./test.Dallas")
    lexer = DallasLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DallasParser(token_stream)

    tree = parser.prog()
    llvm_actions = LLVMActions()

    walker = ParseTreeWalker()
    walker.walk(llvm_actions, tree)

if __name__ == '__main__':
    main()