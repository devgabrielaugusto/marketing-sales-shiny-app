# --------------------------------------------------------
# Libraries
# --------------------------------------------------------
from shared import df_dictionary, df_purchase, df_marketing, app_dir
from shiny import reactive, render
from shiny.express import input, ui
from shinywidgets import output_widget, render_widget 

import plotly.express as px

import pandas as pd
from datetime import date, timedelta
import numpy as np

# --------------------------------------------------------
# Reactive Calculations
# --------------------------------------------------------

# Sales reactive calculation

# Marketing reactive calculation

# --------------------------------------------------------
# UI
# --------------------------------------------------------

# Page title
ui.page_opts(title=ui.span("🚀 Marketing and Sales Dashboard", class_="app-title"), fillable=True)

# Page tabs
with ui.navset_tab():
    # Sales tab
    with ui.nav_panel("Sales"):
        with ui.layout_sidebar(bg="#f8f8f8"):
            with ui.sidebar(bg="#ffffff"):
                ui.h4("Filters Control", class_="mb-3 pb-2 border-bottom sidebar-title")
                ui.input_date_range(
                    "sales_date_range",
                    "Select Date Range",
                    start="2019-08-16",
                    end="2024-06-02"
                )
                with ui.accordion(id="filters_accordion", open=["Category"]):
                    with ui.accordion_panel("Category"):
                        ui.input_checkbox_group(
                            "select_category",
                            "Category:",
                            df_purchase['ORGANISATION_VERTICAL'].unique().tolist(),
                            selected=df_purchase['ORGANISATION_VERTICAL'].unique().tolist(),
                        )
                    with ui.accordion_panel("Subcategory"):
                        ui.input_checkbox_group(
                            "select_subcategory",
                            "Subcategory:",
                            df_purchase['ORGANISATION_SUBVERTICAL'].unique().tolist(),
                            selected=df_purchase['ORGANISATION_SUBVERTICAL'].unique().tolist(),
                        )
                    with ui.accordion_panel("Region"):
                        ui.input_checkbox_group(
                            "select_region",
                            "Region:",
                            df_purchase['TERRITORY_NAME'].unique().tolist(),
                            selected=df_purchase['TERRITORY_NAME'].unique().tolist(),
                        )
                    with ui.accordion_panel("Marketing Channels"):
                        ui.input_checkbox_group(
                            "select_marketing_channels",
                            "Marketing Channels:",
                            df_purchase['ORGANISATION_MARKETING_SOURCES'].unique().tolist(),
                            selected=df_purchase['ORGANISATION_MARKETING_SOURCES'].unique().tolist(),
                        )

            # Big numbers
            with ui.layout_columns():
                with ui.value_box(showcase=ui.h1("🛍️"), class_="gradient-box"):
                    "Total Purchases"
                    @render.text
                    def total_purchases():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['ALL_PURCHASES'].sum():,.0f}"
                with ui.value_box(showcase=ui.h1("📦"), class_="gradient-box"):
                    "Total Purchases Units"
                    @render.text
                    def total_purchases_units():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['ALL_PURCHASES_UNITS'].sum():,.0f}"
                with ui.value_box(showcase=ui.h1("💰"), class_="gradient-box"):
                    "Revenue"
                    @render.text
                    def revenue():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['ALL_PURCHASES_ORIGINAL_PRICE'].sum():,.0f}"
                with ui.value_box(showcase=ui.h1("💸"), class_="gradient-box"):
                    "Inv. Digital Marketing"
                    @render.text
                    def spend():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['TOTAL_SPEND'].sum():,.0f}"

            with ui.layout_columns():
                with ui.value_box(showcase=ui.h1("🪙"), class_="gradient-box-light"):
                    "ROAS"
                    @render.text
                    def roas():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['ALL_PURCHASES_ORIGINAL_PRICE'].sum() / df['TOTAL_SPEND'].sum():,.2f}"
                with ui.value_box(showcase=ui.h1("🥇"), class_="gradient-box-light"):
                    "ROAS 1º Purchase"
                    @render.text
                    def roas_1st_purchase():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['FIRST_PURCHASES_ORIGINAL_PRICE'].sum() / df['TOTAL_SPEND'].sum():,.2f}"
                with ui.value_box(showcase=ui.h1("🧾"), class_="gradient-box-light"):
                    "Revenue per Purchase"
                    @render.text
                    def revenue_per_purchase():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['ALL_PURCHASES_ORIGINAL_PRICE'].sum() / df['ALL_PURCHASES'].sum():,.2f}"
                with ui.value_box(showcase=ui.h1("🏷️"), class_="gradient-box-light"):
                    "Revenue per Unit"
                    @render.text
                    def revenue_per_unit():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        return f"{df['ALL_PURCHASES_ORIGINAL_PRICE'].sum() / df['ALL_PURCHASES_UNITS'].sum():,.2f}"

            # Charts
            with ui.layout_columns():
                with ui.card():
                    ui.card_header("Purchases in Time")
                    @render_widget  
                    def plot_purchases_in_time():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        # Aggregate by date to ensure one point per day and correct sorting
                        df_grouped = df.groupby("DATE_DAY", as_index=False)["ALL_PURCHASES"].sum()
                        df_grouped["DATE_DAY"] = df_grouped["DATE_DAY"].astype(str)
                        
                        lineplot = px.line(
                            data_frame=df_grouped,
                            x="DATE_DAY",
                            y="ALL_PURCHASES",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            hovermode="x unified"
                        ).update_traces(
                            line_color='#337ab7',
                            line_width=3
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee',
                            zeroline=False
                        ).update_xaxes(
                            showgrid=False
                        )
                        return lineplot
                with ui.card():
                    ui.card_header("Purchases by Category")
                    @render_widget  
                    def plot_purchases_by_category():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        # Aggregate and sort for better legibility
                        df_grouped = df.groupby("ORGANISATION_VERTICAL", as_index=False)["ALL_PURCHASES"].sum()
                        df_grouped = df_grouped.sort_values("ALL_PURCHASES", ascending=False)
                        
                        barplot = px.bar(
                            data_frame=df_grouped,
                            x="ORGANISATION_VERTICAL",
                            y="ALL_PURCHASES",
                            text_auto='.2s',
                            color="ALL_PURCHASES",
                            color_continuous_scale="Blues",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            showlegend=False,
                        ).update_traces(
                            textfont_size=12, 
                            textangle=0, 
                            textposition="outside", 
                            cliponaxis=False
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee'
                        )
                        return barplot

            with ui.layout_columns():
                with ui.card():
                    ui.card_header("Marketing Channels")
                    @render_widget  
                    def plot_marketing_channels():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        # Aggregate and sort for better legibility
                        df_grouped = df.groupby("ORGANISATION_MARKETING_SOURCES", as_index=False)["TOTAL_SPEND"].sum()
                        df_grouped = df_grouped.sort_values("TOTAL_SPEND", ascending=False)
                        
                        barplot = px.bar(
                            data_frame=df_grouped,
                            x="ORGANISATION_MARKETING_SOURCES",
                            y="TOTAL_SPEND",
                            text_auto='.2s',
                            color="TOTAL_SPEND",
                            color_continuous_scale="Blues",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            showlegend=False,
                        ).update_traces(
                            textfont_size=12, 
                            textangle=0, 
                            textposition="outside", 
                            cliponaxis=False
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee'
                        )
                        return barplot
                with ui.card():
                    ui.card_header("Revenue in Time")
                    @render_widget  
                    def plot_revenue_in_time():
                        start, end = sales_dates = input.sales_date_range()
                        category = input.select_category()
                        subcategory = input.select_subcategory()
                        region = input.select_region()
                        marketing_channels = input.select_marketing_channels()  

                        df = df_purchase
                        mask = (df_purchase['DATE_DAY'].dt.date >= start) & (df_purchase['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['ORGANISATION_MARKETING_SOURCES'].isin(marketing_channels)]
                        
                        # Aggregate by date to ensure one point per day and correct sorting
                        df_grouped = df.groupby("DATE_DAY", as_index=False)["ALL_PURCHASES_ORIGINAL_PRICE"].sum()
                        df_grouped["DATE_DAY"] = df_grouped["DATE_DAY"].astype(str)
                        
                        lineplot = px.line(
                            data_frame=df_grouped,
                            x="DATE_DAY",
                            y="ALL_PURCHASES_ORIGINAL_PRICE",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            hovermode="x unified"
                        ).update_traces(
                            line_color='#337ab7',
                            line_width=3
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee',
                            zeroline=False
                        ).update_xaxes(
                            showgrid=False
                        )
                        return lineplot

    # Marketing tab
    with ui.nav_panel("Marketing"):
        with ui.layout_sidebar(bg="#f8f8f8"):
            with ui.sidebar(bg="#ffffff"):
                ui.h4("Filters Control", class_="mb-3 pb-2 border-bottom sidebar-title")
                ui.input_date_range(
                    "marketing_date_range",
                    "Select Date Range",
                    start="2019-08-16",
                    end="2024-06-02"
                )
                with ui.accordion(id="filters_accordion_marketing", open=["Category"]):
                    with ui.accordion_panel("Category"):
                        ui.input_checkbox_group(
                            "select_category_marketing",
                            "Category:",
                            df_marketing['ORGANISATION_VERTICAL'].unique().tolist(),
                            selected=df_marketing['ORGANISATION_VERTICAL'].unique().tolist(),
                        )
                    with ui.accordion_panel("Subcategory"):
                        ui.input_checkbox_group(
                            "select_subcategory_marketing",
                            "Subcategory:",
                            df_marketing['ORGANISATION_SUBVERTICAL'].unique().tolist(),
                            selected=df_marketing['ORGANISATION_SUBVERTICAL'].unique().tolist(),
                        )
                    with ui.accordion_panel("Region"):
                        ui.input_checkbox_group(
                            "select_region_marketing",
                            "Region:",
                            df_marketing['TERRITORY_NAME'].unique().tolist(),
                            selected=df_marketing['TERRITORY_NAME'].unique().tolist(),
                        )
                    with ui.accordion_panel("Marketing Channels"):
                        ui.input_checkbox_group(
                            "select_marketing_channels_marketing",
                            "Marketing Channels:",
                            df_marketing['CHANNEL'].unique().tolist(),
                            selected=df_marketing['CHANNEL'].unique().tolist(),
                        )

            # Big numbers
            with ui.layout_columns():
                with ui.value_box(showcase=ui.h1("🛍️"), class_="gradient-box"):
                    "Total Investment"
                    @render.text
                    def total_investment():
                        start, end = sales_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        return f"{df['TOTAL_SPEND'].sum():,.0f}"
                with ui.value_box(showcase=ui.h1("📦"), class_="gradient-box"):
                    "Total Impressions"
                    @render.text
                    def total_impressions():
                        start, end = sales_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        return f"{df['TOTAL_IMPRESSIONS'].sum():,.0f}"
                with ui.value_box(showcase=ui.h1("💰"), class_="gradient-box"):
                    "CPM"
                    @render.text
                    def cpm():
                        start, end = sales_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        return f"{(df['TOTAL_SPEND'].sum()/df['TOTAL_IMPRESSIONS'].sum()) * 1000:,.2f}"

            # Charts
            with ui.layout_columns():
                with ui.card():
                    ui.card_header("Investment in Time")
                    @render_widget  
                    def plot_investment_in_time():
                        start, end = marketing_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        # Aggregate by date to ensure one point per day and correct sorting
                        df_grouped = df.groupby("DATE_DAY", as_index=False)["TOTAL_SPEND"].sum()
                        df_grouped["DATE_DAY"] = df_grouped["DATE_DAY"].astype(str)
                        
                        lineplot = px.line(
                            data_frame=df_grouped,
                            x="DATE_DAY",
                            y="TOTAL_SPEND",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            hovermode="x unified"
                        ).update_traces(
                            line_color='#337ab7',
                            line_width=3
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee',
                            zeroline=False
                        ).update_xaxes(
                            showgrid=False
                        )
                        return lineplot
                with ui.card():
                    ui.card_header("Investment by Channel")
                    @render_widget  
                    def plot_investment_by_channel():
                        start, end = marketing_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        # Aggregate and sort for better legibility
                        df_grouped = df.groupby("CHANNEL", as_index=False)["TOTAL_SPEND"].sum()
                        df_grouped = df_grouped.sort_values("TOTAL_SPEND", ascending=False)
                        
                        barplot = px.bar(
                            data_frame=df_grouped,
                            x="CHANNEL",
                            y="TOTAL_SPEND",
                            text_auto='.2s',
                            color="TOTAL_SPEND",
                            color_continuous_scale="Blues",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            showlegend=False,
                        ).update_traces(
                            textfont_size=12, 
                            textangle=0, 
                            textposition="outside", 
                            cliponaxis=False
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee'
                        )
                        return barplot

            with ui.layout_columns():
                with ui.card():
                    ui.card_header("Investment by Category")
                    @render_widget  
                    def plot_investment_by_category_marketing():
                        start, end = marketing_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        # Aggregate and sort for better legibility
                        df_grouped = df.groupby("ORGANISATION_VERTICAL", as_index=False)["TOTAL_SPEND"].sum()
                        df_grouped = df_grouped.sort_values("TOTAL_SPEND", ascending=False)
                        
                        barplot = px.bar(
                            data_frame=df_grouped,
                            x="ORGANISATION_VERTICAL",
                            y="TOTAL_SPEND",
                            text_auto='.2s',
                            color="TOTAL_SPEND",
                            color_continuous_scale="Blues",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            showlegend=False,
                        ).update_traces(
                            textfont_size=12, 
                            textangle=0, 
                            textposition="outside", 
                            cliponaxis=False
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee'
                        )
                        return barplot
                with ui.card():
                    ui.card_header("Investment by Subcategory")
                    @render_widget  
                    def plot_investment_by_subcategory_marketing():
                        start, end = marketing_dates = input.marketing_date_range()
                        category = input.select_category_marketing()
                        subcategory = input.select_subcategory_marketing()
                        region = input.select_region_marketing()
                        marketing_channels = input.select_marketing_channels_marketing()  

                        df = df_marketing
                        mask = (df_marketing['DATE_DAY'].dt.date >= start) & (df_marketing['DATE_DAY'].dt.date <= end)
                        df = df[mask]
                        df = df[df['ORGANISATION_VERTICAL'].isin(category)]
                        df = df[df['ORGANISATION_SUBVERTICAL'].isin(subcategory)]
                        df = df[df['TERRITORY_NAME'].isin(region)]
                        df = df[df['CHANNEL'].isin(marketing_channels)]
                        
                        # Aggregate and sort for better legibility
                        df_grouped = df.groupby("ORGANISATION_SUBVERTICAL", as_index=False)["TOTAL_SPEND"].sum()
                        df_grouped = df_grouped.sort_values("TOTAL_SPEND", ascending=False)
                        
                        barplot = px.bar(
                            data_frame=df_grouped,
                            x="ORGANISATION_SUBVERTICAL",
                            y="TOTAL_SPEND",
                            text_auto='.2s',
                            color="TOTAL_SPEND",
                            color_continuous_scale="Blues",
                        ).update_layout(
                            xaxis_title=None,
                            yaxis_title=None,
                            template="plotly_white",
                            plot_bgcolor="rgba(0,0,0,0)",
                            margin=dict(l=0, r=0, t=20, b=0),
                            showlegend=False,
                        ).update_traces(
                            textfont_size=12, 
                            textangle=0, 
                            textposition="outside", 
                            cliponaxis=False
                        ).update_yaxes(
                            showgrid=True, 
                            gridcolor='#eee'
                        )
                        return barplot

# Include CSS
ui.include_css(app_dir / "styles.css")