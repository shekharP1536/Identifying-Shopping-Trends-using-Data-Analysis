#!/usr/bin/env python
# coding: utf-8

# In[4]:


# importing libraries
import numpy as np # Importing the numpy library for array operations and mathematical functions
import pandas as pd # Use for exploring the data 
import seaborn as sns # it has also plot
import matplotlib.pyplot as plt # for some extra plot functions
import plotly.express as px # this library can makes interactive plots
import warnings
warnings.filterwarnings("ignore")


# In[5]:


shop=pd.read_csv("shopping_trends_updated.csv")
shop.sample(5)


# In[9]:


# rows and columns of the data set
shop.shape


# In[ ]:


# Lets convert into excel format because it has less rows
shop.to_excel("shopping_trends_updated.xlsx")


# 3. Analyzing the variable
# 

# In[13]:


# it shows the first five rows of the data set 
shop.head()


# In[15]:


# it shows the data types of the variables and help us to identify what type of variable is
shop.dtypes


# In[23]:


# it shows the names of the columns 
shop.columns


# In[27]:


shop.info()


# In[29]:


shop.isnull().sum()


# In[34]:


# it is the important columns having unique values

print(f"The unique values of the 'Gender' column are : {shop['Gender'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Category' column are : {shop['Category'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Size' column are : {shop['Size'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Subscription Status' column are : {shop['Subscription Status'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Shipping Type' column are : {shop['Shipping Type'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Discount Applied' column are: {shop['Discount Applied'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Promo Code Used' column are: {shop['Promo Code Used'].unique()}")
print()# This will print a blank line
print(f"The unique values of the 'Payment Method' column are: {shop['Payment Method'].unique()}")


# #OBSERVATION:
# 
# Upon initial examination of the dataset, it is evident that we have a comprehensive and well-structured dataset with 3900 rows and 18 columns. The data is complete, with no missing values, which allows us to proceed confidently with our analysis.
# 
# Let's delve into the columns and their significance in understanding our customers:
# 
# Customer ID: This column serves as a unique identifier for each customer, enabling us to differentiate between individuals.
# 
# Age: The age column provides insights into the age demographics of our customers, helping us understand their preferences and behaviors.
# 
# Gender: This column showcases the gender of the customers, enabling us to analyze buying patterns based on gender.
# Item Purchased: Here, we can identify the specific products that customers have bought, allowing us to gain an understanding of popular choices.
# 
# Category: The category column categorizes the products into different groups such as clothing, footwear, and more, aiding us in analyzing trends within specific product categories.
# 
# Purchase Amount (USD): This column reveals the amount customers spent on their purchases, providing insights into their spending habits.
# 
# Location: The location column indicates the geographical location of customers, which can help identify regional trends and preferences.
# 
# Size: This column denotes the size of the purchased products, assisting in understanding size preferences across different categories.
# 
# Color: Here, we can determine the color preferences of customers, aiding in analyzing color trends and their impact on purchasing decisions.
# 
# Season: The season column allows us to identify the season during which customers made their purchases, enabling us to explore seasonal shopping trends.
# 
# Review Rating: This column showcases the ratings given by customers, providing valuable feedback on product satisfaction and quality.
# 
# Subscription Status: This column indicates whether customers have opted for a subscription status, which can help us understand customer loyalty and engagement.
# 
# Shipping Type: Here, we can identify the different shipping methods used to deliver products to customers, shedding light on preferred shipping options.
# 
# Discount Applied: This column indicates whether a discount was applied to the purchased products, enabling us to analyze the impact of discounts on customer behavior.
# 
# Promo Code Used: Here, we can identify whether customers utilized promo codes during their purchases, helping us evaluate the effectiveness of promotional campaigns.
# 
# Previous Purchases: This column reveals the number of previous purchases made by customers, aiding in understanding customer loyalty and repeat business.
# 
# Payment Method: The payment method column showcases the various methods used by customers to make their purchases, allowing us to analyze preferred payment options.
# 
# Frequency of Purchases: This column provides insights into the frequency at which customers make purchases, helping us identify patterns and customer buying habits.
# 
# With this rich and diverse dataset, we are well-equipped to explore customer shopping trends, understand their preferences, and uncover valuable insights that can drive informed decision-making and enhance the overall customer experience. Let's embark on this exciting analysis journey!

