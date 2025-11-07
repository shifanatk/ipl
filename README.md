# 🏆 IPL Season Winner Predictor

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-brightgreen.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-purple.svg)

A group project for the course **24AIJ303: Introduction to Machine Learning** at the Thangal Kunju Musaliar College of Engineering, Kollam.

---

## 🚀 Project Links

* ### [➡️ Try the Live Predictor App](https://iplpredictorapp.streamlit.app/)
* ### [➡️ View the Colab Notebook](https://colab.research.google.com/drive/1tntVaSJGYM4Oa6oDWN4B3Q4QZI_c3wOa?usp=sharing)

---

## 📸 Application Screenshot

<img alt="Screenshot of the IPL Predictor App" src="https://github.com/user-attachments/assets/594ca293-f49e-400d-884a-89992d9e7c5f" />

---

## 🎯 Project Goal

This project uses an **XGBoost** model to predict the probability of an IPL team winning the tournament. The model is unique because it makes its predictions based on **mid-season performance** (at the halfway point) combined with **pre-season auction data**.

---

## 🛠️ How It Works

* **Data:** Match data from [Cricsheet](https://cricsheet.org/) and auction data from [Kaggle](https://www.kaggle.com/).
* **Model:** An `XGBClassifier` trained to predict a single target: `is_eventual_winner`.
* **Key Features:** The model's "brain" is built on four engineered features:
    * `points_mid_season`: Points at the halfway mark.
    * `win_pct_mid_season`: Win percentage at the halfway mark.
    * `squad_cost_crores`: Total cost of the team from the auction.
    * `star_player_index`: Number of players on the team costing over 8 Crores.
* **Evaluation:** We use **Top-4 Accuracy** to check if the actual champion was in our model's top 4 predictions, which is a more realistic metric for sports analytics.

---

## 👥 Team Members

* **Asna S B** `[TKM24CA013]`
* **Muhammed Nihal Noushad** `[TKM24CA037]`
* **Rasheeda P V** `[TKM24CA045]`
* **Shibin Mahzoom** `[TKM24CA055]`
* **Shifana T K** `[TKM24CA056]`
