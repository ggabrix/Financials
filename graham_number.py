#check the tasi dic again later
tasi = {
 'إدارة وتطوير العقارات': ['4300.SR',  '4310.SR',  '4020.SR',  '4150.SR',  '4230.SR',  '4320.SR',  '4100.SR',  '4090.SR',  '4321.SR',  '4250.SR',  '4220.SR',  '4322.SR',  '4323.SR'],
'الأدوية': ['4015.SR'],
'الأسمنت': ['3020.SR',  '3040.SR',  '3030.SR',  '3090.SR',  '3091.SR',  '3005.SR',  '3004.SR',  '3003.SR',  '3080.SR',  '3050.SR',  '3010.SR',  '3002.SR',  '3001.SR',  '3060.SR'],
'الإتصالات': ['7020.SR', '7040.SR', '7030.SR', '7010.SR'], 'الإستثمار والتمويل': ['1111.SR',  '4280.SR',  '4080.SR',  '4081.SR',  '4130.SR',  '2120.SR',  '4082.SR'], 'الإعلام والترفيه': ['4210.SR', '4070.SR', '4071.SR'],
'الادوية': ['2070.SR'], 'البتروكيماويات': ['2350.SR',  '1211.SR',  '2310.SR',  '2380.SR',  '2001.SR',  '2330.SR',  '2060.SR',  '2010.SR',  '2170.SR',  '2250.SR',  '2290.SR',  '2210.SR',  '1210.SR',  '2020.SR',  '2223.SR'],
'البنوك': ['1180.SR',  '1010.SR',  '1150.SR',  '1050.SR',  '1140.SR',  '1020.SR',  '1182.SR',  '1120.SR',  '1030.SR',  '1080.SR',  '1060.SR',  '1183.SR'],
'التأمين': ['8210.SR',  '8250.SR',  '8030.SR',  '8160.SR',  '8280.SR',  '8240.SR',  '8070.SR',  '8120.SR',  '8170.SR',  '8270.SR',  '8050.SR',  '8100.SR',  '8012.SR',  '8150.SR',  '8311.SR',  '8260.SR',  '8200.SR',  '8310.SR',  '8180.SR',  '8060.SR',  '8312.SR',  '8190.SR',  '8020.SR',  '8040.SR',  '8300.SR',  '8230.SR',  '8010.SR'], 'التطبيقات وخدمات التقنية': ['7203.SR',
  '7201.SR',  '7200.SR',  '7202.SR',  '7204.SR'], 
'الخدمات الإستهلاكية': ['1810.SR',  '1830.SR',  '4291.SR',  '4290.SR',  '6012.SR','6013.SR','1820.SR',  '4292.SR',  '6002.SR',  '4010.SR',  '4170.SR','6014.SR', '6015.SR'],
'الخدمات التجارية والمهنية': ['4270.SR',  '1831.SR',  '6004.SR',  '1832.SR',  '1833.SR'], 'الرعاية الصحية': ['4004.SR',  '4005.SR',  '4007.SR',  '4013.SR',  '4009.SR',  '4002.SR',  '2140.SR',  '2230.SR',  '4014.SR'],
'السلع الرأسمالية': ['2040.SR',  '1303.SR',  '1212.SR',  '2110.SR',  '2370.SR',  '2160.SR',  '4141.SR',  '2360.SR',  '1302.SR',  '2320.SR',  '4140.SR',  '4142.SR'],
'السلع طويلة الاجل': ['2340.SR','4180.SR',  '4012.SR',  '2130.SR',  '1213.SR',  '4011.SR'],
'الصناديق العقارية المتداولة': ['4347.SR',  '4344.SR',  '4334.SR',  '4336.SR',  '4332.SR',  '4345.SR',  '4340.SR',  '4338.SR',  '4333.SR',  '4346.SR',  '4348.SR',  '4330.SR',  '4342.SR',  '4335.SR',  '4337.SR',  '4339.SR',  '4331.SR'],
'الطاقة': ['2222.SR', '4030.SR', '4200.SR', '2030.SR', '2381.SR'], 
'المرافق العامة': ['2082.SR', '5110.SR', '2080.SR', '2081.SR', '2083.SR'],
'المواد الأساسية': ['1202.SR',  '2300.SR',  '1320.SR',  '1201.SR',  '3008.SR', '2220.SR',  '2200.SR',  '1301.SR',  '3007.SR',  '2180.SR',  '2240.SR',  '1321.SR',  '1304.SR',  '2090.SR',  '2150.SR',  '1322.SR'], 'النقل': ['4261.SR', '4260.SR', '4031.SR', '4040.SR', '4110.SR', '2190.SR'],
'انتاج الأغذية': ['2280.SR',  '2050.SR',  '2270.SR',  '6001.SR',  '6020.SR',  '6090.SR',  '6010.SR',  '2281.SR',  '6070.SR',  '2100.SR',  '6060.SR',  '6050.SR',  '6040.SR', '2282.SR',  '2283.SR'],
'تجزئة الأغذية': ['4161.SR',  '4001.SR',  '4162.SR',  '4160.SR',  '4061.SR',  '4006.SR',  '4163.SR',  '4164.SR'], 
'تجزئة السلع الكمالية': ['4003.SR',  '4190.SR',  '4191.SR',  '1214.SR',  '4008.SR','4240.SR',  '4050.SR',  '4051.SR',  '4192.SR'],
'صندوق متداول': ['4701.SR']}

