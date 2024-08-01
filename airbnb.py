import streamlit as st
from streamlit_option_menu import option_menu
#pd.set_option('display.max_columns', None)
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
from PIL import Image

st.set_page_config(
    page_title="Airbnb Analysis And Visualization",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded")


df= pd.read_csv("C:/Users/nawas/Desktop/project 3/Airbnb.csv")

with st.sidebar:

    options = ["Home", "Data Explore","Geospatial Visualization"]
    selected_option = option_menu("Option Menu", options)

if selected_option =="Home":
    st.title("Airbnb Analysis And Visualization")
    img=Image.open("c:/Users/nawas/Downloads/image.jpg")
    st.image(img)

    st.header('About Airbnb')
    st.write('''***Airbnb is an American company operating an online marketplace
                for short- and long-term homestays and experiences.
                The company acts as a broker and charges a commission from each booking.
                The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia.
                Airbnb is a shortened version of its original name, AirBedandBreakfast.com.***''')

    st.subheader('Airbnb services')
    st.write('''***Airbnb serves as a transformative platform that connects travelers
                    with a diverse array of accommodation options worldwide, beyond traditional hotels.
                    For guests, Airbnb offers the opportunity to discover unique stays such as entire homes,
                    private rooms, and unconventional lodgings like treehouses or castles. 
                    This variety allows travelers to tailor their accommodations to specific preferences,
                    whether seeking a local experience, privacy, or budget-friendly options.
                    Guests benefit from the flexibility to book short-term stays, extended vacations, or 
                    last-minute getaways, often at competitive prices compared to traditional lodging.***''')

elif selected_option =="Data Explore":

    tab1,tab2,tab3,tab4=st.tabs(["PRICE ANALYSIS","AVALIABILITY ANALYSIS","LOCATION ANALYSIS"," CORRELATION ANALYSIS"])
    with tab1:
        st.title("**PRICE ANALYSIS**")

        col1,col2=st.columns(2)
        
        with col1:

            country_1= st.selectbox("Select the country",(df["country"].unique()))

            # Filter df based on selected country
            df1=df[df["country"] == country_1]
            df1.reset_index(drop=True, inplace=True)

            room_ty= st.selectbox("Select the room type",(df1["room_type"].unique()))

            df2=df1[df1["room_type"] == room_ty]
            df2.reset_index(drop=True, inplace=True)

            room_ty_aggregated= pd.DataFrame(df2.groupby("property_type")[["price","review_scores_accuracy","number_of_reviews","review_scores_rating"]].sum())
            room_ty_aggregated.reset_index(inplace= True)
            
            fig_bar=px.bar(room_ty_aggregated, x="property_type", y="price", title="PRICE DIFFERENCE FOR ROOM TYPE",
                        hover_data=["review_scores_accuracy","number_of_reviews","review_scores_rating"],color_discrete_sequence=px.colors.sequential.Rainbow)
            st.plotly_chart(fig_bar)
            
        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")  

            property_ty= st.selectbox("Select the property type",(df2["property_type"].unique()))

            df3=df2[df2["property_type"] == property_ty]
            df3.reset_index(drop=True, inplace=True)

            property_ty_aggregated = pd.DataFrame(df3.groupby("host_response_time")[["price","bedrooms","beds"]].sum())
            property_ty_aggregated.reset_index(inplace= True)

            fig_pie= px.pie(property_ty_aggregated, names= "host_response_time", values="price",
                            hover_data=["bedrooms","beds"],
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600)
            st.plotly_chart(fig_pie)
        
        col1,col2=st.columns(2)

        with col1:
                
            host_response_time= st.selectbox("Select the host_response_time",df3["host_response_time"].unique())

            df4=df3[df3["host_response_time"] == host_response_time]
            df4.reset_index(drop=True, inplace=True)

            host_response_time_agg= pd.DataFrame(df4.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            host_response_time_agg.reset_index(inplace= True)

            fig_bar_1= px.bar(host_response_time_agg, x="bed_type", y=["minimum_nights", "maximum_nights"], 
                            title="MINIMUM NIGHTS AND MAXIMUM NIGHTS",hover_data="price",barmode='group',
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, width=600, height=500)

            st.plotly_chart(fig_bar_1)                   

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("") 

            host_response_time_agg= pd.DataFrame(df4.groupby("bed_type")[["price","beds","bedrooms","accommodates"]].sum())
            host_response_time_agg.reset_index(inplace= True)

            fig_bar_2= px.bar(host_response_time_agg, x='bed_type', y=["beds","bedrooms","accommodates"], 
                            title="BEDS BEDROOMS AND ACCOMADATES",hover_data="price",barmode='group',
                            color_discrete_sequence=px.colors.sequential.Agsunset, width=600, height=500)

            st.plotly_chart(fig_bar_2) 

    with tab2:
        df_a= pd.read_csv("C:/Users/nawas/Desktop/project 3/Airbnb.csv")

        st.title("**AVALIABILITY ANALYSIS**")

        col1,col2=st.columns(2)

        with col1:                  
            country_aa= st.selectbox("Select the country_aa",(df_a["country"].unique()))

            # Filter df based on selected country
            df1_c=df[df["country"] == country_aa]
            df1_c.reset_index(drop=True, inplace=True)

            property_ty_avail= st.selectbox("Select the property_ty_avail",(df1_c["property_type"].unique()))

            df2_p=df1_c[df1_c["property_type"] == property_ty_avail]
            df2_p.reset_index(drop=True, inplace=True)

            fig_sunburst_1=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_30", 
                                    title="AVAILABILITY 30",color_discrete_sequence=px.colors.sequential.Magenta, width=600, height=500)
            
            st.plotly_chart(fig_sunburst_1)
            
        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("") 
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")  

            fig_sunburst_2=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_60", 
                                        title="AVAILABILITY 60",color_discrete_sequence=px.colors.sequential.Cividis_r, width=600, height=500)
                
            st.plotly_chart(fig_sunburst_2)

        col1,col2=st.columns(2)
        with col1:
            fig_sunburst_3=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_90", 
                                        title="AVAILABILITY 90",color_discrete_sequence=px.colors.sequential.Sunset, width=600, height=500)
                
            st.plotly_chart(fig_sunburst_3)
        
        with col2:
            fig_sunburst_4=px.sunburst(df2_p, path=["room_type","is_location_exact","bed_type"], values="availability_365", 
                                        title="AVAILABILITY 365",color_discrete_sequence=px.colors.sequential.Plasma, width=600, height=500)
                
            st.plotly_chart(fig_sunburst_4)  

        room_ty_aa= st.selectbox("Select the room_ty_aa",(df1_c["room_type"].unique()))

        df3_r=df1_c[df1_c["room_type"] == room_ty_aa]
        df3_r.reset_index(drop=True, inplace=True)

        room_type_agg= pd.DataFrame(df3_r.groupby("host_response_time")[["price","availability_30","availability_60","availability_90","availability_365"]].sum())
        room_type_agg.reset_index(inplace= True)

        fig_bar_aa= px.bar(room_type_agg, x="host_response_time", y=["availability_30","availability_60","availability_90","availability_365"], 
                                title="AVAILABILITY BASED ON HOST RESPONSE TIME",hover_data="price",
                                color_discrete_sequence=px.colors.sequential.RdPu,width=600,height=600)

        st.plotly_chart(fig_bar_aa)

    with tab3:
        df_l= pd.read_csv("C:/Users/nawas/Desktop/project 3/Airbnb.csv")

        st.title("**LOCATION ANALYSIS**")

        country_ac= st.selectbox("Select the country_ac",(df_l["country"].unique()))

            # Filter df based on selected country
        df_l_c=df[df["country"] == country_ac]
        df_l_c.reset_index(drop=True, inplace=True)

        property_ty_ac= st.selectbox("Select the property_ty_ac",(df_l_c["property_type"].unique()))

        df_l_p=df1_c[df1_c["property_type"] == property_ty_ac]
        df_l_p.reset_index(drop=True, inplace=True)
        
        accommodates_agg= pd.DataFrame(df_l_p.groupby("accommodates")[["bedrooms","beds","cleaning_fee","extra_people","guests_included","security_deposit"]].sum())
        accommodates_agg.reset_index(inplace= True)

        fig_bar_ac= px.bar(accommodates_agg,x="accommodates", y=["bedrooms","beds","extra_people","guests_included","security_deposit"], 
                            title="Accommodates",hover_data="cleaning_fee",
                            color_discrete_sequence=px.colors.sequential.Electric)
        
        st.plotly_chart(fig_bar_ac)

        fig_bar_2= px.bar(host_response_time_agg, x='bed_type', y=["beds","bedrooms","accommodates"], 
                                            title="BEDS BEDROOMS AND ACCOMADATES",hover_data="price",barmode='group',
                                            color_discrete_sequence=px.colors.sequential.Agsunset, width=600, height=500)

        st.plotly_chart(fig_bar_2)

        with tab4:
            st.title("**CORRELATION ANALYSIS**")
            st.write("")
            st.write("")
            st.write("")

            #correlation map
            corr_df = df[["price","availability_365","minimum_nights","maximum_nights",
                        "number_of_reviews","review_scores_rating"]]
            
            #df["price"] = pd.to_numeric(df["price"], errors='coerce')
            correlation_matrix = corr_df.corr()
            
            # Create a heatmap using Seaborn
            plt.figure(figsize=(12, 8))
            sns.heatmap(correlation_matrix, annot=True)

            # Display the heatmap with Streamlit
            st.pyplot(plt)
        
elif selected_option =="Geospatial Visualization":

        st.subheader("**Geospatial Visualization**")

        df_lat= pd.read_csv("C:/Users/nawas/Desktop/project 3/Airbnb.csv")

        fig_scatter_geo = px.scatter_geo(df_lat,
        lat="latitude",  # specify the column for latitude
        lon="longitude",
        color="country",  # specify the column for longitude
        hover_name="country",  # column added to hover information
        size="accommodates",  # size of markers
        projection="natural earth")

        st.plotly_chart(fig_scatter_geo)




