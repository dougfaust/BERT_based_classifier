CONFIG = {
    "files": {
        "TRAINING_DATA": 'smile-annotations-final.csv',
        "MODEL_DIR": 'Models/'
    },
    "model_selection": {
        "TEST_FRACTION": 0.15,
        "TRAIN_TEST_SPLIT_SEED": 1234
    },
    "train": {
        "TRAIN_BATCH_SIZE": 8,  # cpu maybe 4, good gpu 32
        "EPOCHS": 10,
        "LEARNING_RATE": 1e-5, # BERT paper says 2e-5 to 5e-5
        "EPS": 1e-8
    }
}