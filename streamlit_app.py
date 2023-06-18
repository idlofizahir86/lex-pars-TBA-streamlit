import streamlit as st
import re

keywords = ['if', ':']
operators = ['==', '!=', '>', '<', '>=', '<=', '+', '-', '/', '*', 'and', 'or']
variables = ['a', 'b', 'c']
hitungan = ['+', '-', '/', '*']
extra_operator = ['and', 'or']

def lexical_parser(code):
    tokens = []
    split_code = re.findall(r'\w+|==|!=|>|<|>=|<=|\S', code)  # Memperbarui pola regex

    for token in split_code:
        if token in keywords:
            tokens.append(('Keyword', token))
        elif token in operators:
            tokens.append(('Operator', token))
        elif token in variables:
            tokens.append(('Variable', token))
        else:
            tokens.append(('Unknown', token))

    return tokens

def check_grammar(tokens):
    # Grammar checking logic
    if tokens[0][1] != 'if':
        return "Grammar is not valid"
    
    if tokens[1][1] not in variables:
        return "Grammar is not valid"
    
    if tokens[2][1] not in operators:
        return "Grammar is not valid"
    
    if tokens[3][1] not in variables:
        return "Grammar is not valid"
    
    if tokens[4][1] not in extra_operator and tokens[4][1] != ':':
        return "Grammar is not valid"
    
    if tokens[4][1] == ':':
        if tokens[5][1] not in variables:
            return "Grammar is not valid"
        
        if tokens[6][1] != '=':
            return "Grammar is not valid"
        
        if tokens[7][1] not in variables:
            return "Grammar is not valid"
        
        if tokens[8][1] not in hitungan:
            return "Grammar is not valid"
        
        if tokens[9][1] not in variables:
            return "Grammar is not valid"
    
    elif tokens[4][1] in extra_operator:
        if tokens[5][1] not in variables:
            return "Grammar is not valid"
        
        if tokens[6][1] not in operators:
            return "Grammar is not valid"
        
        if tokens[7][1] not in variables:
            return "Grammar is not valid"
        
        if tokens[8][1] != ':':
            return "Grammar is not valid"
        
        if tokens[9][1] not in variables:
            return "Grammar is not valid"
        
        if tokens[10][1] != '=':
            return "Grammar is not valid"
        
        if tokens[11][1] not in variables:
            return "Grammar is not valid"
        
        if tokens[12][1] not in hitungan:
            return "Grammar is not valid"
        
        if tokens[13][1] not in variables:
            return "Grammar is not valid"

    return "Grammar is valid"

def main():
    st.title("Lexical Parser and Grammar Checker")
    st.write("Enter a Python program in the text area below:")

    code = st.text_area("Program Code", height=200)
    if st.button("Check Grammar"):
        tokens = lexical_parser(code)

        for token_type, token in tokens:
            st.write(f"{token_type} --> `{token}`")

        grammar_result = check_grammar(tokens)

        if grammar_result == "Grammar is valid":
            st.success("Grammar is valid! ✅")
            st.write("Your code follows the valid grammar.")
        else:
            st.error("Grammar is not valid! ❌")
            st.write("Your code does not follow the valid grammar.")

if __name__ == "__main__":
    main()