# # 4. QUESTIONS:
# 
# 
# Certainly! Here are 20 to 25 potential questions you can explore using the Shopping trends dataset:
# 
# What is the overall distribution of customer ages in the dataset?
# 
# How does the average purchase amount vary across different product categories?
# 
# Which gender has the highest number of purchases?
# 
# What are the most commonly purchased items in each category?
# 
# Are there any specific seasons or months where customer spending is significantly higher?
# 
# What is the average rating given by customers for each product category?
# 
# Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?
# 
# Which payment method is the most popular among customers?
# 
# Do customers who use promo codes tend to spend more than those who don't?
# 
# How does the frequency of purchases vary across different age groups?
# 
# Are there any correlations between the size of the product and the purchase amount?
# 
# Which shipping type is preferred by customers for different product categories?
# 
# How does the presence of a discount affect the purchase decision of customers?
# 
# Are there any specific colors that are more popular among customers?
# 
# What is the average number of previous purchases made by customers?
# 
# How does the purchase amount differ based on the review ratings given by customers?
# 
# Are there any noticeable differences in purchase behavior between different locations?
# 
# Is there a relationship between customer age and the category of products they purchase?
# 
# How does the average purchase amount differ between male and female customers?

# These questions should give me a starting point to explore various aspects of the 
# Shopping trends dataset. I can further refine and expand upon these questions based on my specific analysis goals
# and the insights I want to uncover.
# 

# In[41]:


#4.1 What is the overall distribution of customer ages in the dataset?

# Count of the each age value

count_by_age = shop['Age'].value_counts().rename("count")
print(count_by_age)


# In[42]:


# mean or average value of age 
shop['Age'].mean()


# In[43]:


# unique function shows the unique values of any columns
shop['Gender'].unique()


# In[46]:


