import streamlit as st
import os
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS
from services.ui.style_loader import load_css, inject_local_font, inject_webrtc_styles
from services.persistence.exercise_repository import init_db
from streamlit_webrtc import webrtc_streamer, WebRtcMode

def main():
    st.set_page_config(
        page_icon="🏋🏻‍♀️",
        page_title="REAL-TIME AI GYM COACH",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    
    load_css(os.path.join(os.getcwd(), "static", "style.css"))
    inject_local_font(os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean")

    init_db()
   
    if not render_login_wall():
        return

    initial_session_defaults()


    workout_started = st.session_state.get("workout_started", False)


    with st.sidebar:
        st.title("🏋🏻‍♀️REAL-TIME AI GYM COACH")

        if st.session_state.username:
            st.caption(f" 👤 Login as {st.session_state.username}")

        st.divider()

        st.subheader("Workout Plan")

        if not workout_started:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")

            st.number_input("Sets", min_value=0, max_value=50, key="plan_sets", step=1)

            st.number_input("Reps per Set", min_value=0, max_value=50, key="plan_reps", step=1)

            st.markdown("")
            
            start_session_button = st.button("Start Workout", width="stretch", key="start_session_button")

            if start_session_button:
                st.session_state["workout_started"] = True

                st.rerun()
        else:
            exercise = st.session_state.get("plan_exercise")
            sets = st.session_state.get("plan_sets")
            reps = st.session_state.get("plan_reps")

            st.info(f"**{exercise}** -- {sets} Sets / {reps} Reps")

            end_session_button = st.button("End Workout", key="end_session_button", width="stretch")

            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()

        if workout_started:
            st.divider()

            exercise = st.session_state.get("plan_exercise")
            total_reps = st.session_state.get("reps")
            current_set_reps = st.session_state.get("current_set_reps")
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets = st.session_state.get("plan_sets")

            st.subheader("Progress")

            st.metric("Total Reps", f"{total_reps}")
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metrics")
                st.metric("Knee Angle", f"{st.session_state.knee_angle}")
                st.metric("Back Angle", f"{st.session_state.back_angle}")
                st.metric("Depth Status", st.session_state.depth_status)

            elif exercise == "Push-ups":
                st.subheader("Push-up Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}")
                st.metric("Body Alignment", f"{st.session_state.body_alignment}")
                st.metric("Hip Position", st.session_state.hip_status)


            elif exercise == "Bicep Curls (Dumbbell)":
                st.subheader("Curl Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}")
                st.metric("Shoulder Stability", f"{st.session_state.shoulder_status}")
                st.metric("Swing Detection", st.session_state.swing_status)


            elif exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}")
                st.metric("Arm Extension", f"{st.session_state.extension_status}")
                st.metric("Back Arch", st.session_state.arch_status)


            elif exercise == "Lunges":
                st.subheader("Lunge Metrics")
                st.metric("Front Knee Angle", f"{st.session_state.front_knee_angle}")
                st.metric("Torse Angle", f"{st.session_state.torso_angle}")
                st.metric("Balance Status", st.session_state.balance_status)

    st.title("REAL-TIME-AI-GYM-COACH")
    st.markdown("#### Real-time pose detection with proactive AI voice coaching")


    
    if not workout_started:
        st.markdown(
            """
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                min-height: 48vh;
                padding: 20px 16px;
                box-sizing: border-box;
            ">
                <div style="
                    width: 100%;
                    max-width: 760px;
                    box-sizing: border-box;
                    background: linear-gradient(145deg, #171b25, #11141b);
                    border: 1px solid #343b4b;
                    border-radius: 18px;
                    padding: 48px 36px;
                    text-align: center;
                    color: #b8c0ce;
                    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
                ">
                    <div style="
                        font-size: 42px;
                        margin-bottom: 16px;
                    ">🏋️</div>
                    <p>
                        Your personal AI coach is ready.
                        Choose your exercise, sets, and reps from the sidebar,
                        then click
                        <strong style="color: #c4b5fd;">Start Workout</strong>
                        to activate your camera and begin training.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        context = webrtc_streamer(
            key="exercise-analysis",
            mode=WebRtcMode.SENDRECV,
            video_processor_factory=None,
            rtc_configuration={
                "iceServers": [
                    {"urls": ["stun:stun.l.google.com:19302"]}
                ]
            },
            media_stream_constraints={
                "video": True,
                "audio": False,
            },
            async_processing=True,
        )

    st.markdown("#### Workout History")

    inject_webrtc_styles()

if __name__ == "__main__":
    main()