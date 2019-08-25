import requests
import json
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from dashboard.form import TagForm
from dashboard.endpoints_github import URL_REPOSITORY_TOPIC, \
                                       HEADERS_REPOSITORY_TOPIC
from dashboard.views import DashboardView


class EditTagView(LoginRequiredMixin, FormView):
    template_name = 'edit_tag.html'
    form_class = TagForm

    def get_form_kwargs(self):
        kwargs = super(EditTagView, self).get_form_kwargs()
        name_repository = self.kwargs['name_repository']
        tag_values = self._get_tags_repository(name_repository)
        kwargs.update({'tag_values': tag_values, 'name': name_repository})
        return kwargs

    def form_valid(self, form):
        form_data = form.cleaned_data
        token = DashboardView._get_token_user(self)
        data_json = self.format_tags_to_json(form_data)
        headers = HEADERS_REPOSITORY_TOPIC
        url = URL_REPOSITORY_TOPIC.format(
            self.request.user, form_data['name_repository'], token)
        response = requests.put(url, headers=headers, data=data_json)

        if response.status_code == 200:
            messages.success(self.request, 'Tags alteradas com sucesso!')
            return redirect('dashboard')
        else:
            messages.error(self.request, 'Ocorreu um erro ao alterar a tag!')
            return render(self.request, 'edit_tag.html', {'form': form})

    def format_tags_to_json(self, form_data):
        if len(form_data['tag']) > 0:
            list_tags = form_data['tag'].lower().split(',')
        else:
            list_tags = list()

        data = {"names": list_tags}
        data_json = json.dumps(data)
        return data_json

    def _get_tags_repository(self, name_repository):
        token = DashboardView._get_token_user(self)
        headers = HEADERS_REPOSITORY_TOPIC
        url = URL_REPOSITORY_TOPIC.format(
            self.request.user, name_repository, token)
        response = requests.get(url, headers=headers)

        tags = self._format_tags_to_string(response.json())
        return tags

    def _format_tags_to_string(self, tags):
        if 'names' in tags:
            tag_string = ','.join(tags['names'])
        else:
            tag_string = ''

        return tag_string
