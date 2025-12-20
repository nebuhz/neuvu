import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import random

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

st.title("Ứng dụng giải trí")

tab1, tab2, tab3, tab4, tab5, tab6,tab7 = st.tabs(["MV Yêu thích", "Dự án giờ ngủ", "Tin tức mới nhất", "Kiểm tra sức khỏe", "Sport", "Kiểm tra thời gian ngủ","Giai tri"])

with tab1:
    st.header(f"Các bài hát của{select_artist}")
    for title, url in videos[select_artist]:
        st.subheader(title)
        st.video(url)

with tab2:
    ("Dự đoán giờ ngủ mỗi đêm")
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
    st.write("Nhập thông tin cá nhân: ")
    age = st.number_input("Tuổi của bạn", min_value = 5, max_value = 100, value = 25)
    activity = st.slider("Mức độ hoạt động thể chất(1 = ít, 10 = rất nhiều)", 1, 10, 5)
    screen_time = st.number_input("Thời gian dùng màn hình trong 1 ngày(giờ)", min_value = 0, max_value = 24, value = 6)
    if st.button("Dự đoán ngay"):
        input_data = [[age, activity, screen_time]]
        result = model.predict(input_data)[0]
        st.success(f"Bạn nên ngủ khoảng{result:.1f} giờ mỗi đêm")
        if result < 6.5:
            st.warning("Có thể bạn cần nghỉ ngơi nhiều hơn")
        elif result > 9:
            st.info("Có thể bạn cần ngủ bù")
        else:
            st.success("Thời gian ngủ hợp lý")
with tab3:
    st.header("Tin tức mới nhất")
    tabA, tabB = st.tabs(['Tin tức mới nhất từ VnExpress', 'Cập nhật giá vàng từ Vietnamnet'])
    with tabA:
        st.header("Tin tức mới nhất")
        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    
    with tabB:
        st.header("Cập nhật giá vàng")
        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
        gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]

        if gold_news:
            for entry in gold_news[:5]:
                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)
        else:
            st.warning("Không tìm thấy bản tin giá vàng gần đây")

with tab4:
    st.header("Kiểm tra sức khỏe")
    tabC, tabD, tabE = st.tabs(["Kiểm tra sức khỏe", "BMI", "Luong Nuoc Can Uong"])
    with tabC:
        cân_nặng = st.number_input("Nhập cân nặng của bạn(kg)", min_value=10.0, max_value=200.0, value=60.0,step=0.1)
        chiều_cao = st.number_input("Nhập chiều cao của bạn(m)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
        bmi_min = 18.5
        bmi_max = 24.9
        cân_nặng_min = bmi_min * (chiều_cao **2)
        cân_nặng_max = bmi_max * (cân_nặng ** 2)
        giam = cân_nặng - cân_nặng_max

        if st.button("Tính BMI"):
            Bmi = cân_nặng / (chiều_cao ** 2)
            st.success(f"Chỉ số BMI của bạn là: {Bmi:.2f}")

            if Bmi < 18.5:
                st.warning("Bạn đang thiếu cân, nên ăn uống đầy đủ hơn")
                tang = cân_nặng_min - cân_nặng
                st.info(f"ban can tang {tang : .2f}")
            elif 18.5 <= Bmi < 25:
                st.info("Bạn có cân nặng bình thường, hãy duy trì cân nặng")
            elif 25 <= Bmi < 30:
                st.warning("Bạn đang thừa cân, nên giảm cân")

            else:
                st.error("Bạn đang béo phì, nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn")

    with tabD:
        st.title("Khuyến nghị lượng nước uống mỗi ngày")
        tuoi = st.number_input("Nhập tuổi của bạn:", min_value=1, max_value=100, value=18, step=1)
        if st.button("Kiểm tra lượng nước cần uống"):
            if tuoi < 4:
                st.info("Khuyến nghị: 1.3 lít/ngày")
            elif 4 < tuoi <= 8:
                st.info("Khuyến nghị: 1.7 lít/ngày")
            elif 9 <= tuoi <= 13:
                st.info("Khuyến nghị: 2.1-2.4 lít/ngày")
            elif 14 <= tuoi <= 18:
                st.info("Khuyến nghị: 2.3-3.3 lít/ngày")
            elif 19 <= tuoi <= 50:
                st.info("Khuyến nghị: 2.7 lít/ngày với nữ, 3.7 lít/ngày đối với nam")
            elif tuoi > 50:
                st.info("Khuyến nghị: Khoảng 2.5-3.0 lít/ngày (Phụ thuộc vào sức khỏe và mức độ vận động")
            else:
                st.warning("Vui lòng nhập độ tuổi hợp lệ")

    with tabE:
        st.title("Kiểm tra bước chân")
        so_buoc_chan = st.number_input("Nhập tuổi của bạn: ", min_value=1, max_value=1000, value = 18, step=1)
        if st.button("Kiểm tra bước chân của bạn"):
            if so_buoc_chan < 18:
                st.info("Bạn nên đi 12.000-15.000 bước/ngày")
            elif 17<so_buoc_chan<=39:
                st.info("Bạn nên đi 8.000-10.000 bước/ngày")
            elif 39<so_buoc_chan<=64:
                st.warning("Bạn nên đi 7.000-9.000 bước/ngày")
            elif 64<so_buoc_chan<=100:
                st.warning("Bạn nên đi 6.000-8.000 bước/ngày")
            elif 100<so_buoc_chan<=300:
                st.warning("Bạn nên đi dưới 100 bước, không nên vận động quá nhiều")
            elif so_buoc_chan > 300:
                st.warning("...")
            else:
                st.error("Vui lòng nhập lại thông tin")

with tab5:
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("http://vietnamnet.vn/rss/the-thao.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)

with tab6:
    st.title("Kiểm tra thời gian ngủ mỗi ngày")

    tuổi = st.number_input('Nhập độ tuổi của bạn: ',min_value=0, max_value=100, value=18, step = 1)
    if tuổi < 3:
        st.info("Cần ngủ 11-14 tiếng mỗi ngày")
    elif tuổi < 6:
        st.info("Cần ngủ 11-14 tiếng mỗi ngày")
    elif tuổi < 14:
        st.info("Cần tuổi 9-11 tiếng mỗi ngày")
    elif tuổi < 18:
        st.info("Cần ngủ 8-10 tiếng mỗi ngày")
    elif tuổi <65:
        st.info("Cần ngủ 7-9 tiếng mỗi ngày")
    else:
        st.info("Cần ngủ 7-8 tiếng mỗi ngày")
with tab7:
    tabA, tabB = st.tabs(["Game doan so","Game tung xuc sac"])
    with tabA:
        st.header("Game doan so bi mat tu 1 -100")
        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1,100)
            st.session_state.tries = 0
        guess = st.number_input("Nhap so du doan 1 - 100", min_value=1, max_value=100,step=1)
        if st.button("Doan"):
            st.session_state.tries +=1
            if guess < st.session_state.secret:
                st.warning("So bi mat lon hon")
            elif guess >st.session_state.secret:
                st.warning("So bi mat nho hon")
            else:
                st.success(f"chinh xac! Ban doan dung sau {st.session_state.tries} lan!")
        if st.button("Choi lai"):
            st.session_state.secret = random.randint(1,100)
            st.session_state.tries = 0

