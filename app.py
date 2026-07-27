print("Running this app.py")
import sqlite3
from datetime import datetime
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "fitness_app_secret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("fitness.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()


        conn.close()

        if user:
            session["user_id"] = user[0]
            return redirect(url_for("dashboard"))
        else:
            return render_template(
                "login.html",
                error="Invalid email or password. Please try again.",
                email=email
            )

    return render_template("login.html")
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        age = request.form["age"]
        height = request.form["height"]
        weight = request.form["weight"]
        goal = request.form["goal"]

        conn = sqlite3.connect("fitness.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users
        (name, email, password, age, height, weight, goal)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, email, password, age, height, weight, goal))

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    user_id = session["user_id"]

    cursor.execute("""
        SELECT name
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    if user:
        name = user[0]
    else:
        name = "User"

    return render_template(
        "dashboard.html",
        name=name
    )
@app.route("/add_workout", methods=["GET", "POST"])
def add_workout():

    if request.method == "POST":
        exercise = request.form["exercise"]

    return render_template("add_workout.html")
@app.route("/chest")
def chest():

    session_id = request.args.get("session_id")
    print("Session:", session_id)

    exercises = [
        {
            "name": "Bench Press",
            "url": url_for(
                "exercise",
                exercise_name="bench-press",
                session_id=session_id,
                muscle_group="Chest"
            )
        },
        {
            "name": "Incline Dumbbell Press",
            "url": url_for(
                "exercise",
                exercise_name="incline-dumbbell-press",
                session_id=session_id,
                muscle_group="Chest"
            )
        },
        {
            "name": "Chest Fly",
            "url": url_for(
                "exercise",
                exercise_name="chest-fly",
                session_id=session_id,
                muscle_group="Chest"
            )
        },
        {
            "name": "Push-ups",
            "url": url_for(
                "exercise",
                exercise_name="push-ups",
                session_id=session_id,
                muscle_group="Chest"
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Chest",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/triceps")
def triceps():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Tricep Pushdown",
            "url": url_for(
                "exercise",
                exercise_name="tricep-pushdown",
                session_id=session_id,
                muscle_group="Triceps"
            )
        },
        {
            "name": "Overhead Tricep Extension",
            "url": url_for(
                "exercise",
                exercise_name="overhead-tricep-extension",
                session_id=session_id,
                muscle_group="Triceps"
            )
        },
        {
            "name": "Skull Crusher",
            "url": url_for(
                "exercise",
                exercise_name="skull-crusher",
                session_id=session_id,
                muscle_group="Triceps"
            )
        },
        {
            "name": "Close Grip Bench Press",
            "url": url_for(
                "exercise",
                exercise_name="close-grip-bench-press",
                session_id=session_id,
                muscle_group="Triceps"
            )
        },
        {
            "name": "Bench Dips",
            "url": url_for(
                "exercise",
                exercise_name="bench-dips",
                session_id=session_id,
                muscle_group="Triceps"
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Triceps",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/back")
def back():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Lat Pulldown",
            "url": url_for(
                    "exercise",
                    exercise_name="lat-pulldown",
                    session_id=session_id,
                    muscle_group="Back"
                )
        },
        {
            "name": "Barbell Row",
            "url": url_for(
                "exercise",
                exercise_name="barbell-row",
                session_id=session_id,
                muscle_group="Back"
            )
        },
        {
            "name": "Seated Cable Row",
            "url": url_for(
                "exercise",
                exercise_name="seated-cable-row",
                session_id=session_id,
                muscle_group="Back"
            )
        },
        {
            "name": "Deadlift",
            "url": url_for(
                "exercise",
                exercise_name="deadlift",
                session_id=session_id,
                muscle_group="Back"
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Back",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/biceps")
def biceps():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Barbell Curl",
            "url": url_for(
                "exercise",
                exercise_name="barbell-curl",
                session_id=session_id,
                muscle_group="Biceps"
            )
        },
        {
            "name": "Dumbbell Curl",
            "url": url_for(
                "exercise",
                exercise_name="dumbbell-curl",
                session_id=session_id,
                muscle_group="Biceps"
            )
        },
        {
            "name": "Hammer Curl",
            "url": url_for(
                "exercise",
                exercise_name="hammer-curl",
                session_id=session_id,
                muscle_group="Biceps"
            )
        },
        {
            "name": "Preacher Curl",
            "url": url_for(
                "exercise",
                exercise_name="preacher-curl",
                session_id=session_id,
                muscle_group="Biceps"
            )
        },
        {
            "name": "Cable Curl",
            "url": url_for(
                "exercise",
                exercise_name="cable-curl",
                session_id=session_id,
                muscle_group="Biceps"
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Biceps",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/shoulders")
def shoulders():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Shoulder Press",
            "url": url_for(
                "exercise",
                exercise_name="Shoulder Press",
                muscle_group="Shoulders",
                session_id=session_id
            )
        },
        {
            "name": "Lateral Raise",
            "url": url_for(
                "exercise",
                exercise_name="Lateral Raise",
                muscle_group="Shoulders",
                session_id=session_id
            )
        },
        {
            "name": "Front Raise",
            "url": url_for(
                "exercise",
                exercise_name="Front Raise",
                muscle_group="Shoulders",
                session_id=session_id
            )
        },
        {
            "name": "Rear Delt Fly",
            "url": url_for(
                "exercise",
                exercise_name="Rear Delt Fly",
                muscle_group="Shoulders",
                session_id=session_id
            )
        },
        {
            "name": "Arnold Press",
            "url": url_for(
                "exercise",
                exercise_name="Arnold Press",
                muscle_group="Shoulders",
                session_id=session_id
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Shoulders",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/legs")
def legs():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Squat",
            "url": url_for(
                "exercise",
                exercise_name="Squat",
                muscle_group="Legs",
                session_id=session_id
            )
        },
        {
            "name": "Leg Press",
            "url": url_for(
                "exercise",
                exercise_name="Leg Press",
                muscle_group="Legs",
                session_id=session_id
            )
        },
        {
            "name": "Leg Extension",
            "url": url_for(
                "exercise",
                exercise_name="Leg Extension",
                muscle_group="Legs",
                session_id=session_id
            )
        },
        {
            "name": "Leg Curl",
            "url": url_for(
                "exercise",
                exercise_name="Leg Curl",
                muscle_group="Legs",
                session_id=session_id
            )
        },
        {
            "name": "Romanian Deadlift",
            "url": url_for(
                "exercise",
                exercise_name="Romanian Deadlift",
                muscle_group="Legs",
                session_id=session_id
            )
        },
        {
            "name": "Standing Calf Raise",
            "url": url_for(
                "exercise",
                exercise_name="Standing Calf Raise",
                muscle_group="Legs",
                session_id=session_id
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Legs",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/forearms")
def forearms():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Wrist Curl",
            "url": url_for(
                "exercise",
                exercise_name="wrist-curl",
                session_id=session_id,
                muscle_group="Forearms"
            )
        },
        {
            "name": "Reverse Wrist Curl",
            "url": url_for(
                "exercise",
                exercise_name="reverse-wrist-curl",
                session_id=session_id,
                muscle_group="Forearms"
            )
        },
        {
            "name": "Hammer Curl",
            "url": url_for(
                "exercise",
                exercise_name="hammer-curl",
                session_id=session_id,
                muscle_group="Forearms"
            )
        },
        {
            "name": "Farmer's Walk",
            "url": url_for(
                "exercise",
                exercise_name="farmers-walk",
                session_id=session_id,
                muscle_group="Forearms"
            )
        },
        {
            "name": "Reverse Curl",
            "url": url_for(
                "exercise",
                exercise_name="reverse-curl",
                session_id=session_id,
                muscle_group="Forearms"
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Forearms",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/abs")
def abs():

    session_id = request.args.get("session_id")

    exercises = [
        {
            "name": "Crunches",
            "url": url_for(
                "exercise",
                exercise_name="crunches",
                session_id=session_id,
                muscle_group="Abs"
            )
        },
        {
            "name": "Leg Raises",
            "url": url_for(
                "exercise",
                exercise_name="leg-raises",
                session_id=session_id,
                muscle_group="Abs"
            )
        },
        {
            "name": "Plank",
            "url": url_for(
                "exercise",
                exercise_name="plank",
                session_id=session_id,
                muscle_group="Abs"
            )
        },
        {
            "name": "Russian Twist",
            "url": url_for(
                "exercise",
                exercise_name="russian-twist",
                session_id=session_id,
                muscle_group="Abs"
            )
        },
        {
            "name": "Hanging Leg Raise",
            "url": url_for(
                "exercise",
                exercise_name="hanging-leg-raise",
                session_id=session_id,
                muscle_group="Abs"
            )
        }
    ]

    return render_template(
        "muscle_workout.html",
        muscle="Abs",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/exercise/<exercise_name>", methods=["GET", "POST"])
def exercise(exercise_name):

    session_id = request.args.get("session_id")
    muscle_group = request.args.get("muscle_group")
    exercise_id = request.args.get("exercise_id")
    if exercise_id is None:
                conn = sqlite3.connect("fitness.db")
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO workout_exercises
                    (session_id, exercise_name, muscle_group, exercise_order)
                    VALUES (?, ?, ?, ?)
                    """, (
                        session_id,
                        exercise_name.replace("-", " ").title(),
                        muscle_group,
                        1
                    ))

                exercise_id = cursor.lastrowid
                conn.commit()
                conn.close()

                return redirect(
                    url_for(
                        "exercise",
                        exercise_name=exercise_name,
                        session_id=session_id,
                        exercise_id=exercise_id,
                        muscle_group=muscle_group
                    )
)
    if request.method == "POST":

        weight = request.form["weight"]
        reps = request.form["reps"]
        action = request.form["action"]

        conn = sqlite3.connect("fitness.db")
        cursor = conn.cursor()

        

        # Find how many sets already exist for this exercise
        cursor.execute("""
        SELECT COUNT(*)
        FROM workout_sets
        WHERE exercise_id = ?
        """, (exercise_id,))

        set_number = cursor.fetchone()[0] + 1
        print("Saving set...")
        print("Exercise ID:", exercise_id)
        print("Saving set")
        print("Exercise ID:", exercise_id)
        print("Session ID:", session_id)
        print("Muscle Group:", muscle_group)
                # Insert the new set
        cursor.execute("""
        INSERT INTO workout_sets
        (exercise_id, set_number, weight, reps)
        VALUES (?, ?, ?, ?)
        """, (
            exercise_id,
            set_number,
            weight,
            reps
        ))

        conn.commit()
        conn.close()

        if action == "add_set":
            return redirect(
                url_for(
                    "exercise",
                    exercise_name=exercise_name,
                    session_id=session_id,
                    exercise_id=exercise_id,
                    muscle_group=muscle_group
                )
            )

        elif action == "finish":
            return redirect(
                url_for(
                    muscle_group.lower(),
                    session_id=session_id
                )
            )

    return render_template(
        "exercise.html",
        exercise_name=exercise_name,
        session_id=session_id,
        exercise_id=exercise_id,
        muscle_group=muscle_group
    )
