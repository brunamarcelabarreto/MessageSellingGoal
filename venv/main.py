import pandas as pd
from twilio.rest import Client

# Account SID from twilio.com/console
account_sid = "personal sid"
# Auth Token from twilio.com/console
auth_token  = "personal token"

client = Client(account_sid, auth_token)

months_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for month in months_list:
  sell_table = pd.read_excel(f'{month}.xlsx')
  if (sell_table['Vendas'] > 55000).any():
    seller = sell_table.loc[sell_table['Vendas'] > 55000, 'Vendedor'].values[0]
    sales = sell_table.loc[sell_table['Vendas'] > 55000, 'Vendas'].values[0]
    print(f'No mês {month} alguém bateu a meta. Vendedor: {seller}, Vendas: {sales}')
    message = client.messages.create(
      to="my number", 
      from_="number generated from twilio",
      body=f'No mês {month} alguém bateu a meta. Vendedor: {seller}, Vendas: {sales}')
    print(message.sid)


