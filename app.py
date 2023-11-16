import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import plotly.express as px
import altair as alt
import numpy as np



def main():
    st.title("Liga Insurance Visualization :oncoming_automobile:")

    logo = '<img src="https://plat.ai/wp-content/themes/platai/assets/images/logo.svg" alt="Plat.AI">'
    st.sidebar.markdown(f"{logo}<h1></h1>", unsafe_allow_html=True)

    # Load Data
    df = pd.read_csv(r"C:\Users\Admin\PycharmProjects\streamlit_project\multi_app\data\sample_forvisuals_semiprocessed.csv")
    liga = pd.read_csv(r"C:\Users\Admin\PycharmProjects\streamlit_project\multi_app\data\grouped_liga.csv")
    market = pd.read_csv(r"C:\Users\Admin\PycharmProjects\streamlit_project\multi_app\data\grouped_market.csv")


    st.header("Plots :bar_chart:")
    st.markdown(
                """
                <style>
                .rainbow-divider {
                    width: 100%;
                    height: 3px;
                    background: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
                    margin: 10px 0;
                    border: none;
                }
                </style>
                <div class="rainbow-divider"></div>
                """,
                unsafe_allow_html=True,
            )


    # Plot 1
    st.subheader("Data Comparison")

    class_a_selected = st.selectbox('Select BM Class A:', df['bmClass'].unique())
    class_b_selected = st.selectbox('Select BM Class B:', df['bmClass'].unique())

    filtered_df = df[(df['bmClass'] == class_a_selected) | (df['bmClass'] == class_b_selected)]

    proportion_df = filtered_df.groupby('bmClass')['scores'].value_counts(normalize=True).reset_index(name='Proportion')
    proportion_df['Proportion'] *= 100

    fig, ax = plt.subplots(figsize=(8, 6))

    for label, data in proportion_df.groupby('bmClass'):
        ax.bar(data['scores'], data['Proportion'], label=label, alpha=0.6)

    ax.set_xlabel('Scores')
    ax.set_ylabel('Proportion')



    ax.set_title('Proportion of Scores for Selected BM Classes')
    ax.legend()

    st.pyplot(fig)

    st.markdown('---')


    # Plot 2


    total = liga['Number of claims'] + market['Number of claims']

    liga['percentage'] = (liga["Number of claims"] / total) * 100

    fig2 = px.bar(liga, x='scores', y='Number of claims', color_discrete_sequence=['orange'],
                 title=f"Claims by Scores: Liga vs Market",
                 labels={'Number of claims': 'Number of claims', 'scores': 'Scores'},
                 height=600)


    market['percentage'] = (market['Number of claims'] / total) * 100

    fig3 = px.bar(market, x='scores', y='Number of claims', color_discrete_sequence=['green'],
                  title=f"Claims by Scores: Liga vs Market",
                  labels={'Number of claims': 'Number of claims', 'scores': 'Scores'},
                  height=600,
                  text='scores')



    fig2.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total score')
    fig2.update_traces(customdata=liga['percentage'])

    fig3.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total score')
    fig3.update_traces(customdata=market['percentage'])


    fig2.add_traces(fig3.data)

    legend_annotations = [
        dict(x=0.9, y=1, xref='paper', yref='paper', showarrow=False,
             text="Liga",
             bgcolor="orange", opacity=0.7, font=dict(color="white"), xanchor='right', yanchor='top'),

        dict(x=0.9, y=0.94, xref='paper', yref='paper', showarrow=False,
             text="Market",
             bgcolor="green", opacity=0.7, font=dict(color="white"), xanchor='right', yanchor='top')
    ]

    fig2.update_layout(annotations=legend_annotations)

    st.plotly_chart(fig2)



    total2 = liga['Number of contracts'] + market['Number of contracts']

    liga['percentage2'] = (liga["Number of contracts"] / total2) * 100
    fig2b = px.bar(liga, x='scores', y='Number of contracts', color_discrete_sequence=['orange'],
                  title=f"Contracts by Scores: Liga vs Market",
                  labels={'Contracts': 'Contracts', 'scores': 'Scores'},
                  height=600)

    market['percentage2'] = (market['Number of contracts'] / total2) * 100

    fig3b = px.bar(market, x='scores', y='Number of contracts', color_discrete_sequence=['green'],
                  title=f"Contracts by Scores: Liga vs Market",
                  labels={'Contracts': 'Contracts', 'scores': 'Scores'},
                  height=600,
                  text='scores')

    fig2b.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total score')
    fig2b.update_traces(customdata=liga['percentage2'])

    fig3b.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total score')
    fig3b.update_traces(customdata=market['percentage2'])

    fig2b.add_traces(fig3b.data)

    legend_annotations2 = [
        dict(x=0.9, y=1, xref='paper', yref='paper', showarrow=False,
             text="Liga",
             bgcolor="orange", opacity=0.7, font=dict(color="white"), xanchor='right', yanchor='top'),

        dict(x=0.9, y=0.94, xref='paper', yref='paper', showarrow=False,
             text="Market",
             bgcolor="green", opacity=0.7, font=dict(color="white"), xanchor='right', yanchor='top')
    ]

    fig2b.update_layout(annotations=legend_annotations2)

    st.plotly_chart(fig2b)

    st.markdown('---')



    # Plot 3
    liga_data = pd.read_csv(r"C:\Users\Admin\PycharmProjects\streamlit_project\multi_app\data\liga.csv")
    market_data = pd.read_csv(r"C:\Users\Admin\PycharmProjects\streamlit_project\multi_app\data\market.csv")
    mean_score1 = liga_data['scores'].mean()
    mean_score2 = market_data['scores'].mean()
    median_score1 = liga_data['scores'].median()
    median_score2 = market_data['scores'].median()

    custom_palette = {"Liga": "orange", "Market": "green"}


    data = {
        'Dataset': ['Liga'] * len(liga_data) + ['Market'] * len(market_data),
        'Scores': list(liga_data['scores']) + list(market_data['scores'])
    }

    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 6))
    ax = sns.boxplot(x='Dataset', y='Scores', data=df,  palette=custom_palette)
    plt.title('Mean & Median Scores of Liga vs Market', loc='left', fontsize=10)
    plt.xlabel('Dataset')
    plt.ylabel('Scores')

    ax.text(0, mean_score1, f"Mean: {mean_score1:.2f}", ha='center', va='bottom')
    ax.text(1, mean_score2, f"Mean: {mean_score2:.2f}", ha='center', va='bottom')
    ax.text(0, median_score1, f"Median: {median_score1:.2f}", ha='center', va='top', color='black', fontsize=10)
    ax.text(1, median_score2, f"Median: {median_score2:.2f}", ha='center', va='bottom', color='black', fontsize=10)




    st.pyplot(plt)

    st.markdown('---')


    # Plot 4

    st.subheader('Proportion by Scores: Liga vs Market')

    liga_check = st.checkbox("Liga")
    market_check = st.checkbox("Market without Liga")

    if liga_check:
        chart = alt.Chart(
            pd.concat([liga.assign(Dataset="Liga")])
        )

        circles = chart.mark_point(size=50).encode(
                x='scores',
                y='proportion',
                color=alt.Color('Dataset', scale=alt.Scale(range=['orange'])),
                tooltip=['scores', 'proportion', 'Dataset']
            )

        lines = chart.mark_line().encode(
            x='scores',
            y='proportion',
            color=alt.Color('Dataset', scale=alt.Scale(range=['orange']))
        )

        chart = (circles + lines).properties(
            width=600,
            height=400
        ).interactive()

    if market_check:
        chart = alt.Chart(
        pd.concat([market.assign(Dataset="Market without Liga")])
    )

        circles = chart.mark_point(size=50).encode(
            x='scores',
            y='proportion',
            color=alt.Color('Dataset', scale=alt.Scale(range=['green'])),
            tooltip=['scores', 'proportion', 'Dataset']
        )

        lines = chart.mark_line().encode(
            x='scores',
            y='proportion',
            color=alt.Color('Dataset', scale=alt.Scale(range=['green']))
        )

        chart = (circles + lines).properties(
            width=600,
            height=400
        ).interactive()

    if liga_check and market_check:
        chart = alt.Chart(
            pd.concat([liga.assign(Dataset="Liga"), market.assign(Dataset="Market without Liga")])
        )

        circles = chart.mark_point(size=50).encode(
            x='scores',
            y='proportion',
            color=alt.Color('Dataset', scale=alt.Scale(range=['orange', 'green'])),
            tooltip=['scores', 'proportion', 'Dataset']
        )

        lines = chart.mark_line().encode(
            x='scores',
            y='proportion',
            color=alt.Color('Dataset', scale=alt.Scale(range=['orange', 'green']))
        )

        chart = (circles + lines).properties(
            width=600,
            height=400
        ).interactive()

    if not liga_check and not market_check:
        st.warning("**Please select a dataset**")

    else:
        pass
        st.altair_chart(chart, use_container_width=True)



    st.markdown('---')



if __name__ == '__main__':
       main()
