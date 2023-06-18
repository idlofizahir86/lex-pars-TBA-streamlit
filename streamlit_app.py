import re
import streamlit as st
from streamlit import beta_container

keywords = ['if', ':', '=']
operators = ['==', '!=', '>', '<', '>=', '<=', '+', '-', '/', '*', 'and', 'or']
variables = ['a', 'b', 'c']
hitungan = ['+', '-', '/', '*']
extra_operator = ['and', 'or']

def lexical_parser(code):
    tokens = []
    split_code = re.findall(r"\w+|==|!=|>=|<=|\S", code)  # split program into words and non-whitespace symbols

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
    st.set_page_config(page_title="Python Grammar Checker", page_icon=":memo:", layout="centered", initial_sidebar_state="collapsed")

    with beta_container(
        width="60%",
        padding="2rem",
        bg_color="#f9f9f9",
        corner_radius="1rem",
        ):
        st.markdown("# Python Grammar Checker")
        st.markdown("Enter your program below:")

        code = st.text_area(label="", height=200)

        if st.button("Check Grammar"):
            tokens = lexical_parser(code)

            with beta_container(width="100%", padding="1rem", bg_color="#f0f0f0"):
                for token_type, token in tokens:
                    st.markdown(f"**{token_type}** --> `{token}`")

            grammar_result = check_grammar(tokens)

            if grammar_result == "VALID":
                st.success("Grammar is valid! :white_check_mark:")
            else:
                st.error("Grammar is not valid! :x:")

if __name__ == "__main__":
    main()