@app.route("/workout_log")
def workout_log():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, session_name, workout_date
        FROM workout_sessions
        WHERE user_id = ?
        ORDER BY workout_date DESC
    """, (session["user_id"],))

    sessions = cursor.fetchall()

    conn.close()

    return render_template(
        "workout_log.html",
        sessions=sessions
    )
@app.route("/weight_tracker", methods=["GET", "POST"])
def weight_tracker():

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    if request.method == "POST":

        weight = request.form["weight"]
        today = datetime.now().strftime("%Y-%m-%d")

        # Check if today's entry already exists
        cursor.execute("""
        SELECT id
        FROM weight_logs
        WHERE user_id = ? AND log_date = ?
        """, (1, today))

        existing = cursor.fetchone()

        if existing:

            # Update today's weight
            cursor.execute("""
            UPDATE weight_logs
            SET weight = ?
            WHERE id = ?
            """, (weight, existing[0]))

        else:

            # Insert a new weight
            cursor.execute("""
            INSERT INTO weight_logs
            (user_id, weight, log_date)
            VALUES (?, ?, ?)
            """, (1, weight, today))

        conn.commit()

        return redirect(url_for("weight_tracker"))

    cursor.execute("""
    SELECT weight, log_date
    FROM weight_logs
    WHERE user_id = ?
    ORDER BY log_date DESC
    """, (1,))

    weights = cursor.fetchall()

    conn.close()

    return render_template(
        "weight_tracker.html",
        weights=weights
    )
@app.route("/workout/<int:session_id>")
def workout_details(session_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    # Verify that this workout session belongs to the logged-in user
    cursor.execute("""
        SELECT id
        FROM workout_sessions
        WHERE id = ? AND user_id = ?
    """, (session_id, session["user_id"]))

    session_exists = cursor.fetchone()

    if not session_exists:
        conn.close()
        return redirect(url_for("workout_log"))

    # Fetch exercises only after ownership is verified
    cursor.execute("""
        SELECT
            workout_exercises.exercise_name,
            workout_sets.set_number,
            workout_sets.weight,
            workout_sets.reps
        FROM workout_exercises
        JOIN workout_sets
        ON workout_exercises.id = workout_sets.exercise_id
        WHERE workout_exercises.session_id = ?
        ORDER BY workout_exercises.id, workout_sets.set_number
    """, (session_id,))

    exercises = cursor.fetchall()

    conn.close()

    return render_template(
        "workout_details.html",
        exercises=exercises,
        session_id=session_id
    )
@app.route("/start_workout", methods=["GET", "POST"])
def start_workout():

    if request.method == "POST":

        selected_muscles = request.form.getlist("muscles")

        workout_name = " + ".join(selected_muscles)

        conn = sqlite3.connect("fitness.db")
        cursor = conn.cursor()

        today = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
        INSERT INTO workout_sessions
        (user_id, session_name, workout_date)
        VALUES (?, ?, ?)
        """, (session["user_id"], workout_name, today))

        

        session_id = cursor.lastrowid
        for index, muscle in enumerate(selected_muscles, start=1):

            cursor.execute("""
            INSERT INTO workout_muscles
            (session_id, muscle_name, muscle_order)
            VALUES (?, ?, ?)
            """, (
                session_id,
                muscle,
                index
            ))
        conn.commit()
        conn.close()

        if not selected_muscles:
            return render_template(
                "start_workout.html",
                error="Please select at least one muscle."
            )

        first_muscle = selected_muscles[0].lower()

        return redirect(
            url_for(
                first_muscle,
                session_id=session_id
            )
        )

    return render_template("start_workout.html")
