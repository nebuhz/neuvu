import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser

st.sidebar.title("Danh sách nghệ sĩ")
selected_artist = st.sidebar.radio("Chọn nghệ sĩ:", ['Adele', 'Lady Gaga', 'Anime songs'])

videos = {
    "Adele": [
        ("Rolling in the deep", "https://www.youtube.com/watch?v=rYEDA3JcQqw"),
        ("Skyfall", "https://www.youtube.com/watch?v=DeumyOzKqgI")
    ],
    "Lady Gaga": [
        ("Poker face", "https://www.youtube.com/watch?v=bESGLojNYSo"),
        ("Judas", "https://www.youtube.com/watch?v=wagn8Wrmzuc")
    ],
    "Anime songs": [
        ("unravel", "https://www.youtube.com/watch?v=Fve_lHIPa-I")
    ]
}

st.title("Ứng dụng giải trí và sức khỏe")
tab1, tab2, tab3, tab4,tab5,tab6 = st.tabs(["MV yêu thích", "Dự đoán giờ ngủ", "Đọc báo", "Kiểm tra sức khỏe","Luong nuoc moi ngay","Số bước chân cần đi"])

with tab1:
    st.header(f"Các bài hát của {selected_artist}")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)  # ✅ fixed parentheses

with tab2:
    st.header("Dự đoán giờ đi ngủ mỗi đêm")

    # Dữ liệu mẫu: [tuổi, mức độ hoạt động, thời gian dùng màn hình]
    x = [
        [10, 1, 8],
        [20, 5, 6],
        [25, 8, 3],
        [30, 6, 5],
        [35, 2, 9],
        [40, 4, 3]
    ]
    y = [10, 8, 6, 7, 9.5, 9]

    model = LinearRegression()
    model.fit(x, y)

    st.write("Nhập thông tin cá nhân:")
    age = st.number_input("Tuổi của bạn", min_value=5, max_value=100, value=25)
    activity = st.slider("Mức độ hoạt động thể chất (1 = ít, 10 = rất nhiều)", 1, 10, 5)
    screen_time = st.number_input("Thời gian dùng màn hình trong 1 ngày (giờ)", min_value=0, max_value=24, value=2)

    if st.button("Dự đoán ngay"):
        input_data = [[age, activity, screen_time]]
        result = model.predict(input_data)[0]
        st.success(f"Bạn nên ngủ khoảng {result:.1f} giờ mỗi đêm")

        if result < 6.5:
            st.warning("Bạn cần ngủ nhiều hơn để cải thiện sức khỏe")
        elif result > 9:
            st.info("Bạn đang hoạt động nhiều, bạn cần ngủ bù hợp lí")
        else:
            st.success("Lượng ngủ lí tưởng, hãy giữ thói quen tốt này!")
with tab3:
    st.header("Tin tức mới nhất")
    tabA, tabB,tabC = st.tabs(["Sports","...","uhmmm"])
    with tabA:
            st.header("The latest news from VNExpress")
    feed = feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
    with tabB:
            st.header("I hate men like you")
    with tabC:
            st.header("Theory channel")

with tab4:
    st.header("Kiem tra chi so BMI cua ban")
    weight = st.number_input("Nhap can nang cua ban", max_value=200.0,min_value=10.0,value=50.0)
    height = st.number_input("Nhap chieu cao cua ban", max_value=2.5,min_value=1.0,value=1.5)
    min_acc_weight = 18.5 * (height ** 2)
    max_acc_weight = 25 * (height ** 2)
    if st.button("Tinh BMI"):
        bmi = weight/(height ** 2)
        st.success(f"Chi so BMI cua ban la: {bmi:.2f}")

        if bmi <18.5:
            st.warning("Ban dang thieu can, nen an uong on dinh hon")
            weight_to_add = min_acc_weight - weight
            st.write("Để trở về chỉ số BMI lý tưởng, hãy cố gắng tăng ít nhất", weight_to_add,"cân.")
        elif 18.5 <= bmi <25:
            st.info("Ban co can nang binh thuong. Hay tiep tuc duy tri loi song hien tai")
        elif 25 <= bmi < 30:
            st.warning("Ban dang thua can, hay can doi loi song va tap the duc nhieu")
            weight_to_lose = weight - max_acc_weight
            st.write("Để trở về chỉ số BMI lý tưởng, hãy cố gắng giảm ít nhất", weight_to_lose,"cân.")
        else: 
            st.error("Ban dang beo phi. Hay tham van chuyen gia dinh duong ngay lap tuc")
            weight_to_lose = weight - max_acc_weight
            st.write("Để trở về chỉ số BMI lý tưởng, hãy cố gắng giảm ít nhất", weight_to_lose,"cân.")
with tab5:
    st.title("Khuyen nghi luong nuoc uong moi ngay")
    tuoi = st.number_input("Nhap do tuoi cua ban",min_value=1,max_value=100,value=15,step=1)
    if st.button("Kiem tra luong nuoc can uong"):
        if tuoi < 4:
            st.info("1.3 lit/ngay")
        elif 4 <= tuoi <=8:
            st.info("1.7 lit/ngay")
        elif 9<=tuoi<=13:
            st.info("2.1 - 2.4 lit/ngay")
        elif 14 <= tuoi <=18:
            st.info("2.3 - 3.3 lit/ngay")
        elif 19 <= tuoi <= 50:
            st.info("2.7 - 3.7 lit/ngay")
        elif tuoi >50:
            st.info("2.5-3.0 lit/ngay (tuy vao suc khoe va muc do hoat dong)")
        else:
            st.warning("vui long nhap do tuoi hop le")
with tab6:
    st.title("Số bước chân cần đi mỗi ngày")
    tuổi = st.number_input("Nhập độ tuổi của bạn",min_value=1, max_value=100,value=15,step=1)
    print("Bạn",tuổi,"tuổi")
    if st.button("Số bước chân khuyến khích mỗi ngày"):
        if tuổi <18:
            st.info("Bạn nên đi **12 000 - 15 000** bước chân mỗi ngày")
        elif 17 < tuổi <=39:
            st.info("Bạn nên đi **8 000 - 10 000** bước chân mỗi ngày")
        elif 39 < tuổi <= 64:
            st.warning("Bạn nên đi **7 000 - 9 000** bước chân mỗi ngày")
        elif tuổi > 64:
            st.warning("Bạn nên đi **6 000 - 7 000** bước chân mỗi ngày")
        else:
            st.error("Xin hãy kiểm tra lại thông tin.")
