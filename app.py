import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px
import altair as alt
import numpy as np




def main():
    st.title("Liga Insurance Visualization :oncoming_automobile:")

    logo = '<img src="https://plat.ai/wp-content/themes/platai/assets/images/logo.svg" alt="Plat.AI">'
    st.sidebar.markdown(f"{logo}<h1></h1>", unsafe_allow_html=True)

    # Load Data
    df = pd.read_csv(r"C:\Users\Adrak3\PycharmProjects\streamlit_project\multi_app\data\main_data_semi_preprocessed.csv")
    rgs = pd.read_csv(r"C:\Users\Adrak3\PycharmProjects\streamlit_project\multi_app\data\grouped_rgs.csv")
    chrgs = pd.read_csv(r"C:\Users\Adrak3\PycharmProjects\streamlit_project\multi_app\data\grouped_chrgs.csv")



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
    st.subheader("Data Comparison")

    selected_bm_class = st.selectbox('Select BM class', df['bmClass'].unique())
    filtered_df = df[df['bmClass'] == selected_bm_class]

    score_counts = filtered_df['scores'].value_counts().reset_index()
    score_counts.columns = ['scores', 'count']

    total_count = len(filtered_df)
    score_counts['percentage'] = (score_counts['count'] / total_count) * 100

    # Plot 1
    fig = px.bar(score_counts, x='scores', y='percentage', color='percentage',
                 title=f'Proportion of Scores for BM classes: {selected_bm_class}',
                 labels={'percentage': 'Percent %', 'scores': 'Scores'},
                 height=600,
                 text='scores')
    fig.update_layout(barmode='stack', xaxis_tickangle=-45)

    yticks = score_counts['scores'].tolist()
    plt.yticks(range(len(yticks)), yticks)

    st.plotly_chart(fig)

    st.markdown('---')



    # Plot 2

    rgs['percentage'] = (rgs["Number of claims"] / rgs['Number of claims'].sum()) * 100
    fig2 = px.bar(rgs, x='scores', y='Number of claims', color_discrete_sequence=['orange'],
                 title=f"Claims by Scores: Liga vs Market",
                 labels={'Number of claims': 'Number of claims', 'scores': 'Scores'},
                 height=600)


    chrgs['percentage'] = (chrgs['Number of claims'] / chrgs['Number of claims'].sum()) * 100

    fig3 = px.bar(chrgs, x='scores', y='Number of claims', color_discrete_sequence=['green'],
                  title=f"Claims by Scores: Liga vs Market",
                  labels={'Number of claims': 'Number of claims', 'scores': 'Scores'},
                  height=600,
                  text='scores')



    fig2.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total')
    fig2.update_traces(customdata=rgs['percentage'])

    fig3.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total')
    fig3.update_traces(customdata=chrgs['percentage'])


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

    rgs['percentage2'] = (rgs["Number of contracts"] / rgs['Number of contracts'].sum()) * 100
    fig2b = px.bar(rgs, x='scores', y='Number of contracts', color_discrete_sequence=['orange'],
                  title=f"Contracts by Scores: Liga vs Market",
                  labels={'Contracts': 'Contracts', 'scores': 'Scores'},
                  height=600)

    chrgs['percentage2'] = (chrgs['Number of contracts'] / chrgs['Number of contracts'].sum()) * 100

    fig3b = px.bar(chrgs, x='scores', y='Number of contracts', color_discrete_sequence=['green'],
                  title=f"Contracts by Scores: Liga vs Market",
                  labels={'Contracts': 'Contracts', 'scores': 'Scores'},
                  height=600,
                  text='scores')

    fig2b.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total')
    fig2b.update_traces(customdata=rgs['percentage'])

    fig3b.update_traces(marker_opacity=0.7, marker_line_width=0,
                       hovertemplate='%{y} <br>%{customdata:.2f}% of total')
    fig3b.update_traces(customdata=chrgs['percentage'])

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
    rgs_data = pd.read_csv(r"C:\Users\Adrak3\PycharmProjects\streamlit_project\multi_app\data\rgs.csv")
    chrgs_data = pd.read_csv(r"C:\Users\Adrak3\PycharmProjects\streamlit_project\multi_app\data\chrgs.csv")
    mean_score1 = rgs_data['scores'].mean()
    mean_score2 = chrgs_data['scores'].mean()

    custom_palette = {"Liga": "orange", "Market": "green"}


    data = {
        'Dataset': ['Liga'] * len(rgs_data) + ['Market'] * len(chrgs_data),
        'Scores': list(rgs_data['scores']) + list(chrgs_data['scores'])
    }

    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 6))
    ax = sns.boxplot(x='Dataset', y='Scores', data=df,  palette=custom_palette)
    plt.title('Mean Scores of Liga vs Market', loc='left', fontsize=10)
    plt.xlabel('Dataset')
    plt.ylabel('Scores')

    ax.text(0, mean_score1, f"Mean: {mean_score1:.2f}", ha='center', va='bottom')
    ax.text(1, mean_score2, f"Mean: {mean_score2:.2f}", ha='center', va='bottom')

    st.pyplot(plt)

    st.markdown('---')


    # Plot 4

    st.subheader('Proportion by Scores: Liga vs Market')

    chart = alt.Chart(
        pd.concat([rgs.assign(Dataset="Liga"), chrgs.assign(Dataset="Market")])
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

    st.altair_chart(chart, use_container_width=True)

    st.markdown('---')



if __name__ == '__main__':
       main()
