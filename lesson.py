import streamlit as st

# Sayfa başlığı ve tasarımı
st.set_page_config(page_title="Asya'nın Testi", layout="centered")

# Başlangıçta puanı sıfır olarak tanımlıyoruz
if 'puan' not in st.session_state:
    st.session_state.puan = 0

st.title("--- ASYA'YI NE KADAR İYİ TANIYORSUN? ---")

# --- 1. SORU ---
st.subheader("1. Soru: Asya'nın en sevdiği renk nedir?")
st.write("A) Mavi B) Beyaz C) Yeşil D) Narçiçeği")
cevap1 = st.text_input("Cevabınız: (A/B/C/D):", key="c1").upper()

if cevap1:
    if cevap1 == "B":
        st.session_state.puan += 20
        st.success(f"Doğru cevap! Demek beni dinliyorsun. İşte puanın: {st.session_state.puan}")
    elif cevap1 == "C":
        st.session_state.puan += 10
        st.warning(f"Hep yeşil giymem onu favorim yapmaz ama sana acıdım. İşte puanın: {st.session_state.puan}")
    else: 
        st.session_state.puan += 0
        st.error(f"Cidden mi? İşte puanın ezik: {st.session_state.puan}")

st.divider()

# --- 2. SORU ---
st.subheader("2. Soru: Asya'nın olmak istediği hayvan nedir?")
st.write("A) Yunus B) Hemşire Köpekbalığı C) Katil Balina D) Kambur Balina")
cevap2 = st.text_input("Cevabınız: (A/B/C/D):", key="c2").upper()

if cevap2:
    if cevap2 == "A":
        st.session_state.puan += -10
        st.error(f"NE!!! Ben yunuslardan nefret ederim. -10 puan: {st.session_state.puan}")
    elif cevap2 == "B" or cevap2 == "C":
        st.session_state.puan += 0
        st.warning(f"Olsam üzlümezdim ama maalesef asıl istediğim bu değil. 0 puan: {st.session_state.puan}")
    else:
        st.session_state.puan += 20
        st.success(f"Doğru bildin. Eğer bir hayvan olsaydım alfa kambur balina olurdum. İşte puanın: {st.session_state.puan}")

st.divider()

# --- 3. SORU ---
st.subheader("3. Soru: Asya son zamanlarda rüyasında en çok neyi görüyor?")
st.write("A) Evlilik B) Katilden kaçış C) Katil olmak D) Yüksekten düşmek")
cevap3 = st.text_input("Cevabınız: (A/B/C/D):", key="c3").upper()

if cevap3:
    if cevap3 == "A":
        st.session_state.puan += 20
        st.success(f"Doğru cevap! Nedense hep evlenecek gibi oluyorum. İşte puanın: {st.session_state.puan}")
    elif cevap3 == "C":
        st.session_state.puan += 10
        st.warning(f"Bu aralar diyorum. Beni götünle mi dinliyosun. Neyse al 10 puan: {st.session_state.puan}")
    else: 
        st.session_state.puan += 0
        st.error(f"Yok bunlar çok klasik: {st.session_state.puan}")

st.divider()

# --- 4. SORU ---
st.subheader("4. Soru: Asya'nın en sevdiği lise yılı nedir?")
st.write("A) Hazırlık Sınıfı B) 9. Sınıf C) 10. Sınıf D) 11. Sınıf E) 12. Sınıf")
cevap4 = st.text_input("Cevabınız: (A/B/C/D/E):", key="c4").upper()

if cevap4:
    if cevap4 == "A":
        st.session_state.puan += 20
        st.success(f"Doğru cevap! Hazırlık C olmazsa olmazdı. İşte puanın: {st.session_state.puan}")
    elif cevap4 == "C":
        st.session_state.puan += 0
        st.error(f"Ben Berke miyim mk? Neyse işte puanın: {st.session_state.puan}")
    else:
        st.session_state.puan += 0
        st.error(f"Yok 0 puan: {st.session_state.puan}")

st.divider()

# --- 5. SORU ---
st.subheader("5. Soru: Asya puanı yetse ne okurdu?")
st.write("A) Karabük üni otobüs şoförlüğü B) Ytü İstatistik C) Tıp D) İtü Bilgisayar")
cevap5 = st.text_input("Cevabınız: (A/B/C/D):", key="c5").upper()

if cevap5:
    if cevap5 == "D":
        st.session_state.puan += 20
        st.success(f"İtü bilgisayarla cerrahpaşa arasında kaldım en son cerrahpaşa yazdım. İşte puanın: {st.session_state.puan}")
    elif cevap5 == "C":
        st.session_state.puan += 10
        st.warning(f"Çok arada kalınabilirdi ama değil. Yarı puan verdim gitti: {st.session_state.puan}")
    else:
        st.session_state.puan += 0
        st.error(f"Yok 0 puan: {st.session_state.puan}")
    
    st.error(f"Kaç puan aldın bakalım. SS at sikmim: {st.session_state.puan}")
