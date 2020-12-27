import streamlit as st
import pandas as pd
import joblib

st.title('Протокол № 42 от 29.12.2020')
r'''
1. Наименоание заказчика: 
2. Наименовние объекта контроля: силовой трансформатор ТРДН-40000/110
3. Место отбора пробы: Т-1, бак РПН
4. Дата и время доставки: 27.12.2020 13:00
5. Дата проведения работ: 27.12.2020 – 28.12.2020
6. Цель испытания: контроль влагосодержания трансформатороного масла, анализ примесей
7. Условия проведения испытаний: температура в помещениии 23 градуса Цельсия, влажность 54%, давление 749 мм.рт.ст.
8. Дополнительные сведения: отбор проб Лаборатория "MADE"
9. Средства измерения и испытательное оборужование:
'''
measurement = pd.DataFrame({'Наименование средства измерения': ['Весы ВЛТЭ-510'],
                   'Зав. номер ': ['Д15 328'],
                   'Инвертарный номер': ['08/432562/45215'],
                   'Погрешность СИ': ['+/ 50 мг'],
                   'Дата последней поверки': ['22.11.2019']})
# set first td and first th of every table to not display
st.markdown("""
<style>
table td:nth-child(1) {
    display: none
}
table th:nth-child(1) {
    display: none
}
</style>
""", unsafe_allow_html=True)
st.table(measurement)
st.header('Результы аналиа отбора масла')
active_rows = ['moisture',
               'acid',
               'oil_tangent',
               'ionol',
               'flush_point',
               'hydrogen',
               'metan',
               'eten',
               'etan',
               'etin',
               'cardon_dioxid',
               'carbon_oxid']
moisture = st.number_input('Влагосодержание % масс, г/т', value=9.6)
acid = st.number_input('Кислотное число, мг КОН/г масла', value=0.01)
oil_tangent = st.number_input('Содержание воднорастворимых кислот и щелочей мг КОН/ г масла', value=0.15, format='%f')
ionol = st.number_input('Содержание ионола мг/г', value=0.288, format='%f')
flush_point = st.number_input('Температура вспышки в закрытом тигле, град. Цельсия', value=136.0, format='%f')
r'Содержание $$H_2$$, мг/г'
hydrogen = st.number_input(r'водород, %', value=0.000987, format='%f')
r'''Содержание $$CH_4$$'''
metan = st.number_input('метан %', value=0.00009, format='%f')
r'''Содержание $$C_2H_4$$'''
eten = st.number_input('этилен %', value=0.000138, format='%f')
r'''Содержание $$C_2H_6$$'''
etan = st.number_input('этан, %', value=0.00016, format='%f')
r'''Содержание $$C_2H_2$$'''
etin = st.number_input('ацэтилен, %', value=0, format='%f')
r'''Содержание $$CO_2$$'''
cardon_dioxid = st.number_input('диоксид углерода, %', value=0.054551, format='%f')
r'''Содержание $$CO$$'''
carbon_oxid = st.number_input('углекислый газ, %', value=0.012935, format='%f')
model = joblib.load("transformer_classifier.pkl")
if st.button('Проверить состояние трансформатора'):
    dataset = [moisture,
               acid,
               oil_tangent,
               ionol,
               flush_point,
               hydrogen,
               metan,
               eten,
               etan,
               etin,
               cardon_dioxid,
               carbon_oxid]
    state = model.predict(dataset)
    if state == 'good':
        state = 'Хорошее'
    if state == 'satisfactory':
        state = 'удовлетворительное'
    if state == 'unsatisfactory':
        state = 'неудовлетвориельное'
    if state == 'unserviceable':
        state = 'непригоден к использованию'
    st.write(f'Текущее состояние трансформатора  **_{state}_**')
