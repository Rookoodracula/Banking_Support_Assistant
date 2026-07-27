import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import streamlit as st

#Setting page configs

st.set_page_config(
    page_title="🏦 Your Banking Support Assistant",
    page_icon="🏦",
    layout="wide"
)

st.title("Welcome, I am Your Banking Support Assistant")
st.write("Ask me anything banking related queries.")

# Importing Modules

try:
    from src.predictor import predict
    from src.retrieve import retrieve_similar
    from src.responses import get_response
except Exception as e:
    st.error(f"⚠️ Error loading backend modules: {e}")
    st.stop()


# Sidebar

st.sidebar.title("Project Information")

st.sidebar.markdown("### Model")
st.sidebar.write("DistilBERT")

st.sidebar.markdown("### Retrieval")
st.sidebar.write("Sentence Transformer")

st.sidebar.markdown("### Dataset")
st.sidebar.write("Banking77")


# Session State

if "history" not in st.session_state:
    st.session_state.history = []


# USER INPUT

query = st.text_input(
    "Enter your banking query",
    placeholder="Example: My card has not arrived yet"
)

if st.button("Predict"):

    if query.strip() == "":
        st.warning("Please enter a query.")
        st.stop()

    prediction, top3 = predict(query)
    retrieved = retrieve_similar(query)
    response = get_response(prediction["intent"])

    st.session_state.history.append((query, response))
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Predicted Intent")
        st.success(prediction["intent"])

        st.metric(
            "Confidence",
            f"{prediction['confidence']:.2f}%"
        )

        st.subheader("Top 3 Predictions")

        for item in top3:

            st.write(
                f"• {item['intent']} ({item['confidence']:.2f}%)"
            )

    with col2:

        st.subheader("Most Similar FAQ")
        st.info(retrieved["matched_question"])
        st.write(f"Category: {retrieved['category']}")
        st.write(f"Similarity: {retrieved['similarity']:.2f}%")

    st.markdown("---")
    st.subheader("Chatbot Response")
    st.success(response)

# History

if st.session_state.history:

    st.markdown("---")
    st.subheader("Conversation History")

    for q, r in reversed(st.session_state.history):

        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {r}")
        st.markdown("---")
