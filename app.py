import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb  # Required to load the model

# --- 1. Load Model and Data (Cached for performance) ---
# @st.cache_data ensures we only load these files once
@st.cache_data
def load_data():
    try:
        model = joblib.load('ipl_xgb_model.joblib')
        columns = joblib.load('model_feature_columns.joblib')
        matches_df = pd.read_csv('matches_data.csv')
        auction_df = pd.read_csv('auction_data.csv')
        
        # Convert date columns back to datetime
        matches_df['Date'] = pd.to_datetime(matches_df['Date'])
        matches_df['year'] = matches_df['Date'].dt.year
        return model, columns, matches_df, auction_df
    except FileNotFoundError:
        st.error("ERROR: One or more required files not found. (model, columns, matches_data, or auction_data)")
        st.stop()

# --- 2. The Prediction Function (Copied from your notebook) ---
# We pass the data in as arguments instead of using global variables
def get_live_predictions(year_to_predict, at_match_number, model, feature_cols, all_matches_df, all_auction_df):
    
    # --- 1. Get all matches for the season ---
    # Note: Using 'all_matches_df' and 'all_auction_df' passed into the function
    season_matches_all = all_matches_df[all_matches_df['year'] == year_to_predict].copy()
    season_auction = all_auction_df[all_auction_df['year'] == year_to_predict].copy()

    # --- 2. Create the "snapshot" in time ---
    current_matches = season_matches_all.iloc[:at_match_number]

    if len(current_matches) == 0:
        return "Not enough matches have been played yet."

    # --- 3. Calculate Live Features ---
    live_features_list = []
    teams_in_season = pd.concat([season_matches_all['Team1'], season_matches_all['Team2']]).unique()

    for team in teams_in_season:
        team_matches_fh = current_matches[(current_matches['Team1'] == team) | (current_matches['Team2'] == team)]
        wins = (team_matches_fh['WinningTeam'] == team).sum()
        points = wins * 2
        win_pct = wins / len(team_matches_fh) if len(team_matches_fh) > 0 else 0

        team_auction_players = season_auction[season_auction['team'] == team]
        squad_cost = team_auction_players['price'].sum() / 1_00_00_000 
        star_player_index = (team_auction_players['price'] > 8_00_00_000).sum() 

        live_features_list.append({
            'team': team,
            'points_mid_season': points,
            'win_pct_mid_season': win_pct,
            'squad_cost_crores': squad_cost,
            'star_player_index': star_player_index,
        })

    live_features_df = pd.DataFrame(live_features_list)

    # --- 4. Prepare Data for the Model ---
    # Use the 'feature_cols' list we loaded
    X_live = live_features_df[feature_cols]

    # --- 5. Make Live Predictions ---
    # Use the 'model' we loaded
    live_probs = model.predict_proba(X_live)[:, 1]

    # --- 6. Format and Return the Output ---
    prediction_results = live_features_df[['team']].copy()
    prediction_results['win_probability'] = live_probs
    
    # Sort and format for display
    prediction_results = prediction_results.sort_values('win_probability', ascending=False)
    prediction_results['win_probability'] = prediction_results['win_probability'].apply(lambda x: f"{x:.2%}")
    
    return prediction_results.reset_index(drop=True)

# --- 3. Build the Streamlit UI ---
st.set_page_config(page_title="IPL Winner Predictor", layout="wide")
st.title("🏆 IPL Tournament Winner Predictor")
st.write("This app uses an XGBoost model to predict the tournament winner based on mid-season performance and auction data.")

# Load all files
xgb_model, model_columns, matches, auction_df = load_data()

# --- User Inputs ---
st.sidebar.header("Select Prediction Point")

# Get valid years from the data (2013 onwards, as per your model)
valid_years = sorted(matches[matches['year'] >= 2013]['year'].unique(), reverse=True)
selected_year = st.sidebar.selectbox(
    "Select Year:",
    valid_years
)

# --- Calculate Snapshot Match Numbers ---
if selected_year:
    season_matches = matches[matches['year'] == selected_year]
    total_matches_in_season = len(season_matches)
    
    # We assume the last 4 matches are playoffs
    # This logic matches your notebook (e.g., Match 70 for a 74-game season)
    league_stage_end = total_matches_in_season - 4
    halfway_point = league_stage_end // 2
    three_quarter_point = int(league_stage_end * 0.75)

    snapshot_options = {
        f"Halfway (After Match {halfway_point})": halfway_point,
        f"75% Mark (After Match {three_quarter_point})": three_quarter_point,
        f"End of League (After Match {league_stage_end})": league_stage_end
    }

    selected_snapshot_name = st.sidebar.radio(
        "Select Snapshot:",
        snapshot_options.keys()
    )
    
    selected_match_number = snapshot_options[selected_snapshot_name]

    # --- Run Prediction ---
    if st.sidebar.button("Predict Winner"):
        st.header(f"Predictions for {selected_year}")
        st.subheader(f"Based on data up to: {selected_snapshot_name}")

        with st.spinner(f"Calculating probabilities for {selected_year}..."):
            # Call the prediction function
            predictions_df = get_live_predictions(
                selected_year,
                selected_match_number,
                xgb_model,
                model_columns,
                matches,
                auction_df
            )
            
            # Display the results
            st.dataframe(predictions_df, use_container_width=True)
            
            # Highlight the top pick
            top_pick = predictions_df.iloc[0]
            st.success(f"**Top Pick to Win:** {top_pick['team']} ({top_pick['win_probability']})")
            
else:
    st.info("Loading data... please wait.")