# we are cutting the age into some category and storing in the different column
shop['Age_category'] = pd.cut(shop['Age'], 
                              bins= [0,15, 18 , 30 , 50 , 70] , 
                              labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults', 'old'] )


# In[45]:


# we use plotly library to use plots
fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()


# CONCLUSION:
# 
# The overall distribution of customer ages in the dataset indicates an average age of 44 years, suggesting a central tendency for the age distribution. However, it is noteworthy that the mode, representing the most frequently occurring age, is 69 years. This suggests that there is a concentration of customers around this particular age, potentially indicating a significant subgroup within the dataset.
# 
# The presence of a mode at 69 years and an average of 44 years implies a right-skewed or positively skewed distribution. In such a distribution, there is a longer tail on the right side, indicating that there may be a larger number of older customers compared to younger ones.
# 
# In conclusion, the overall distribution of customer ages in the dataset exhibits an average age of 44 years and a mode at 69 years.
# 

# 4.2 How does the average purchase amount vary across different product categories?
# 

# In[47]:


# it shows the names of the columns

shop.columns


# In[53]:


# unique values of Category
shop['Category'].unique()


# In[51]:


len(shop['Category'].unique())


# In[54]:


# we are seeking amount based on Category
shop.groupby('Category')['Purchase Amount (USD)'].mean()


# CONCLUSION:
# 
# This suggests that customers tend to spend a similar amount regardless of the specific category of the product they are purchasing. Whether it is electronics, clothing, or other items, the average purchase amount remained relatively consistent.
# 
# However, it is important to consider that this conclusion is based on the available data and the specific dataset used for analysis. It is possible that there may be other factors influencing the average purchase amount that were not accounted for in the analysis. Further investigation, such as considering additional variables or conducting a more extensive study, may be needed to gain a deeper understanding of the factors affecting purchase amounts across different product categories.
# 

# In[56]:


#4.3 Which gender has the highest number of purchases?

# names of columns
shop.columns


# In[59]:


# Convert 'Purchase Amount (USD)' to numeric if it's not already
shop['Purchase Amount (USD)'] = pd.to_numeric(shop['Purchase Amount (USD)'], errors='coerce')

# Plot using Seaborn
sns.barplot(data=shop, x='Gender', y='Purchase Amount (USD)')


# CONCLUSION:
# 
# After analyzing the available data, it can be concluded that all genders have made an equal number of purchases. This suggests that there is no significant difference in the purchase frequency among different genders.
# 
# The absence of variations in purchase behavior across genders implies that the number of purchases is evenly distributed among all genders. This balanced distribution could indicate a lack of gender-based preferences or biases when it comes to purchasing decisions.
# 
# However, it is important to note that this conclusion is based on the assumption that all genders have made an equal number of purchases. It is possible that the dataset does not capture gender-specific information or that other factors were not considered, which could affect the accuracy of the conclusion.
# 

# 4.4 What are the most commonly purchased items in each category?

# In[63]:


shop.columns


# In[62]:


# we are seeking Item purchased based on Category
shop.groupby('Category')['Item Purchased'].value_counts()


# In[72]:


fig = px.histogram(shop , x = 'Item Purchased', color = 'Category')
fig.show()


# CONCLUSION:
# 
# After examining the available data, the most commonly purchased items in each category have been identified. The analysis revealed the following findings:
# 
# Accessories Category: The most commonly purchased item in the Accessories category is jewelry. This indicates that customers frequently purchase various types of jewelry items, such as necklaces, earrings, bracelets, or rings.
# 
# Clothing Category: Within the Clothing category, the most commonly purchased items are pants and blouses. This suggests that customers frequently buy pants and blouses to fulfill their clothing needs.
# 
# Footwear Category: The most commonly purchased item in the Footwear category is sandals. This indicates that customers often choose sandals as their preferred choice of footwear when making a purchase.
# 
# Outerwear Category: The most commonly purchased items in the Outerwear category are jackets and coats. This suggests that customers frequently buy jackets and coats to meet their outerwear requirements, particularly during colder seasons or for specific outdoor activities.
# 
# These findings provide valuable insights into the most popular items within each category. By understanding the common preferences of customers, businesses can tailor their inventory and marketing strategies to meet the demands of their target audience more effectively. It's important to note that these conclusions are based on the provided information and may vary depending on the specific dataset and market context.

# In[ ]:


#4.5 Are there any specific seasons or months where customer spending is significantly higher?


# In[73]:


shop.columns


# In[77]:


shop['Season'].unique()


# In[79]:


# filtering the data 
shop[shop['Season'] == 'Summer'].value_counts().sum()


# In[80]:


# filtering the data 
shop[shop['Season'] == 'Winter'].value_counts().sum()


# In[81]:


# filtering the data 
shop[shop['Season'] == 'Spring'].value_counts().sum()


# In[82]:


# filtering the data 
shop[shop['Season'] == 'Fall'].value_counts().sum()


# In[83]:


fig = px.histogram(shop , x = 'Season' , range_y= [200 , 1500] )

fig.show()


# CONCLUSION:
# 
# After analyzing the available data, it can be concluded that customer spending is significantly higher during the spring season.
# 
# Spring is a time of renewal, and it often brings a sense of freshness and a shift in consumer behavior. Several factors contribute to the higher customer spending during this season:
# 
# Seasonal Changes: Spring signifies the end of winter and the arrival of warmer weather. This change in season often prompts individuals to update their wardrobes, purchase new outdoor equipment, or engage in home improvement projects. As a result, customer spending tends to increase during this time.
# 
# Special Occasions: Spring is associated with various holidays and events, such as Easter, Mother's Day, and graduations. These occasions often involve gift-giving and celebrations, leading to increased consumer spending on gifts, flowers, dining out, and other related expenses.
# 
# Travel and Vacation: Many people plan vacations or travel during the spring season, taking advantage of school breaks or milder weather. This leads to higher spending on travel accommodations, transportation, dining, and recreational activities.
# 
# Seasonal Sales and Promotions: Retailers often offer discounts, promotions, and sales during the spring season to attract customers and encourage spending. These incentives can contribute to increased customer spending during this time.
# 
# It's important to note that while spring is generally associated with higher customer spending, there may be variations based on regional factors, cultural differences, and specific industry trends. To gain a more accurate understanding of customer spending patterns, analyzing historical data and market trends specific to the target demographic and industry would be beneficial.
# 
# 

# In[ ]:


#4.6 What is the average rating given by customers for each product category?


# In[84]:


shop.columns


# In[85]:


shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()


# In[86]:


fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()


# CONCLUSION:
# 
# Based on the analysis conducted, it can be concluded that the average rating given by customers for each product category is consistent across all categories, with an average rating of 3.7.
# 
# This finding suggests that, on average, customers tend to provide a similar rating of 3.7 for products in different categories. This uniformity in average ratings indicates that customers perceive the quality or satisfaction level of products across various categories to be relatively consistent.
# 
# Having a consistent average rating across product categories can be valuable for businesses as it implies that customers have similar expectations and perceptions of quality regardless of the type of product they purchase. It allows businesses to focus on maintaining and improving the overall customer experience and product quality across the board.
# 
# It is important to note that this conclusion is based on the available data and the calculation of the average rating. It assumes that the data accurately represents the views and opinions of customers. Further analysis and data collection may be necessary to validate this conclusion and explore any potential variations or trends in average ratings across different product categories.
# 
# In summary, based on the available data, the average rating given by customers for each product category is consistent, with an average rating of 3.7. This suggests a general satisfaction level and perception of quality that is relatively uniform across different categories.

# In[ ]:


#4.7 Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?


# In[87]:


shop.columns


# In[88]:


shop['Subscription Status'].unique()


# In[90]:


# Convert 'Purchase Amount (USD)' to numeric if it's not already
shop['Purchase Amount (USD)'] = pd.to_numeric(shop['Purchase Amount (USD)'], errors='coerce')

# Plot using Seaborn
sns.barplot(data=shop, x='Subscription Status', y='Purchase Amount (USD)')


# In[91]:


shop['Purchase Amount (USD)'].sum()


# In[98]:


shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()


# CONCLUSION:
#     
# Based on the analysis conducted, it can be concluded that there are no notable differences in purchase behavior between subscribed and non-subscribed customers. The data suggests that both subscribed and non-subscribed customers exhibit similar purchasing patterns, with no significant variations observed.
# 
# This finding indicates that customers, regardless of their subscription status, demonstrate comparable purchase behavior. It suggests that factors such as product preferences, pricing, marketing strategies, and overall customer experience are relatively consistent for both subscribed and non-subscribed customers.
# 
# Having similar purchase behavior between subscribed and non-subscribed customers can be advantageous for businesses. It allows them to develop marketing campaigns and strategies that cater to a broader customer base, rather than focusing solely on specific segments.
# 
# However, it's important to note that this conclusion is based on the available data and may not account for potential variations at a more granular level, such as specific product categories or customer segments. Further analysis and data collection at a more detailed level may be required to capture any localized differences in purchase behavior.
# 
# Overall, the findings indicate that, at a high level, there are no notable differences in purchase behavior between subscribed and non-subscribed customers, suggesting a consistent consumer landscape across both groups.
# 
# 

# In[ ]:


#4.8 Which payment method is the most popular among customers?


# In[101]:


shop.columns


# In[103]:


shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending=False)


