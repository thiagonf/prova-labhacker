from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.staticfiles.templatetags.staticfiles import static
import requests
from dashboard.endpoints_github import URL_REPOSITORIES_USER, URL_INFO_USER, \
                                        HEADERS_REPOSITORY_TOPIC


class DashboardView(LoginRequiredMixin, TemplateView):
    '''
    Initial view that redirects user to login or dashboard
    '''
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        all_repositories = self._get_all_repositories()
        open_repositories = self._get_open_repositories(all_repositories)
        private_repositories = self._get_private_repositories(all_repositories)

        context['repositories'] = [{'name': 'all',
                                    'count': len(all_repositories),
                                    'repositories': all_repositories},
                                   {'name': 'open',
                                    'count': len(open_repositories),
                                    'repositories': open_repositories},
                                   {'name': 'private',
                                    'count': len(private_repositories),
                                    'repositories': private_repositories}]

        self.request.session['avatar'] = self._get_avatar_github()
        return context

    def _get_all_repositories(self):
        token = self._get_token_user()
        affiliation = 'owner'
        repository_per_page = 100
        headers = HEADERS_REPOSITORY_TOPIC
        url = URL_REPOSITORIES_USER.format(
            token, affiliation, repository_per_page)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            if 'next' in response.links.keys():
                list_repositories = self._get_more_page_repository(
                    response, token)
            else:
                list_repositories = response.json()
        else:
            list_repositories = list()

        return list_repositories

    def _get_more_page_repository(self, response, token):
        repositories = response.json()

        while 'next' in response.links.keys():
            response = requests.get(response.links['next']['url'],
                                    headers={"Authorization": token})
            repositories.extend(response.json())

        return repositories

    def _get_token_user(self):
        user = self.request.user
        social = user.social_auth.get(provider='github')
        token = social.extra_data['access_token']
        return token

    def _get_open_repositories(self, all_repositories):
        list_open_repositories = list()
        for repository in all_repositories:
            if not repository['private']:
                list_open_repositories.append(repository)
        return list_open_repositories

    def _get_private_repositories(self, all_repositories):
        list_private_repositories = list()
        for repository in all_repositories:
            if repository['private']:
                list_private_repositories.append(repository)
        return list_private_repositories

    def _get_avatar_github(self):
        user = self.request.user
        url = URL_INFO_USER.format(user.username)
        response = requests.get(url)
        data = response.json()
        if 'avatar_url' in data:
            avatar = data['avatar_url']
        else:
            avatar = static('images/default-user.jpg')

        return avatar
