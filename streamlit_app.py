import re
import streamlit as st

keywords = ['if', ':']
operators = ['==', '!=', '>', '<', '>=', '<=', '+', '-', '/', '*', 'and', 'or']
variables = ['a', 'b', 'c']
hitungan = ['+', '-', '/', '*']
extra_operator = ['and', 'or']

def lexical_parser(code):
    tokens = []
    split_code = re.findall(r'\w+|\S', code)  # split program into words and non-whitespace symbols

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
    if tokens[0][1] != 'if':
        return "INVALID"

    if tokens[1][1] not in variables:
        return "INVALID"

    if tokens[2][1] not in operators:
        return "INVALID"

    if tokens[3][1] not in variables:
        return "INVALID"

    if tokens[4][1] not in extra_operator and tokens[4][1] != ':':
        return "INVALID"

    if tokens[4][1] == ':':
        if tokens[5][1] not in variables:
            return "INVALID"

        if tokens[6][1] != '=':
            return "INVALID"

        if tokens[7][1] not in variables:
            return "INVALID"

        if tokens[8][1] not in hitungan:
            return "INVALID"

        if tokens[9][1] not in variables:
            return "INVALID"

    elif tokens[4][1] in extra_operator:
        if tokens[5][1] not in variables:
            return "INVALID"

        if tokens[6][1] not in operators:
            return "INVALID"

        if tokens[7][1] not in variables:
            return "INVALID"

        if tokens[8][1] != ':':
            return "INVALID"

        if tokens[9][1] not in variables:
            return "INVALID"

        if tokens[10][1] != '=':
            return "INVALID"

        if tokens[11][1] not in variables:
            return "INVALID"

        if tokens[12][1] not in hitungan:
            return "INVALID"

        if tokens[13][1] not in variables:
            return "INVALID"

    return "VALID"

def main():
    st.title("Python Grammar Checker")
    code = st.text_area("Masukkan program")

    if st.button("Check Grammar"):
        tokens = lexical_parser(code)

        for token_type, token in tokens:
            st.write(f"{token_type} --> {token}")

        result = check_grammar(tokens)
        st.write("Grammar:", result)

if __name__ == "__main__":
    main()
