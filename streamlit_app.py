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

st.divider()
st.header("📸 Ajouter une image")

image = st.file_uploader(
    "Choisis une image depuis ta galerie",
    type=["png", "jpg", "jpeg", "webp"]
)

if image is not None:
    st.image(
        image,
        caption="Image sélectionnée",
        use_container_width=True
    )


if st.button("✨ Préparer mon idée"):
    if idee.strip():
        st.success("Ton scénario est prêt !")

        st.subheader("🎬 Ton projet vidéo")
        st.write("**Personnage :**", fruit)
        st.write("**Durée souhaitée :**", duree)

        prompt = f"""
Crée une vidéo verticale de type TikTok.
Personnage principal : {fruit}.
Durée souhaitée : {duree}.

Histoire demandée :
{idee}

Instructions :
- Le fruit est un personnage vivant et expressif.
- Garde le même personnage pendant toute la vidéo.
- Utilise un style cinématographique de haute qualité.
- Ajoute des mouvements naturels et des expressions claires.
- Prévois une voix en français si le modèle vidéo le permet.
- Construis une histoire avec un début, une action et une fin.
- Format vertical 9:16.
"""

        st.text_area(
            "Prompt prêt pour la génération vidéo",
            value=prompt,
            height=300
        )

        st.download_button(
            label="📥 Télécharger mon prompt",
            data=prompt,
            file_name="prompt_fruzen.txt",
            mime="text/plain"
        )

        st.subheader("🧪 Mode test gratuit")
        st.info(
            "Le scénario est préparé ! "
            "La génération vidéo réelle sera disponible "
            "lorsque le moteur IA sera connecté."
        )

        st.write("**Statut :** Scénario prêt, vidéo non générée.")
        st.progress(100)

        st.success(
            "✅ Test réussi : Fruzen a préparé ton projet sans "
            "consommer de crédits vidéo."
        )

    else:
        st.warning("Décris d'abord ton histoire !")

st.divider()
st.caption("Fruzen IA — Notre projet, notre ambition 🚀")
