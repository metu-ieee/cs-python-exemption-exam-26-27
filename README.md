# Python 101 — Exemption Exam: "Society OS" (METU IEEE CS)

Welcome to the official **METU IEEE Computer Society** Python 101 Exemption Exam. Passing this exam proves your proficiency in core Python mechanics and object-oriented programming, exempting you from the beginner education track and qualifying you as an **Active Member**.

## Exam Rules & The 3-Push Cap
* **Push Limit (3 Graded Pushes Max):** You have a strict limit of **3 pushes** to the `main` branch.
* **Highest Score Wins:** Your official exam grade is the **highest score** achieved across your 3 pushes (`max(Push 1, Push 2, Push 3)`). Any push after your 3rd attempt will be automatically ignored by the autograder.
* **Test Locally First:** Do not burn a push to test syntax! Run the local sanity script in your terminal as many times as you want before pushing:
  ```bash
  python exam/local_tests.py
  ```
* **Read-Only Integrity: Do NOT modify** `exam/read_only_base.py` or `exam/read_only_helpers.py`. The cloud autograder verifies cryptographic SHA-256 hashes of both files before grading; any modification results in an automatic `0/100`.

## How to Start

1. Click the green **Code** button at the top right of this repository.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Open `exam/exam_specifications.md` and read the architectural specifications carefully.
4. Implement your solutions inside `exam/student_classes.py` and `exam/student_functions.py`.
5. Run python `exam/local_tests.py` in the terminal to verify your baseline logic.
6. When ready to submit an official attempt, commit and push your changes (`git push origin main`), then open the Actions tab on GitHub to view your Attempt Scorecard.
