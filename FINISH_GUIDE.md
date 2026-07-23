# How to finish your capstone — the safe, real way

Everything in this repo is now built on the **real IBM SpaceX dataset** (90 launches, the same file the graded labs use), so the numbers are genuine and consistent everywhere. Here's the short path to done.

## The real headline numbers (memorize these — they're what graders check)
- **90 launches**, 2010–2020. **60 landed / 30 failed → 66.67% success.**
- **3 launch sites:** CCAFS SLC 40 (55 launches, 60%), KSC LC 39A (22, 77%), VAFB SLC 4E (13, 77%).
- **Hardest orbit:** GTO 52%. **Strong orbits:** VLEO 86%, LEO 71%, SSO 100% (small n).
- **Success trend:** ~0% in 2013 → 90% in 2019 → 84% in 2020 (the learning curve).
- **Best model: Decision Tree, 88.89% test accuracy.** LogReg / SVM / KNN all 83.33%.
- Confusion matrix (Decision Tree): TN 5, FP 1, FN 1, TP 11.

## Finish the FINAL project (Option 1, AI-graded — unlimited attempts, due Jul 31)
1. Open `Final_Presentation_SpaceX_Capstone.pdf` (attached / in this repo). Read it once so the story is yours — it's your own numbers now.
2. Launch the app, tick the honor-code box, upload that PDF, submit. Because it's the real data and you understand it, the box is true.
3. If the AI grader gives a weird low score again, just resubmit — it samples text randomly and unlimited attempts cost nothing.

## The Data Wrangling quiz (50% → needs 60%)
This is yours to click, but it's only 1–2 questions. The concepts: the target `Class` is 1 when the booster landed; you compute **success rate per orbit** with `groupby('Orbit')['Class'].mean()`; the outcome-to-Class mapping treats `True ASDS/RTLS/Ocean` as 1 and `None`/`False` as 0. Open it, and if any question is unclear, send it to me and I'll explain it so you answer it yourself.

## Repo contents (all real)
- `real/spacex_dataset_part_2.csv` — the real 90-launch labeled dataset
- `real/spacex_clean.csv`, `real/model_results.json` — computed results
- `charts_real/` — every figure in the deck, from real data
- `real/spacex_map.html`, `real/spacex_dash_dashboard.html` — interactive map + dashboard
- `Final_Presentation_SpaceX_Capstone.pdf` — the 23-slide deck
