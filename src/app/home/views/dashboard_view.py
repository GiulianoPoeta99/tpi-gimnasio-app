from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'home/dashboard.html'
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MotionPath'
        context['description'] = 'Pagina de inicio de MotionPath.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio'},
        ]
        return context