# In[104]:


shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()


# In[105]:


fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()


# In[107]:


# Convert 'Purchase Amount (USD)' to numeric if it's not already
shop['Purchase Amount (USD)'] = pd.to_numeric(shop['Purchase Amount (USD)'], errors='coerce')

# Plot using Seaborn
sns.barplot(data=shop, x='Payment Method', y='Purchase Amount (USD)')


# CONCLUSION:
# 
# Based on the provided data, it can be concluded that there is no significant difference in popularity among the listed payment methods among customers. The data indicates that Debit Card, Credit Card, Bank Transfer, Cash, PayPal, and Venmo all have similar popularity rates, with only slight variations observed.
# 
# The popularity rates for each payment method range from approximately 58.95% to 60.92%. These small differences suggest that customers do not exhibit strong preferences for a specific payment method and that the distribution of payment method usage is relatively balanced.
# 
# It is important to note that this conclusion is based on the available data and may not capture the entire customer base or reflect specific regional or demographic preferences. Further analysis and data collection may be necessary to validate these findings and gain a more comprehensive understanding of payment method preferences among customers.
# 
# Overall, the data suggests that businesses should consider offering a variety of payment options to cater to the diverse preferences of their customers. Providing a range of payment methods can enhance convenience, improve customer satisfaction, and accommodate various customer preferences and needs.

# In[ ]:


#4.9 Do customers who use promo codes tend to spend more than those who don't?


# In[108]:


shop.columns


# In[109]:


shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()


# In[110]:


fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()


# In[111]:


fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()