@app.route("/weight_graph")
def weight_graph():

    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT weight, log_date
        FROM weight_logs
        WHERE user_id = ?
        ORDER BY log_date
    """, (session["user_id"],))

    weights = cursor.fetchall()

    conn.close()

    return render_template(
        "weight_graph.html",
        weights=weights
    )
@app.route("/muscle_groups")
def muscle_groups():

    session_id = request.args.get("session_id")

    return render_template(
        "muscle_groups.html",
        session_id=session_id
    )
@app.route("/finish_muscle")
def finish_muscle():

    session_id = request.args.get("session_id")
    muscle = request.args.get("muscle")

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    # Mark current muscle as completed
    cursor.execute("""
    UPDATE workout_muscles
    SET completed = 1
    WHERE session_id = ? AND muscle_name = ?
    """, (session_id, muscle))

    conn.commit()

    # Find next incomplete muscle
    cursor.execute("""
    SELECT muscle_name
    FROM workout_muscles
    WHERE session_id = ? AND completed = 0
    ORDER BY muscle_order
    LIMIT 1
    """, (session_id,))

    next_muscle = cursor.fetchone()

    conn.close()

    if next_muscle:
        print("Redirecting to:", next_muscle[0])
        return redirect(
            url_for(
                next_muscle[0].lower(),
                session_id=session_id
            )
        )
    return redirect(url_for("workout_log"))
@app.route("/calorie_tracker", methods=["GET", "POST"])
def calorie_tracker():

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()
    user_id = session["user_id"]
    today = date.today()
    if request.method == "POST":
        print(request.form)
        action = request.form.get("action")

        if action == "add_food":

            food_name = request.form["food_name"]
            calories = request.form["calories"]
            meal_type = request.form["meal_type"]



            cursor.execute("""
                INSERT INTO food_logs
                (user_id, food_name, calories, meal_type, log_date)
                VALUES (?, ?, ?, ?, ?)
            """, (
                user_id,
                food_name,
                calories,
                meal_type,
                today
            ))

            conn.commit()
       
    cursor.execute("""
            SELECT SUM(calories)
            FROM food_logs
            WHERE user_id = ?
            AND log_date = ?
            """, (user_id, today))

    total_calories = cursor.fetchone()[0]
    if total_calories is None:
        total_calories = 0

    cursor.execute("""
        SELECT food_name, calories, meal_type, log_date
        FROM food_logs
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))

    foods = cursor.fetchall()
    cursor.execute("""
        SELECT calorie_goal
        FROM users
        WHERE id = ?
    """, (user_id,))

    calorie_goal = cursor.fetchone()[0]

    if calorie_goal is None:
        calorie_goal = 0
    conn.close()

    return render_template(
            "calorie_tracker.html",
            foods=foods,
            total_calories=total_calories,
            calorie_goal=calorie_goal
        )
