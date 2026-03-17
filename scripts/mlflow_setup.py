"""MLflow + DagsHub setup for TruthLens UA Analytics."""
import mlflow, os

def setup_tracking(use_dagshub=False):
    """Configure MLflow tracking."""
    if use_dagshub:
        import dagshub
        dagshub.init(
            repo_owner="102012dl",
            repo_name="truthlens-ua-analytics",
            mlflow=True
        )
        print("MLflow -> DagsHub tracking enabled")
    else:
        mlflow.set_tracking_uri("mlruns/")
        mlflow.set_experiment("truthlens-ua-analytics")
        print("MLflow -> local tracking enabled")

def log_baseline_run(metrics: dict, params: dict):
    """Log a baseline experiment run."""
    with mlflow.start_run(run_name="baseline-linearsvc"):
        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        print(f"Run logged: {mlflow.active_run().info.run_id}")

if __name__ == "__main__":
    setup_tracking(use_dagshub=False)
    log_baseline_run(
        metrics={"f1_weighted": 0.9947, "accuracy": 0.9942,
                 "precision": 0.9927, "recall": 0.9967, "latency_ms": 12},
        params={"model": "LinearSVC", "C": 1.0,
                "max_features": 50000, "ngram_range": "(1,2)",
                "dataset": "ISOT", "samples": 39103}
    )
