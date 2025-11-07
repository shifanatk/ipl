IPL Season Winner Predictor
A machine learning project to forecast the Indian Premier League (IPL) champion. This project analyzes mid-season performance metrics and pre-season auction data to predict the probability of each team winning the tournament.

This was submitted as a group project for the course 24AIJ303: Introduction to Machine Learning at the Thangal Kunju Musaliar College of Engineering, Kollam.

🚀 Deployed App
You can access the live Streamlit app here:

https://iplpredictorapp.streamlit.app/

<img width="1911" height="1004" alt="image" src="https://github.com/user-attachments/assets/594ca293-f49e-400d-884a-89992d9e7c5f" />


📖 Abstract
The IPL Season Winner Predictor project forecasts the top four teams and their winning probabilities in the final season using mid-season performance data. The system utilizes the XGBoost algorithm, a powerful ensemble learning method, to build a predictive model.



Instead of directly predicting a single winner, the model focuses on identifying the top four contenders and their respective probabilities, resulting in a more robust and insightful approach. The key finding reveals that mid-season data, combined with auction statistics, can reliably forecast end-season outcomes.



🛠️ Technology Stack
Python: The core programming language.


Pandas & NumPy: For data collection, cleaning, and feature engineering.


Scikit-learn: For data preprocessing and model evaluation.


XGBoost: The primary machine learning algorithm used for prediction.


Streamlit: For building and deploying the interactive web application.


Google Colab: The environment used for model development and training.

⚙️ Methodology
The project follows a systematic data science pipeline:

1. Data Acquisition and Preprocessing

Match Data: Detailed ball-by-ball and match-level records for all IPL seasons were sourced from Cricsheet.



Auction Data: Player auction data from 2013-2025 was collected from various Kaggle datasets.


Cleaning: Data was extensively cleaned, including standardizing team names (e.g., 'Delhi Daredevils' to 'Delhi Capitals') and converting price strings (e.g., '10 Cr') into numerical values.



2. Feature Engineering
The model's core features are calculated for each team, each season, based on a "snapshot" of performance at the halfway point of the tournament.


The key features include:


points_mid_season: Total points a team had at the mid-season mark.


win_pct_mid_season: The team's win percentage at the mid-season mark.


squad_cost_crores: The total amount spent by the team in the auction.



star_player_index: A custom metric counting the number of "star" players on a team (defined as players costing over 8 Crores).


3. Modeling
An XGBoost Classifier was trained on historical data (seasons 2013-2020) to predict a binary target: is_eventual_winner.


The model was specifically tuned to handle the severe class imbalance (only one winner per season) using the scale_pos_weight parameter.


4. Evaluation
The model was evaluated using Top-N Accuracy, which assesses if the actual champion was present in the model's Top-1, Top-2, Top-3, or Top-4 predictions.


This probabilistic approach is more realistic for sports analytics, as it correctly identifies a pool of likely contenders rather than just one winner.

👥 Team Members
This project was submitted in partial fulfillment of the requirements for the B.Tech degree by the following team:


Asna S B [TKM24CA013] 


Muhammed Nihal Noushad [TKM24CA037] 


Rasheeda P V [TKM24CA045] 


Shibin Mahzoom [TKM24CA055] 


Shifana T K [TKM24CA056] 

🎓 Acknowledgements
We extend our sincere gratitude to our project guide and the faculty at the Thangal Kunju Musaliar College of Engineering, Kollam, for their invaluable guidance and support.

Prof. Divya C P (Project Coordinator, Assistant Professor, Dept. of CSE) 

Dr. Aneesh G Nath (Head of the Department, Associate Professor, Dept. of CSE)