companies = {'2222.SR': 'أرامكو السعودية',
 '1180.SR': 'الأهلي السعودي',
 '2082.SR': 'أكوا باور',
 '1010.SR': 'الرياض',
 '1150.SR': 'الإنماء',
 '2350.SR': 'كيان السـعودية',
 '1211.SR': 'معادن',
 '2310.SR': 'سبكيم العالمية',
 '7020.SR': 'اتحاد اتصالات',
 '2380.SR': 'بترو رابغ',
 '2001.SR': 'كيمانول',
 '2330.SR': 'المتقدمة',
 '2060.SR': 'التصنيع',
 '7203.SR': 'علم',
 '1050.SR': 'السعودي الفرنسي',
 '1202.SR': 'مبكو',
 '4261.SR': 'ذيب',
 '4004.SR': 'دله الصحية',
 '1111.SR': 'مجموعة تداول',
 '5110.SR': 'كهرباء السعودية',
 '2010.SR': 'سابك',
 '1140.SR': 'البلاد',
 '1810.SR': 'سيرا القابضة',
 '2280.SR': 'المراعي',
 '2170.SR': 'اللجين القابضة',
 '8210.SR': 'بوبا العربية',
 '3020.SR': 'أسمنت اليمامة',
 '2250.SR': 'المجموعة السعودية',
 '4300.SR': 'دار الأركان',
 '1830.SR': 'وقت اللياقة',
 '4030.SR': 'البحري',
 '4291.SR': 'الوطنية للتربية والتعليم',
 '2050.SR': 'صافولا',
 '4005.SR': 'رعاية',
 '4007.SR': 'الحمادي',
 '2290.SR': 'ينساب',
 '2300.SR': 'صناعة الورق',
 '2270.SR': 'سدافكو',
 '8250.SR': 'جي آي جي',
 '4013.SR': 'د. سليمان الحبيب',
 '4210.SR': 'الأبحاث والتسويق',
 '4003.SR': 'إكسترا',
 '3040.SR': 'أسمنت القصيم',
 '4161.SR': 'بن داود',
 '3030.SR': 'أسمنت السعودية',
 '4009.SR': 'المستشفى السعودي الألماني',
 '4260.SR': 'بدجت السعودية',
 '4347.SR': 'بنيان ريت',
 '4290.SR': 'الخليج للتدريب',
 '4344.SR': 'سدكو كابيتال ريت',
 '4310.SR': 'مدينة المعرفة',
 '3090.SR': 'أسمنت تبوك',
 '4334.SR': 'المعذر ريت',
 '3091.SR': 'أسمنت الجوف',
 '8030.SR': 'ميدغلف للتأمين',
 '4280.SR': 'المملكة',
 '4336.SR': 'ملكية ريت',
 '4332.SR': 'جدوى ريت الحرمين',
 '4345.SR': 'الأنماء ريت للتجزئة',
 '4031.SR': 'الخدمات الأرضية',
 '4340.SR': 'الراجحي ريت',
 '4338.SR': 'الأهلي ريت 1',
 '8160.SR': 'التأمين العربية',
 '4002.SR': 'المواساة',
 '2210.SR': 'نماء للكيماويات',
 '8280.SR': 'العالمية',
 '4333.SR': 'تعليم ريت',
 '4020.SR': 'العقارية',
 '4001.SR': 'أسواق ع العثيم',
 '4346.SR': 'ميفك ريت',
 '3005.SR': 'أم القرى',
 '8240.SR': 'تشب العربية',
 '8070.SR': 'الدرع العربي',
 '2040.SR': 'الخزف السعودي',
 '8120.SR': 'إتحاد الخليج الأهلية',
 '3004.SR': 'أسمنت الشمالية',
 '4348.SR': 'الخبير ريت',
 '4162.SR': 'المنجم',
 '2070.SR': 'الدوائية',
 '8170.SR': 'الاتحاد للتأمين',
 '4150.SR': 'التعمير',
 '4330.SR': 'الرياض ريت',
 '8270.SR': 'بروج للتأمين',
 '6001.SR': 'حلواني إخوان',
 '4342.SR': 'جدوى ريت السعودية',
 '8050.SR': 'سلامة',
 '4230.SR': 'البحر الأحمر',
 '4335.SR': 'مشاركة ريت',
 '3003.SR': 'أسمنت المدينة',
 '6012.SR': 'ريدان الغذائية',
 '4160.SR': 'ثمار',
 '3080.SR': 'أسمنت الشرقية',
 '4061.SR': 'أنعام القابضة',
 '3050.SR': 'أسمنت الجنوبية',
 '8100.SR': 'سايكو',
 '1820.SR': 'مجموعة الحكير',
 '8012.SR': 'جزيرة تكافل',
 '4320.SR': 'الأندلس',
 '4006.SR': 'أسواق المزرعة',
 '1303.SR': 'صناعات كهربائية',
 '3010.SR': 'أسمنت العربية',
 '4337.SR': 'مشاعر ريت',
 '8150.SR': 'أسيج',
 '1320.SR': 'الأنابيب السعودية',
 '4292.SR': 'عطاء التعليمية',
 '3002.SR': 'أسمنت نجران',
 '4190.SR': 'جرير',
 '2340.SR': 'العبداللطيف',
 '1201.SR': 'تكوين',
 '6020.SR': 'جاكو',
 '6002.SR': 'هرفي للأغذية',
 '3008.SR': 'الكثيري القابضة',
 '4191.SR': 'أبو معطي',
 '4339.SR': 'دراية ريت',
 '4270.SR': 'طباعة وتغليف',
 '8311.SR': 'عناية',
 '3001.SR': 'أسمنت حائل',
 '8260.SR': 'الخليجية العامة',
 '4010.SR': 'دور',
 '6090.SR': 'جازادكو',
 '4180.SR': 'مجموعة فتيحي',
 '8200.SR': 'الإعادة السعودية',
 '4100.SR': 'مكة للإنشاء',
 '4012.SR': 'ثوب الأصيل',
 '8310.SR': 'أمانة للتأمين',
 '6010.SR': 'نادك',
 '4040.SR': 'سابتكو',
 '2130.SR': 'صدق',
 '1214.SR': 'الحسن شاكر',
 '2080.SR': 'غازكو',
 '8180.SR': 'الصقر للتأمين',
 '1212.SR': 'أسترا الصناعية',
 '8060.SR': 'ولاء للتأمين',
 '2140.SR': 'أيان للاستثمار',
 '8312.SR': 'الإنماء طوكيو م',
 '2281.SR': 'تنمية',
 '4200.SR': 'الدريس',
 '2110.SR': 'الكابلات',
 '7201.SR': 'بحر العرب',
 '2370.SR': 'مسك',
 '6070.SR': 'الجوف',
 '4008.SR': 'ساكو',
 '8190.SR': 'المتحدة للتأمين',
 '1210.SR': 'بي سي آى',
 '4331.SR': 'الجزيرة ريت',
 '2220.SR': 'معدنية',
 '1213.SR': 'نسيج',
 '2160.SR': 'أميانتيت',
 '2200.SR': 'أنابيب',
 '1301.SR': 'أسلاك',
 '4141.SR': 'العمران للصناعة والتجارة',
 '4110.SR': 'باتك',
 '2100.SR': 'وفرة',
 '2081.SR': 'الخريف',
 '1831.SR': 'مهارة',
 '3060.SR': 'أسمنت ينبع',
 '4080.SR': 'سناد القابضة',
 '2360.SR': 'الفخارية',
 '6004.SR': 'التموين',
 '8020.SR': 'ملاذ للتأمين',
 '1020.SR': 'الجزيرة',
 '1182.SR': 'أملاك',
 '6060.SR': 'الشرقية للتنمية',
 '3007.SR': 'زهرة الواحة للتجارة',
 '8040.SR': 'أليانز إس إف',
 '2180.SR': 'فيبكو',
 '8300.SR': 'الوطنية',
 '6050.SR': 'الأسماك',
 '2240.SR': 'الزامل للصناعة',
 '8230.SR': 'تكافل الراجحي',
 '6013.SR': 'التطويرية الغذائية',
 '6040.SR': 'تبوك الزراعية',
 '7200.SR': 'إم آي إس',
 '4090.SR': 'طيبة',
 '4240.SR': 'سينومي ريتيل',
 '4050.SR': 'ساسكو',
 '4011.SR': 'لازوردي',
 '2230.SR': 'الكيميائية',
 '1321.SR': 'أنابيب الشرق',
 '1302.SR': 'بوان',
 '4051.SR': 'باعظيم',
 '7040.SR': 'عذيب للاتصالات',
 '2320.SR': 'البابطين',
 '8010.SR': 'التعاونية',
 '1304.SR': 'اليمامة للحديد',
 '2090.SR': 'جبسكو',
 '4140.SR': 'صادرات',
 '4070.SR': 'تهامة للإعلان',
 '4081.SR': 'النايفات',
 '2030.SR': 'المصافي',
 '4321.SR': 'سينومي سنترز',
 '7202.SR': 'سلوشنز',
 '7030.SR': 'زين السعودية',
 '4250.SR': 'جبل عمر',
 '2190.SR': 'سيسكو',
 '4130.SR': 'الباحة',
 '4071.SR': 'العربية',
 '2150.SR': 'زجاج',
 '4220.SR': 'إعمار',
 '4014.SR': 'دار المعدات الطبية',
 '4170.SR': 'شمس',
 '1832.SR': 'صدر',
 '2120.SR': 'المتطورة',
 '1120.SR': 'الراجحي',
 '2020.SR': 'سابك للمغذيات الزراعية',
 '1030.SR': 'استثمار',
 '1080.SR': 'العربي الوطني',
 '1060.SR': 'ساب',
 '7010.SR': 'اس تي سي',
 '4163.SR': 'الدواء',
 '4164.SR': 'النهدي',
 '1322.SR': 'أماك',
 '4701.SR': 'الخبير للدخل',
 '1183.SR': 'سهل',
 '4322.SR': 'رتال',
 '6014.SR': 'الآمار',
 '2282.SR': 'نقي',
 '2381.SR': 'الحفر العربية',
 '2083.SR': 'مرافق',
 '6015.SR': 'أمريكانا',
 '4142.SR': 'كابلات الرياض',
 '2223.SR': 'لوبريف',
 '4192.SR': 'السيف غاليري',
 '7204.SR': 'توبي',
 '1833.SR': 'الموارد',
 '4015.SR': 'جمحوم فارما',
 '4082.SR': 'مرنة',
 '2283.SR': 'المطاحن الأولى',
 '4323.SR': 'سمو'}

