from scipy.stats import randint, uniform

# LIGHTGM_PARAMS={
#     'n_estimators' : randint(100, 500),
#     'max_depth' : randint(5, 50),
#     'learning_rate' : uniform(0.01, 0.2),
#     'num_leaves' : randint(20, 100),
#     'boosting_type' : ['gbdt', 'dart', 'goss']
# }

# RANDOM_SEARCH_PARAMS = {
#     'n_iter' : 4,
#     'cv' : 2,
#     'n_jobs' : -1,
#     'verbose' : 2,
#     'random_state' : 42,
#     'scoring' : 'accuracy'
# }

LIGHTGM_PARAMS = {
    'n_estimators': randint(100, 300),         # Fewer trees for speed
    'max_depth': randint(5, 25),               # Shallower trees
    'learning_rate': uniform(0.01, 0.1),       # Slightly lower max
    'num_leaves': randint(20, 50),             # Smaller leaves for small data
    'boosting_type': ['gbdt', 'dart']          # Remove 'goss' for now
    # Add 'top_rate':[0.1,0.2], 'other_rate':[0.1,0.2] if using goss
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 4,
    'cv': 2,
    'n_jobs': 1,      # Try 1 or 2 to avoid oversubscription
    'verbose': 2,
    'random_state': 42,
    'scoring': 'accuracy'
}
