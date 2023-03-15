import rpa as r
import pandas as pd
# to use Pandas to read Excel, pip install pandas -> pip install xlrd -> pip install openpyxl # noqa

r.init(turbo_mode=True)
r.url('https://rpachallenge.com')

# download() is used here but you can also do a click() on the button
r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a')

# load and prepare all data to string
df = pd.read_excel('challenge.xlsx', engine='openpyxl')
df['Phone Number'] = df['Phone Number'].astype(str)

# timer starts after running this step
r.click('//*[text()="Start"]')

# loop through and fill in all fields
for i in range(len(df.axes[0])):
    r.type('//*[@ng-reflect-name="labelFirstName"]', df['First Name'][i])
    r.type('//*[@ng-reflect-name="labelLastName"]', df['Last Name '][i])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', df['Company Name'][i])
    r.type('//*[@ng-reflect-name="labelRole"]', df['Role in Company'][i])
    r.type('//*[@ng-reflect-name="labelAddress"]', df['Address'][i])
    r.type('//*[@ng-reflect-name="labelEmail"]', df['Email'][i])
    r.type('//*[@ng-reflect-name="labelPhone"]', df['Phone Number'][i])
    r.click('//*[@value="Submit"]')

# page as identifier means the webpage
r.snap('page', 'score.png')
r.wait(10)
r.close()