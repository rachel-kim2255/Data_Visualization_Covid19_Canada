# 🦠 Coivd-19 in Canada  
**🛠️ Tableau, PowerPoint, Python, SQL**  
<br>
📎 Rachel Kim and 3 others  
📚 Team Project  
📅 Date: 2025.04  
👩‍💻 Role: Dashboard design, Preparing PowerPoint Deck  
<br>
The dashboard addresses our curiosity about “How Canada was affected by Covid 19”. The dashboard highlights key metrics—confirmed cases, confirmed deaths, severity of infections leading to hospitalization, affected occupations and the gender distribution. Additionally, the dashboard explores positivity of recovery trends. This helps us understand the impact of the pandemic across Canada.    
<br>
<br>
🎨 Dashboard Link: https://public.tableau.com/app/profile/ryangwoo.kim/viz/CSIS3860_FinalProject_Group5submission/Dashboard?publish=yes  
<br>

---
## 📂 Methodology Summary
To create the visualizations in our project, we first performed data cleaning and preprocessing tasks, including:

- Reading three different CSV files into memory as Pandas DataFrames  
- Removing empty rows and columns  
- Converting date formats to ISO standard  
- Normalizing province names using a mapping dictionary (e.g., "ON" → "Ontario")  
- Creating an SQL table in SQL Server to match the structure of the cleaned DataFrame  
- Inserting the cleaned and formatted dataset into SQL
  

## Datasets Used

The datasets used to create our visualizations are:

- `data_class.csv` – COVID-19 Canada Dataset  
- `covid_19_data_Canada.csv` – Novel Coronavirus 2019 Dataset - Canada  
- `Public_COVID-19_Canada.csv` – COVID-19 in Canada - Open Data  

These datasets were used to build visualizations including:

- Time-based trend lines  
- Age group comparisons  
- Regional breakdowns  
- Interactive dashboards  

Each chart was designed to explore specific patterns and support insights on the effectiveness of public health responses during the early months of the pandemic.


## Calculated Columns (During Preprocessing)

1. **Age Group**: Categorized the original `Age` column into grouped ranges  
2. **Date and Time**: Unified and standardized date and time formats  
3. **Province**: Cleaned to retain only the province name (removed city data)  
4. **Region**: Grouped provinces into four broader regions — East, West, Central, and Central-West  
5. **Province Abbreviation**: Added standard two-letter codes (e.g., ON, BC, QC)  
6. **Age Numeric**: Mapped age groups to midpoint values (e.g., "30–39" → 35) for analysis