import streamlit as st
import pandas as pd
import yfinance as yf
import warnings
import logging

warnings.filterwarnings('ignore')  # Ignore warnings

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def calculate_graham_number(stock, graham_factor):
    """Calculate and print the Graham number for a given stock."""
    try:
        data = yf.Ticker(stock).info
        df = pd.DataFrame(data).T[0]
        eps_forward = df.get('forwardEps')
        eps_trailing = df.get('trailingEps')

        # Choose EPS type
        if eps_forward is not None:
            eps = eps_forward
            eps_type = "forward"
        elif eps_trailing is not None:
            eps = eps_trailing
            eps_type = "trailing"
        else:
            return '-', 'unknown', None

        book_value = df['bookValue']
        current_price = df['currentPrice']

        # Check if EPS is negative
        if eps < 0:
            return '-', eps_type, current_price
        else:
            graham_number = round((graham_factor * eps * book_value) ** 0.5,2)

            # Check if the Graham number is far below the current price by 50% or more
            if graham_number < current_price * 0.5:
                return '-', eps_type, current_price
            else:
                return graham_number, eps_type, current_price
    except Exception as e:
        # Map the stock symbol to a company name
        company_name = companies.get(stock, "Unknown Company")
        error_message = f"An error occurred when processing {company_name} ({stock}): {e}"
        print(error_message)
        st.error(error_message)  # Display the error message in the Streamlit UI
        logger.error(error_message)  # Log the error
        return None, 'unknown', None  # Return None if an exception occurs