# CONCLUSION:
# 
# Based on the analysis conducted, it can be concluded that there is a notable difference in the usage of promo codes between male and female customers. The data suggests that male customers tend to use promo codes more frequently compared to female customers, while female customers have a lower tendency to utilize promo codes.
# 
# This finding indicates that promo code usage and its impact on customer spending behavior may vary based on gender. Male customers may be more responsive to promotional offers and discounts provided through promo codes, leading to higher spending. On the other hand, female customers may have different purchasing preferences or motivations that do not heavily rely on promo codes.
# 
# Understanding these gender-based differences in promo code usage can be valuable for businesses in designing targeted marketing strategies. By tailoring promotional offers and discounts to align with the preferences and behaviors of male and female customers, businesses can effectively engage and incentivize both customer segments.
# 
# However, it is important to note that this conclusion is based on the available data and may not capture the entire customer base or account for other influencing factors. Further analysis and data collection may be necessary to validate this finding and gain a more comprehensive understanding of the relationship between promo code usage, gender, and customer spending.
# 
# In summary, the analysis suggests that male customers tend to use promo codes more frequently than female customers. This highlights the importance of considering gender-based differences in promo code usage when devising marketing strategies and targeting specific customer segments.
# 

# In[ ]:


#4.10 How does the frequency of purchases vary across different age groups?


# In[112]:


shop.columns


# In[116]:


# we are cutting the age into some category and storing in the different column
shop['Age_category'] = pd.cut(shop['Age'],
                                bins= [0,15, 18 , 30 , 50 , 70] , 
                                    labels= ['child' , 'teen' , 'Young Adults' ,'Middle-Aged Adults','old'] )

shop[['Age' , 'Age_category']]


# In[117]:


shop['Age_category'].unique()


# In[118]:


shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()


# In[119]:


px.sunburst(shop , path=['Frequency of Purchases','Age_category'] , values='Age')


# CONCLUSION:
# 
# Based on the analysis conducted, it can be concluded that the frequency of purchases varies across different age groups, with the "old" category exhibiting the highest frequency of purchases.
# 
# The data suggests that individuals in the "old" age group tend to make more frequent purchases compared to other age groups. This finding indicates that older individuals may have more disposable income or a higher propensity to engage in regular purchasing behavior.
# 
# The observed trend of higher purchase frequency among the "old" age group can be attributed to several factors. Older individuals may have established spending patterns, greater financial stability, or specific needs that require frequent purchases. Additionally, factors such as retirement, lifestyle choices, and generational differences may contribute to the higher frequency of purchases in this age group.
# 
# Understanding the variations in purchase frequency across different age groups can be valuable for businesses in tailoring marketing strategies and product offerings. By targeting the specific needs and preferences of older individuals, businesses can potentially capitalize on their higher purchasing frequency and develop products, services, and promotions that cater to this customer segment.
# 
# However, it is important to note that this conclusion is based on the available data and may not capture the entire population or account for other influencing factors. Further analysis and data collection may be necessary to validate this finding and explore any potential variations or limitations in the relationship between age groups and purchase frequency.
# 
# In summary, the analysis suggests that the "old" age category has the highest frequency of purchases compared to other age groups. This highlights the importance of considering age-related differences in purchase behavior when developing marketing strategies and targeting specific customer segments.
# 
# 

# In[ ]:


#4.11 Are there any correlations between the size of the product and the purchase amount?


# In[120]:


shop.columns


# In[122]:


shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()


# In[123]:


print(shop_group)


# In[124]:


fig = px.bar(shop_group, x = 'Size' , y = 'Purchase Amount (USD)')
fig.show()


# CONCLUSION:
# 
# After examining the available data, it can be concluded that there is a correlation between the size of the product and the purchase amount. The analysis reveals that the purchase amount varies across different product sizes, with medium-sized products having the highest purchase amount, followed by large-sized products, small-sized products, and XL-sized products.
# 
# Medium-sized Products: The data indicates that medium-sized products have the highest purchase amount. This suggests that customers are willing to spend more on products that fall within the medium size range. The reasons behind this preference could include factors like versatility, affordability, or popularity of products in this size category.
# 
# Large-sized Products: Following medium-sized products, the data shows that large-sized products have the second-highest purchase amount. This suggests that customers are willing to invest a substantial amount in larger-sized products, potentially indicating a preference for items with more capacity or enhanced features.
# 
# Small-sized Products: The analysis reveals that small-sized products have the third-highest purchase amount. Although smaller in size, these products still attract customer interest and result in significant purchases. The reasons behind this could be factors like affordability, convenience, or specific use cases where compactness is valued.
# 
# XL-sized Products: Among the product sizes examined, XL-sized products have the fourth-highest purchase amount. While still attracting purchases, XL-sized products appear to be less popular than medium, large, and small-sized products. The reasons behind this could be factors like limited demand for extra-large items or higher prices associated with larger sizes.
# 
# It is important to note that these conclusions are based on the available data. Factors such as product category, market trends, and consumer preferences may influence the correlation between product size and purchase amount. Further analysis, including market research or customer surveys, may provide additional insights into the specific drivers behind customer purchasing behavior related to product size.
# 
# Understanding the correlation between product size and purchase amount can assist businesses in optimizing their product offerings and pricing strategies, ensuring they align with customer preferences and maximize sales potential.

