## Automatic Field of Work Categorization Using NLP

This project applies Natural Language Processing (NLP) techniques to automate the categorization of the "Field of Work" column from questionnaire data stored in an Excel worksheet. The developed solution is flexible and can be adapted to analyze other columns with minimal modifications. The approach ensures proper handling of unavailable data entries and utilizes translation for multilingual processing.

---

### Features

- **Automatic Categorization**:
  - Uses an efficient small-scale embedding model (all-MiniLM-L6-v2) to iteratively refine hierarchical category matching.
  - Handles up to four hierarchical levels of categories, with each category having at least three child sub-categories to balance comprehensiveness and depth.
  - Processes mixed Chinese-English entries using the translation model Helsinki-NLP/opus-mt-zh-en.

- **Preprocessing**:
  - Filters and processes missing or invalid data entries such as N/A, NA, or empty cells, ensuring robust performance.

- **Data Structure**:
  - The project defines standard industrial sector categories with up to four levels, providing a hierarchical framework for precise categorization.

- **Reproducibility**:
  - Modular code design for easy adaptation and scalability to handle different datasets or NLP tasks.
---

### How It Works

1. **Input Data**:
   - Reads the Excel worksheet with questionnaire responses.
   - Encodes all the categories and sub-categories of all hierarchical levels to create embeddings for effective matching and refinement.

2. **Translation**:
   - Uses the Helsinki-NLP/opus-mt-zh-en model to translate Chinese entries into English.

3. **Categorization**:
   - Employs the all-MiniLM-L6-v2 model to map each entry to a hierarchical category by refining matches across levels.

4. **Handling Missing Data**:
   - Filters invalid entries (e.g., N/A, NA, empty cells) to avoid classification errors.

5. **Output**:
   - Generates an updated Excel worksheet (df_excel_output.xlsx) with additional columns:
     - Unified_Status
     - Unified_Field_of_Work

---

### Future Directions

- **Remote Server Computation**:
  - Explore running computation-intensive NLP tasks on remote servers like Google Colab or AWS.

- **Adaptive Categories**:
  - Conduct global semantic identification to dynamically establish hierarchical categories that better capture real-world complexities when scaling data.

- **Enhanced Models**:
  - Utilize local open-sourced or commercial large language models (LLMs) or access advanced APIs to improve category representation and matching accuracy.

---

### License

- **Code**: Open License
- **Example Data**: The questionnaire data provided in this repository (6th HKU+ Alumni Talk(1-242).xlsx) is **not licensed for distribution**. It is included solely for demonstrative purposes.

---

### Dependencies

To install all required dependencies, run:
```bash
pip install -r requirements.txt
```

---

### Outlook

Future improvements aim to optimize computational efficiency and improve the accuracy of hierarchical categorizations, aligning the approach more closely with real-world complexities and large-scale data needs.

--- 

For more information or issues, feel free to contact the repository owner. [Visit Ju Wu's Website for Contact Info](https://juwu-19.github.io/neo/)