# List of Graham factors
graham_factors = [22.5, 30, 50]


st.title('Calculate Graham Number')

def get_data_for_sector(sector):
    stock_codes = tasi[sector]
    # Assuming you have a function to fetch data for a stock code
    data = [fetch_data_for_stock(code) for code in stock_codes]
    df = pd.DataFrame(data)
    return df

sector = st.selectbox('Select sector', list(tasi.keys()))
data = get_data_for_sector(sector)

st.write(data)

for stock in tasi[selected_sector]:
    row = {"Stock": stock}
    # Get company name from dictionary
    row["Company"] = companies.get(stock, "Unknown Company")
    for factor in graham_factors:
        graham_number, eps_type, current_price = calculate_graham_number(stock, factor)
        row[f"Graham_{factor}"] = graham_number
        row["EPS_Type"] = eps_type
        row["Current_Price"] = current_price
    graham_numbers = graham_numbers.append(row, ignore_index=True)

# Filter the DataFrame
graham_numbers = graham_numbers[graham_numbers['Graham_22.5'] != '-']

# Display the DataFrame
st.dataframe(graham_numbers)
========================================================


import streamlit as st
import pandas as pd
import yfinance as yf
import warnings
import logging

warnings.filterwarnings('ignore')  # Ignore warnings

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def fetch_data_for_stock(stock):
    # Fetch data for a stock using yfinance
    data = yf.Ticker(stock).info
    # Convert the dictionary into a DataFrame and Transpose it
    df = pd.DataFrame(data, index=[0])
    return df