@app.route("/profile", methods=["GET", "POST"])
@app.route("/profile")
def profile():

    user_id = session["user_id"]

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        name,
        email,
        age,
        height,
        weight,
        goal,
        calorie_goal
        FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()


    cursor.execute("SELECT id, name FROM users")
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        height = request.form["height"]
        weight = request.form["weight"]
        goal = request.form["goal"]
        calorie_goal = request.form["calorie_goal"]
        cursor.execute("""
            UPDATE users
            SET
                name = ?,
                age = ?,
                height = ?,
                weight = ?,
                goal = ?,
                calorie_goal = ?
            WHERE id = ?
            """, (
                name,
                age,
                height,
                weight,
                goal,
                calorie_goal,
                user_id
            ))

        conn.commit()
        
    conn.close()

    return render_template(
    "profile.html",
    user=user
    )
@app.route("/render_users")
def render_users():

    conn = sqlite3.connect("fitness.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, email, age, height, weight, goal
        FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    html = "<h2>Registered Users</h2><hr>"

    for user in users:
        html += f"""
        <p>
        ID: {user[0]}<br>
        Name: {user[1]}<br>
        Email: {user[2]}<br>
        Age: {user[3]}<br>
        Height: {user[4]}<br>
        Weight: {user[5]}<br>
        Goal: {user[6]}
        </p><hr>
        """

    return html

@app.route("/session_test")
def session_test():
    return f"Current session user_id = {session.get('user_id')}"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
