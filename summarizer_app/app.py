import streamlit as st

# Additional Pkgs/Summarization Pkgs
import nltk
nltk.download('punkt')

# TextRank Algorithm
from gensim.summarization import summarize

# LexRank Algorithm
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# EDA Pkgs
import pandas as pd

# Data visualization 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # TkAgg # Backend
# import seaborn as sns
# import plotly.express as px
import altair as alt

# Fxn for LexRank Summarization
# Function for Sumy Summarization
def sumy_summarizer(docx, num=2):
    parser = PlaintextParser.from_string(docx,Tokenizer('english'))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,num)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

# Evaluate Summary 
from rouge import Rouge
def evaluate_summary(summary, reference):
    r = Rouge()
    eval_score = r.get_scores(summary,reference)
    # convert the result to a dataframe (eval_score results come in as a dictionary)
    eval_score_df = pd.DataFrame(eval_score[0])
    return eval_score_df



def main():
    """ A Simpple Summarization NLP App"""
    title_html = '<h1 style="background-color:#333333; text-align: center; border-radius: 8px;"> Summarization App</h1>'
    st.markdown(title_html,unsafe_allow_html=True)    

    menu = ['Home', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Summarization')

        raw_text = st.text_area('Enter text here')
        
        if st.button('summarize'):
            try:
            #if raw_text:
                with st.expander('Original Text'):
                    st.write(raw_text)
                c1, c2 = st.columns([0.5,0.5])
                with c1:
                    with st.expander('LexRank Summary'):
                        my_summary = sumy_summarizer(raw_text)
                        document_len = {'Original':len(raw_text),'Summary':len(my_summary)}
                        st.write(document_len)
                        st.write(my_summary)
                        st.info('Rouge Score')
                        score = evaluate_summary(my_summary,raw_text)
                        #st.write(score.T)
                        st.write(score) # or st.dataframe(score)
                        score['metrics']= score.index
                        #st.write(score)
                        c = alt.Chart(score).mark_bar().encode(x='metrics',y='rouge-1')
                        st.altair_chart(c)

                with c2:
                    with st.expander('TextRank Summary'):
                        my_summary = summarize(raw_text)
                        document_len = {'Original':len(raw_text),'Summary':len(my_summary)}
                        st.write(document_len)
                        st.write(my_summary)
                        st.info('Rouge Score')
                        score = evaluate_summary(my_summary,raw_text)
                        st.write(score)
                        score['metrics']= score.index
                        c = alt.Chart(score).mark_bar().encode(x='metrics',y='rouge-1')
                        st.altair_chart(c)  
            except:
            # else:
                st.warning('No text is available')                
    else:
        st.subheader('About')



if __name__ == '__main__':
    main()