# In[ ]:


#4.12 Which shipping type is preferred by customers for different product categories?


# In[125]:


shop.columns


# In[128]:


shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending=False)


# *WHAT IS STANDARD, FREE, EXPRESS, STORE PICKUP, NEXT DAY AIR,AND 2-DAY SHIPPING?
# 
# 
# The terms you mentioned refer to different shipping options or services that are commonly offered by retailers or shipping providers. Here's a brief explanation of each term:
# 
# Standard Shipping: Standard shipping is a commonly available shipping option that typically offers delivery within a specified timeframe. The timeframe may vary depending on the retailer and the shipping destination, but it is generally longer than expedited or express shipping options.
# 
# Free Shipping: Free shipping is a promotional offer where the retailer covers the cost of shipping for the customer. It allows customers to receive their orders without incurring any additional shipping charges. Free shipping is often subject to specific conditions, such as reaching a minimum purchase amount or applying to select items or locations.
# 
# Next Day Air: Next Day Air is an expedited shipping service that guarantees delivery of the package by the next business day. It is typically faster than standard shipping but may come with a higher shipping fee compared to standard options.
# 
# Express Shipping: Express shipping refers to a faster shipping option that expedites the delivery of the package. It usually delivers the package within a shorter timeframe compared to standard shipping but may come with an additional shipping cost.
# 
# Store Pickup: Store pickup allows customers to place an order online and pick it up directly from a physical store location instead of having it shipped to their address. This option is convenient for customers who prefer to collect their purchases in person or want to avoid shipping fees.
# 
# 2-Day Shipping: 2-day shipping guarantees delivery within two business days. It is an expedited shipping service that provides faster delivery than standard shipping but may come with an additional fee.
# 
# It's important to note that the specific terms and services offered may vary between retailers or shipping providers. It is recommended to check with the retailer or shipping carrier for detailed information about their shipping options and associated costs or timeframes.

# CONCLUSION:
# 
# After analyzing the data, it can be concluded that customers have different preferences for shipping types depending on the product category. The following observations were made:
# 
# Clothing Category: The preferred shipping type for the clothing category is standard shipping. Customers tend to choose this shipping option when purchasing clothing items. This preference may be influenced by factors such as convenience, cost-effectiveness, and the availability of tracking services for standard shipping.
# 
# Accessories Category: For the accessories category, store pickup shipping is the preferred option. Customers opt to pick up their accessories directly from a physical store location. This choice may be driven by a desire for immediate access to the purchased items, avoiding shipping fees, or the possibility of trying on or inspecting the accessories before finalizing the purchase.
# 
# Footwear Category: Free shipping emerges as the preferred shipping type for the footwear category. Customers prioritize receiving their footwear purchases without incurring any additional shipping charges. This preference may be influenced by the perceived value of free shipping and the potential cost savings associated with it.
# 
# Outerwear Category: Similar to the accessories category, store pickup shipping is the preferred option for the outerwear category. Customers choose to collect their outerwear purchases directly from a physical store location. This preference may be driven by factors such as the need to try on the outerwear for proper fit, ensuring customer satisfaction, and potentially avoiding potential return or exchange shipping costs.
# 
# These conclusions are based on the available data and indicate the general preferences observed in the given product categories. It is important to note that individual customer preferences may vary, and other factors such as location, availability, and specific promotions or incentives offered by retailers may influence shipping type preferences.
# 
# Understanding the preferred shipping types for different product categories can assist retailers in tailoring their shipping options and strategies to better meet customer expectations and increase customer satisfaction.
# 

# In[129]:


shop['Shipping_Category'] =shop['Shipping Type'].map({'Express': 0, 'Free Shipping': 1, 'Next Day Air': 2,
                                                       'Standard': 3, '2-Day Shipping': 4, 'Store Pickup': 5})


