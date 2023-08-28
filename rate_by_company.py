INITIAL_COMPANY_DATA = {'quantity': 0, 'rate_sum': 0.0}

def calc_rate_sum_by_company(data):
  rate_sum_by_company = dict()

  for item in data:
    company = item.get('company')
    companyData = rate_sum_by_company.get(company)

    # Se não existem ainda a empresa no dicionario,
    # esse if cria uma empresa com dados iniciais
    if companyData == None:
      companyData = dict(INITIAL_COMPANY_DATA)
    
    quantity = companyData.get('quantity')
    upated_quantity =  quantity + 1

    rate_sum = companyData.get('rate_sum')
    updated_rate_sum = rate_sum + float(item['rate'])

    companyData.update({'quantity':upated_quantity, 'rate_sum': updated_rate_sum})
    rate_sum_by_company.update({company: companyData})
  
  return rate_sum_by_company

def calc_rate_by_company(rate_sum_by_company):
  rate_by_company = dict()

  # key seria o nome de cara empresa
  for key in rate_sum_by_company:
    rate_sum = rate_sum_by_company.get(key)
    quantity = rate_sum.get('quantity')
    rate_sum = rate_sum.get('rate_sum')

    rate_by_company.update({key: rate_sum / quantity})
  
  return rate_by_company


def get_rate_by_company(data):
  rate_sum_by_company = calc_rate_sum_by_company(data)
  rate_by_company = calc_rate_by_company(rate_sum_by_company)

  return rate_by_company
