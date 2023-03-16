import rpa as r
import pandas as pd


r.init(turbo_mode=True)
r.url('https://rpachallenge.com')

r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a')

df = pd.read_excel('challenge.xlsx', engine='openpyxl')
df['Phone Number'] = df['Phone Number'].astype(str)

r.click('//*[text()="Start"]')

for i in range(len(df.axes[0])):
    r.type('//*[@ng-reflect-name="labelFirstName"]', df['First Name'][i])
    r.type('//*[@ng-reflect-name="labelLastName"]', df['Last Name '][i])
    r.type('//*[@ng-reflect-name="labelCompanyName"]', df['Company Name'][i])
    r.type('//*[@ng-reflect-name="labelRole"]', df['Role in Company'][i])
    r.type('//*[@ng-reflect-name="labelAddress"]', df['Address'][i])
    r.type('//*[@ng-reflect-name="labelEmail"]', df['Email'][i])
    r.type('//*[@ng-reflect-name="labelPhone"]', df['Phone Number'][i])
    r.click('//*[@value="Submit"]')
r.snap('page', 'score.png')
r.wait(5)
r.close()