import streamlit as st
st.set_page_config(
    page_title="Fruzen IA",
    page_icon="🍓",
    layout="wide"
)
st.title("🍓 Fruzen IA")
st.subheader("🎬 Crée tes vidéos IA avec des fruits vivants")
st.write(
    "Bienvenue sur Fruzen IA ! "
    "Prépare tes idées et construis tes prochaines vidéos."
)
st.divider()
st.header("🎥 Créer une vidéo")
fruit = st.selectbox(
    "Choisis ton personnage",
    ["🍓 Fraise", "🍌 Banane", "🥝 Kiwi", "🍉 Pastèque"]
)
idee = st.text_area(
    "Décris l'histoire de ta vidéo",
    placeholder="Exemple : une fraise qui travaille dans un restaurant..."
)
duree = st.selectbox(
    "Durée souhaitée",
    ["15 secondes", "30 secondes", "60 secondes"]
)
if st.button("✨ Préparer mon idée"):
    if idee.strip():
        st.success("Ton idée est prête à être préparée !")
        st.write("**Personnage :**", fruit)
        st.write("**Histoire :**", idee)
        st.write("**Durée :**", duree)
    else:
        st.warning("Décris d'abord ton histoire !")
st.divider()
st.caption("Fruzen IA — Notre projet, notre ambition 🚀")

st.divider()
st.header("📸 Ajouter une image")
image = st.file_uploader(
    "Choisis une image depuis ta galerie",
    type=["png", "jpg", "jpeg", "webp"]
)

if image is not None:
    st.image(image, caption="Image sélectionnée", use_container_width=True)