def calculate_graham_number(stock, graham_factor):
    """Calculate and print the Graham number for a given stock."""
    try:
        data = yf.Ticker(stock).info
        df = pd.DataFrame(data).T[0]
        eps_forward = df.get('forwardEps')
        eps_trailing = df.get('trailingEps')

        # Choose EPS type
        if eps_forward is not None:
            eps = eps_forward
            eps_type = "forward"
        elif eps_trailing is not None:
            eps = eps_trailing
            eps_type = "trailing"
        else:
            return '-', 'unknown', None

        book_value = df['bookValue']
        current_price = df['currentPrice']

        # Check if EPS is negative
        if eps < 0:
            return '-', eps_type, current_price
        else:
            graham_number = round((graham_factor * eps * book_value) ** 0.5,2)

            # Check if the Graham number is far below the current price by 50% or more
            if graham_number < current_price * 0.5:
                return '-', eps_type, current_price
            else:
                return graham_number, eps_type, current_price
    except Exception as e:
        # Map the stock symbol to a company name
        company_name = companies.get(stock, "Unknown Company")
        error_message = f"An error occurred when processing {company_name} ({stock}): {e}"
        print(error_message)
        st.error(error_message)  # Display the error message in the Streamlit UI
        logger.error(error_message)  # Log the error
        return None, 'unknown', None  # Return None if an exception occurs
# List of Graham factors
graham_factors = [22.5, 30, 50]

st.title('Calculate Graham Number')

def get_data_for_sector(sector):
    stock_codes = tasi[sector]
    data = [fetch_data_for_stock(code) for code in stock_codes]
    df = pd.DataFrame(data)
    return df

sector = st.selectbox('Select sector', list(tasi.keys()))
data = get_data_for_sector(sector)

st.write(data)

# Define your graham_numbers DataFrame here
graham_numbers = pd.DataFrame()

for stock in tasi[sector]:
    row = {"Stock": stock}
    row["Company"] = companies.get(stock, "Unknown Company")
    for factor in graham_factors:
        graham_number, eps_type, current_price = calculate_graham_number(stock, factor)
        row[f"Graham_{factor}"] = graham_number
        row["EPS_Type"] = eps_type
        row["Current_Price"] = current_price
    graham_numbers = graham_numbers.append(row, ignore_index=True)

graham_numbers = graham_numbers[graham_numbers['Graham_22.5'] != '-']
st.dataframe(graham_numbers)
