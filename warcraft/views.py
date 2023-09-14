from django.views.generic import TemplateView


class StartView(TemplateView):
    template_name = 'warcraft/start_page.html'


class AboutView(TemplateView):
    template_name = 'warcraft/about_page.html'


class GalleryView(TemplateView):
    template_name = 'warcraft/gallery_page.html'


class VideoView(TemplateView):
    template_name = 'warcraft/video_page.html'