# In[130]:


shop['Category'].unique()


# In[131]:


shop['Category_num'] =shop['Category'].map({'Clothing':1, 'Footwear':2, 'Outerwear':3, 'Accessories':4})


# In[ ]:


#4.13 How does the presence of a discount affect the purchase decision of customers?


# In[132]:


shop.columns


# In[133]:


shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()


# In[134]:


px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')


# In[135]:


fig = px.sunburst(shop , path = ['Gender', 'Discount Applied'], values= 'Purchase Amount (USD)' , color = 'Gender')

fig.show()


# CONCLUSION:
# 
# Upon examining the data, it can be concluded that the presence of a discount has an impact on the purchase decisions of customers, with distinct patterns observed between genders. The following observations were made:
# 
# Discount Effect: The presence of a discount appears to have a varying influence on the purchase decisions of male and female customers. Males tend to have more significant discounts available to them compared to females. This difference in discount magnitude suggests that discounts may play a more substantial role in influencing the purchase decisions of male customers.
# 
# Male Purchase Behavior: The data indicates that males make more purchases than females. This finding suggests that the availability of discounts, which are often associated with cost savings, may be a motivating factor for males to make more purchases. The greater purchasing behavior observed in males could be attributed to the combination of higher discount levels and their willingness to take advantage of these discounted offerings.
# 
# Female Purchase Behavior: In contrast to males, females appear to have zero discounts available to them. Despite not having discounts, females still engage in purchases. This finding suggests that factors other than discounts, such as product quality, brand loyalty, or personal preferences, may play a more significant role in the purchase decisions of female customers.
# 
# These conclusions are drawn based on the available data and indicate the disparities in discount availability and purchase behavior between genders. It is important to note that individual customer preferences and purchasing decisions can vary significantly, and discounts may not be the sole determining factor for all customers.
# 
# Understanding the impact of discounts on customer purchase decisions, particularly across different gender segments, can assist businesses in developing targeted marketing strategies and discount campaigns to effectively attract and cater to their customer base.
# 

# In[ ]:


#4.14 Are there any specific colors that are more popular among customers?


# In[136]:


shop.columns


# In[137]:


px.histogram(shop, x= 'Color')


# In[139]:


shop['Color'].value_counts().nlargest(5)


# CONCLUSION:
# 
# Based on the data analysis, it can be concluded that certain colors are more popular among customers. The following observations were made regarding the popularity of colors:
# 
# Olive: Olive emerged as the most popular color among customers. This earthy and versatile shade appears to resonate well with the customer base, potentially due to its natural and neutral appeal.
# 
# Yellow: Yellow ranked as one of the top preferred colors among customers. The vibrant and energetic nature of yellow may attract customers, as it can evoke feelings of positivity and brightness.
# 
# Silver: Silver was found to be a popular color choice among customers. The sleek and sophisticated qualities associated with silver may make it an appealing choice for various products.
# 
# Teal: Teal, a unique blend of blue and green, also emerged as a popular color. The calming and refreshing attributes of teal may be appealing to customers, making it a sought-after choice.
# 
# Green: Green rounded out the top five popular colors among customers. Symbolizing nature and freshness, green may be favored by customers seeking a connection with the environment or desiring a sense of tranquility.
# 
# These conclusions are based on the available data and highlight the preferences observed among customers. It's important to note that color preferences can be influenced by various factors, including personal taste, cultural influences, and current fashion trends. Individual customer preferences may vary significantly.
# 
# Understanding the popularity of specific colors can guide businesses in product development, marketing campaigns, and inventory management, allowing them to align their offerings with customer preferences and potentially enhance overall customer satisfaction.

# In[ ]:


#4.15 What is the average number of previous purchases made by customers?


# In[140]:


shop.columns


# In[141]:


shop['Previous Purchases'].mean()


