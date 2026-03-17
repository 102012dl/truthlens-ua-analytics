Slide 01 — Title:
  TruthLens UA Analytics
  AI-платформа верифікації новин та виявлення ІПСО
  102012dl | Neoversity MSCS DS&DA 2026

Slide 02 — Problem (with data):
  9,557 ІПСО-постів у UA Telegram (UNLP 2025)
  5,000+ фактів дезінформації (StopFake)
  15-20 хв ручна верифікація → < 1 сек автоматична

Slide 03 — Solution:
  Hybrid: ML(LinearSVC) + ІПСО(regex) + Source Scoring
  Input: URL або текст → Output: FAKE/REAL/SUSPICIOUS + score

Slide 04 — 7-Level Architecture:
  DATA → PREPROCESSING → TF-IDF → LinearSVC
  → ІПСО DETECTOR → SOURCE SCORER → VERDICT ENGINE

Slide 05 — Datasets:
  ISOT: 39,103 EN articles (train/test 80/20)
  UNLP 2025: 9,557 UA Telegram posts (ІПСО)
  Gold: 31 авторських кейсів (100% accuracy)

Slide 06 — A/B ML Results table:
  Model          | F1     | Latency
  LinearSVC(C=1) | 0.9947 | 12ms  ← WINNER
  RandomForest   | 0.9942 | 45ms
  LinearSVC(0.5) | 0.9931 | 11ms
  LogisticReg    | 0.9881 |  8ms

Slide 07 — ІПСО Detector:
  10 techniques (UNLP 2025)
  Override rule: ipso_count ≥ 2 → FAKE
  Example: "ТЕРМІНОВО!!! ЗСУ ЗДАЛИ!" →
    urgency_injection + military_disinfo + deletion_threat = FAKE

Slide 08 — Source Credibility Formula:
  credibility = 0.35×evidence + 0.25×(1-contradiction)
              + 0.20×consistency + 0.20×prior
  pravda.com.ua=0.92 | riafan.ru=0.05

Slide 09 — Live Demo:
  Screenshot: POST /check → JSON result
  Screenshot: Dashboard with metrics

Slide 10 — Deploy & MLOps:
  Docker Compose | GitHub + GitLab | nmvp1-v1.1.0
  Render.com | MLflow A/B tracking

Slide 11 — Competitive Analysis:
  TruthLens UA | NewsGuard | GDELT | StopFake
  Unique: UA-specific ІПСО + open source + explainable

Slide 12 — SaaS Roadmap:
  v1.0: NMVP1 ✅ | v1.5: UA model | v2.0: Real-time
  Висновок: F1=0.9947, 100% gold accuracy, production-ready
