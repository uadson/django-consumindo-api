from django.views.generic import TemplateView

import json
import requests
import pandas as pd


# class based views
class DataView(TemplateView):
    template_name = 'core/data.html'

    def get_context_data(self, **kwargs):

        # getting url with data
        url = 'http://127.0.0.1:8000/data/'
        data_url = requests.get(url)

        # converting the data into a dictionary
        data_dict = json.loads(data_url.content)

        # creating a dataframe with the data
        data = pd.DataFrame(data_dict['data'])

        # creating the excel file
        writer = pd.ExcelWriter('date.xlsx', engine='xlsxwriter')

        # saving dataframe data in excel file
        data.to_excel(writer, sheet_name='Sheet1')
        writer.save()

        context = super(DataView, self).get_context_data(**kwargs)

        # displaying dataframe data in a template
        context['data'] = data.to_html()

        return context