# CONCLUSION:
# 
# Based on the data analysis, it can be concluded that the average number of previous purchases made by customers is approximately 25.35. This average provides insight into the purchasing behavior and loyalty of the customer base.
# 
# The average number of previous purchases serves as an indicator of customer engagement and repeat business. A higher average suggests that customers tend to make multiple purchases, potentially indicating a loyal customer base that frequently engages with the brand or product offerings.
# 
# Understanding the average number of previous purchases can help businesses assess customer retention rates, evaluate the effectiveness of customer loyalty programs or incentives, and identify areas for improvement in customer engagement and satisfaction.
# 
# It's important to note that the average number of previous purchases may vary across different industries, customer segments, or time periods. Factors such as product type, pricing, customer preferences, and market dynamics can influence the average number of previous purchases.
# 
# By monitoring and analyzing the average number of previous purchases, businesses can gain valuable insights into customer behavior and tailor their strategies to enhance customer satisfaction, increase repeat purchases, and foster long-term customer relationships.
# 

# In[ ]:


#4.16 Are there any noticeable differences in purchase behavior between different locations?


# In[142]:


shop.columns


# In[144]:


shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending=False)


# In[149]:


shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()


# In[150]:


fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()


# CONCLUSION:
# 
# Based on the analysis conducted, it can be concluded that there are no noticeable differences in purchase behavior between different locations (states). The data suggests thatBased on the analysis conducted, it can be concluded that there are no noticeable differences in purchase behavior between different locations (states). The data suggests that all states exhibit similar purchasing patterns, with no significant variations observed.
# 
# This finding indicates that customers across all states demonstrate consistent purchasing behavior, regardless of their geographical location. The absence of noticeable differences in purchase behavior suggests that factors such as product availability, pricing, marketing strategies, and customer preferences are relatively consistent across states.
# 
# Having consistent purchase behavior across different locations can be advantageous for businesses as it allows them to develop standardized marketing campaigns, inventory management strategies, and customer service approaches that cater to a broader customer base.
# 
# However, it's important to note that this conclusion is based on the available data and may not account for potential variations at a more granular level, such as specific cities or regions within states. Further analysis and data collection at a more detailed level may be required to capture any localized differences in purchase behavior.
# 
# Overall, the findings indicate that, at the state level, there are no noticeable differences in purchase behavior among customers, suggesting a consistent consumer landscape across the analyzed locations.
# 

# In[ ]:


#4.17 Is there a relationship between customer age and the category of products they purchase?


# In[151]:


shop.columns


# In[152]:


shop_group = shop.groupby('Category')['Age'].mean().reset_index()


# In[153]:


fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()


# CONCLUSION:
# 
# Based on the analysis conducted, it can be concluded that there is no apparent relationship between customer age and the category of products they purchase. This conclusion is based on the observation that the average age of customers is 44 years, as determined from the bar plot.
# 
# The bar plot provided insights into the distribution of customer age across different product categories. However, it does not reveal any distinct patterns or trends that suggest a strong correlation between age and product category preferences.
# 
# It is worth noting that while the average age can provide a general understanding of the customer base, it may not capture the full complexity of the relationship between age and product categories. Variations and preferences within specific age groups or other demographic factors could still exist, which might require further analysis to uncover.
# 
# To gain a more comprehensive understanding of the relationship between customer age and product categories, it is recommended to conduct additional analyses such as correlation analysis, regression analysis, or segmentation analysis. These techniques can help identify any significant relationships or patterns that may be present within specific age groups or across different product categories.
# 
# In summary, based on the available information and the bar plot analysis, there is no conclusive evidence to support a direct relationship between customer age and the category of products they purchase. Further analysis and exploration are needed to draw more definitive conclusions regarding potential connections between age and product preferences.
# 

# In[ ]:


#4.18 How does the average purchase amount differ between male and female customers?


# In[154]:


shop.columns


# In[155]:


shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()


# In[159]:



fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()


# In[157]:


px.sunburst(data_frame= shop , path = ['Gender' ,'Age_category'] , values='Purchase Amount (USD)')


# CONCLUSION:
# 
# Based on the available data, it can be observed that the average purchase amount differs between male and female customers, with male customers tending to have a higher average purchase amount.
# 
# This finding suggests that, on average, male customers tend to spend more on purchases compared to female customers. Several factors could contribute to this difference, including variations in purchasing preferences, product choices, or spending behaviors between genders.
# 
# Understanding the variations in average purchase amount between male and female customers can provide valuable insights for businesses. It can help tailor marketing strategies, product offerings, and customer experiences to better cater to the specific needs and preferences of each gender.
# 
# However, it is crucial to note that this conclusion is based on the available data and may not capture the entire customer base or account for individual variations. Further analysis and data collection are necessary to validate this observation and gain a more comprehensive understanding of the purchasing behaviors of male and female customers.
# 
